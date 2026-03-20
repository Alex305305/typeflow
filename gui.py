# gui.py

import subprocess
import os
import tkinter as tk
import time
from config import BG_COLOR, FG_COLOR, FONT_FAMILY, FONT_SIZE_INPUT, FONT_SIZE_PROMPT, CORRECT_COLOR, ERROR_COLOR, CURRENT_BG
from core import TypingSession, save_session_to_csv
from PIL import Image, ImageTk
import config
from lessons import LESSONS, LESSON_NAMES_RU, get_lesson, get_next_level
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))


class TypingGUI:
    def __init__(self, root: tk.Tk, track: str, level_key: str, language: str):
        self.root = root
        self.language = language
        self.track = track
        self.level_key = level_key
        self.session = TypingSession(track, level_key, language)
        self.diamonds = 0
        self.sound_enabled = True  # звук включён по умолчанию

        # Обязательно: создаём ВСЕ атрибуты ДО setup_ui() Фон сразу
        # Создаём холст для фона
        self.bg_canvas = tk.Canvas(self.root, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        # Список для хранения ссылок на изображения (защита от GC)
        self._bg_photos = None
        # ID текущего изображения на холсте
        self.bg_image_id = None

        # Привязываем событие изменения размера
        self.root.bind("<Configure>", self.on_resize)

        # Фон загрузится после отображения окна
        self.root.after(300, self.init_background)
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Press Start 2P", 10),
            bg=BG_COLOR,
            fg="white"
        )
        self.status_label.pack(side="bottom", pady=2)

        self.current_index = 0
        self.user_input = ""
        self.is_training_ended = False

        # Режим отображения: False = Minecraft, True = Terminal
        self.devops_mode = False
        # Ссылки на меню-панель (будет создано позже)
        self.menu_panel = None
        self.mode_label = None

        self.setup_ui()

        # Клик по окну снимает фокус с entry
        self.root.bind("<Button-1>", self.on_window_click)

        self.chest_window = None
        self.create_chest_window()

    def play_sound(self, name: str):
        """Надёжное воспроизведение звука через paplay."""
        import subprocess, os
        # Путь: sounds/название.wav
        path = os.path.join("sounds", f"{name}.wav")
        if not os.path.isfile(path):
            print(f"⚠️ Звук не найден: {path}")
            return
        try:
            # Используем полный путь к paplay + shell=True для надёжности
            subprocess.run(["/usr/bin/paplay", path],
                           stdout=subprocess.DEVNULL,
                           stderr=subprocess.DEVNULL,
                           shell=False)  # ← shell=False безопаснее
        except FileNotFoundError:
            print("❌ paplay не установлен. Установите: sudo apt install pulseaudio-utils")
        except Exception as e:
            print("❌ Ошибка воспроизведения:", e)

    def restart(self):
        self.play_sound("закрытие_программы")  # ← звук при перезапуске
        self.root.destroy()
        new_root = tk.Tk()
        new_root.title("Тренажер слепой печати")
        new_root.geometry("800x600")
        new_root.configure(bg=BG_COLOR)
        app = TypingGUI(new_root, self.track, self.level_key, self.language)
        new_root.mainloop()


    def setup_ui(self):
        # Убираем стандартное меню (не создаём menu = tk.Menu)
        # Создаём кастомную панель меню
        self.menu_panel = tk.Frame(
            self.root,
            bg='#3C2A1E',  # цвет земли
            height=40,
            relief='raised',
            bd=3
        )
        self.menu_panel.pack(fill="x", padx=5, pady=5)
        self.menu_panel.pack_propagate(False)

        # Кнопки меню
        buttons = [
            ("📁 Файл", self.show_file_menu),
            ("📊 История", self.show_history),
            ("⚙️ Настройки", self.show_settings),
            (("📚 Уроки", self.show_lesson_selector)),
            ("💎 Достижения", self.show_achievements)
        ]

        for text, command in buttons:
            # Рамка кнопки (эффект блока)
            btn_frame = tk.Frame(
                self.menu_panel,
                bg='#8B8B8B',
                relief='raised',
                bd=2
            )
            btn_frame.pack(side="left", padx=3, pady=3)

            btn = tk.Button(
                btn_frame,
                text=text,
                command=command,
                bg='#B0B0B0',
                fg='white',
                font=("Press Start 2P", 8),
                relief='flat',
                padx=8,
                pady=3,
                cursor='hand2'
            )
            btn.pack(padx=1, pady=1)

            # Эффекты наведения
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg='#D0D0D0'))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg='#B0B0B0'))
            btn.bind("<Button-1>", lambda e, b=btn: b.configure(relief='sunken'))
            btn.bind("<ButtonRelease-1>", lambda e, b=btn: b.configure(relief='flat'))

        # Индикатор режима (Minecraft/Terminal)
        self.mode_frame = tk.Frame(
            self.menu_panel,
            bg='#2D2D2D',
            relief='sunken',
            bd=2
        )
        self.mode_frame.pack(side="right", padx=10, pady=3)

        self.mode_label = tk.Label(
            self.mode_frame,
            text="⚡ Minecraft",
            font=("Press Start 2P", 7),
            bg='#2D2D2D',
            fg='#7CFC00'
        )
        self.mode_label.pack(padx=5, pady=2)

        # Привязываем клик для смены режима
        self.mode_frame.bind("<Button-1>", self.toggle_mode)
        self.mode_label.bind("<Button-1>", self.toggle_mode)

        # Основной canvas (прозрачный фон)
        self.canvas = tk.Canvas(
            self.root,
            bg=BG_COLOR,  # прозрачный фон (будет виден фон главного окна)
            highlightthickness=0,
            height=60
        )
        self.canvas.pack(pady=20, padx=40, fill="x")
        self.canvas.focus_set()

        # Привязываем клавиши
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<BackSpace>", self.on_backspace)
        self.root.bind("<Return>", lambda e: self.submit_current())

        # Статистика (внизу)
        self.stats_var = tk.StringVar(value="Точность: — | WPM: —")
        self.stats_label = tk.Label(
            self.root,
            textvariable=self.stats_var,
            bg=BG_COLOR,
            fg="#a0a0a0",
            font=("Press Start 2P", 12),
            wraplength=700,
            justify="center"
        )
        self.stats_label.pack(pady=20, padx=40, fill="x")

        # Алмазы — правый верхний угол
        self.diamonds_label = tk.Label(
            self.root,
            text=f"Алмазов: {self.diamonds}",
            font=("Press Start 2P", 12),
            bg=BG_COLOR,
            fg="#4CC9F0"
        )
        """ relx=0.98  – почти у правого края.
            rely=0.98  – почти у нижнего края.
            anchor="se" – точка привязки – юго-восток (правый нижний угол метки)
        """
        self.diamonds_label.place(relx=0.98, rely=0.98, anchor="se")

        # Статус CAPS LOCK
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Press Start 2P", 10),
            bg=BG_COLOR,
            fg="white"
        )
        self.status_label.pack(side="bottom", pady=2)

        # Первое слово
        self.update_prompt()

        # Звук приветствия
        self.root.after(500, lambda: self.play_sound("переход_на_другой_уровень"))

    def show_file_menu(self):
        """Выпадающее меню 'Файл' в стиле Minecraft"""
        file_popup = tk.Menu(self.root, tearoff=0, bg='#2D2D2D', fg='white',
                             font=("Press Start 2P", 8), bd=2, relief='raised')
        file_popup.add_command(
            label="🔄 Перезапустить урок",
            command=self.restart,
            foreground='#7CFC00'
        )
        file_popup.add_separator(background='#8B8B8B')
        file_popup.add_command(
            label="📊 Статистика",
            command=self.show_history,
            foreground='#FFA500'
        )
        file_popup.add_separator(background='#8B8B8B')
        file_popup.add_command(
            label="🚪 Выход",
            command=self.root.quit,
            foreground='#FF4444'
        )
        # Показываем под курсором
        x = self.root.winfo_pointerx()
        y = self.root.winfo_pointery()
        file_popup.tk_popup(x, y)

    def show_settings(self):
        """Окно настроек"""
        settings_win = tk.Toplevel(self.root)
        settings_win.title("⚙️ Настройки")
        settings_win.geometry("450x350")
        settings_win.configure(bg='#2D2D2D')
        settings_win.resizable(False, False)

        # Заголовок
        tk.Label(
            settings_win,
            text="⚙️ НАСТРОЙКИ",
            font=("Press Start 2P", 16),
            bg='#2D2D2D',
            fg='#FFD700'
        ).pack(pady=10)

        # Фрейм для содержимого
        content = tk.Frame(settings_win, bg='#3C2A1E', relief='sunken', bd=3)
        content.pack(padx=20, pady=10, fill="both", expand=True)

        # 1. Звук
        sound_var = tk.BooleanVar(value=self.sound_enabled)
        tk.Checkbutton(
            content,
            text="🔊 Включить звуки",
            variable=sound_var,
            bg='#4C4C4C',
            fg='white',
            selectcolor='#2D2D2D',
            font=("Press Start 2P", 10),
            anchor='w'
        ).pack(fill="x", padx=20, pady=10)

        # 2. Тема (Minecraft / Terminal)
        theme_var = tk.StringVar(value="minecraft" if not self.devops_mode else "terminal")
        tk.Label(
            content,
            text="🎨 Тема оформления:",
            bg='#4C4C4C',
            fg='white',
            font=("Press Start 2P", 10)
        ).pack(padx=20, pady=(10, 0), anchor='w')

        theme_frame = tk.Frame(content, bg='#4C4C4C')
        theme_frame.pack(padx=20, pady=5, fill="x")

        tk.Radiobutton(
            theme_frame,
            text="Minecraft",
            variable=theme_var,
            value="minecraft",
            bg='#4C4C4C',
            fg='white',
            selectcolor='#2D2D2D',
            font=("Press Start 2P", 8)
        ).pack(side="left", padx=5)

        tk.Radiobutton(
            theme_frame,
            text="Terminal",
            variable=theme_var,
            value="terminal",
            bg='#4C4C4C',
            fg='white',
            selectcolor='#2D2D2D',
            font=("Press Start 2P", 8)
        ).pack(side="left", padx=5)

        # 3. Кнопка сброса статистики
        tk.Button(
            content,
            text="🗑️ Сбросить статистику",
            command=self.reset_statistics,
            bg='#FFA500',
            fg='black',
            font=("Press Start 2P", 8),
            padx=10,
            pady=5
        ).pack(pady=20)

        # Кнопки сохранения и отмены
        btn_frame = tk.Frame(settings_win, bg='#2D2D2D')
        btn_frame.pack(pady=10)

        def save():
            # Сохраняем настройки
            self.sound_enabled = sound_var.get()
            # Применяем тему
            if theme_var.get() == "minecraft" and self.devops_mode:
                self.toggle_mode()  # переключаем на Minecraft
            elif theme_var.get() == "terminal" and not self.devops_mode:
                self.toggle_mode()  # переключаем на Terminal
            settings_win.destroy()
            self.show_minecraft_message("✅ Настройки сохранены", "#7CFC00")

        tk.Button(
            btn_frame,
            text="💾 Сохранить",
            command=save,
            bg='#7CFC00',
            fg='black',
            font=("Press Start 2P", 10),
            padx=20,
            pady=5
        ).pack(side="left", padx=10)

        tk.Button(
            btn_frame,
            text="❌ Отмена",
            command=settings_win.destroy,
            bg='#FF4444',
            fg='white',
            font=("Press Start 2P", 10),
            padx=20,
            pady=5
        ).pack(side="left", padx=10)


    def reset_statistics(self):
        """Сбрасывает файл статистики"""
        try:
            open("typing_history.csv", "w").close()  # очищаем файл
            self.show_minecraft_message("📊 Статистика очищена", "#FFA500")
        except Exception as e:
            self.show_minecraft_message("❌ Ошибка при сбросе", "#FF4444")


    def show_achievements(self):
        """Окно достижений"""
        ach_window = tk.Toplevel(self.root)
        ach_window.title("🏆 Достижения")
        ach_window.geometry("500x400")
        ach_window.configure(bg='#2D2D2D')

        # Заголовок
        title_frame = tk.Frame(ach_window, bg='#8B8B8B', relief='raised', bd=3)
        title_frame.pack(pady=10, padx=20, fill="x")

        tk.Label(
            title_frame,
            text="🏆 ДОСТИЖЕНИЯ",
            font=("Press Start 2P", 16),
            bg='#8B8B8B',
            fg='#FFD700'
        ).pack(pady=5)

        # Список достижений (пример)
        achievements = [
            ("💎 Первый алмаз", "Наберите 100 символов без ошибок", self.diamonds >= 1),
            ("⚡ Скорость света", "Достигните WPM > 60", False),
            ("🔰 Новичок", "Пройдите 10 уроков", False),
            ("🐧 Linux-гуру", "Наберите 1000 команд в терминале", False),
        ]

        for title, desc, earned in achievements:
            ach_frame = tk.Frame(
                ach_window,
                bg='#4C4C4C' if earned else '#2D2D2D',
                relief='raised' if earned else 'sunken',
                bd=2
            )
            ach_frame.pack(pady=5, padx=20, fill="x")

            color = '#FFD700' if earned else '#808080'

            tk.Label(
                ach_frame,
                text=f"{'✅' if earned else '⬜'} {title}",
                font=("Press Start 2P", 10),
                bg='#4C4C4C' if earned else '#2D2D2D',
                fg=color,
                anchor='w'
            ).pack(pady=5, padx=10, fill="x")

            tk.Label(
                ach_frame,
                text=desc,
                font=("Press Start 2P", 7),
                bg='#4C4C4C' if earned else '#2D2D2D',
                fg='white',
                anchor='w'
            ).pack(pady=2, padx=20, fill="x")

    def toggle_mode(self, event=None):
        """Переключение между Minecraft и Terminal режимами"""
        self.devops_mode = not getattr(self, 'devops_mode', False)

        if self.devops_mode:
            self.mode_label.config(text="💻 Terminal", fg="#00FF00")
            self.apply_terminal_style()
        else:
            self.mode_label.config(text="⚡ Minecraft", fg="#7CFC00")
            self.apply_minecraft_style()

        # Перерисовываем текущее упражнение
        self.update_display()

    def apply_terminal_style(self):
        """Стиль терминала (зелёный/чёрный)"""
        # Меняем глобальные цвета (если они используются в отрисовке)
        # Так как CORRECT_COLOR и CURRENT_BG импортированы, меняем через globals?
        # Проще использовать переменные экземпляра, но для простоты переопределим в update_display
        # Сохраним флаг и в update_display будем проверять self.devops_mode
        # Пока просто меняем фон канваса и меток
        self.canvas.configure(bg='black')
        self.stats_label.configure(bg='black', fg='#00FF00')
        # Дополнительно: можно изменить цвета в update_display

    def apply_minecraft_style(self):
        """Возвращаем Minecraft стиль"""
        self.canvas.configure(bg=BG_COLOR) # используем цвет фона
        self.stats_label.configure(bg=BG_COLOR, fg='#a0a0a0')

    def show_minecraft_message(self, text, color):
        """Временное сообщение в стиле Minecraft (по центру)"""
        msg = tk.Label(
            self.root,
            text=text,
            font=("Press Start 2P", 14),
            bg='#2D2D2D',
            fg=color,
            relief='raised',
            bd=3
        )
        msg.place(relx=0.5, rely=0.5, anchor="center")
        self.root.after(2000, msg.destroy)

    def show_lesson_selector(self):
        """Открывает окно выбора урока в стиле Minecraft"""
        track = self.session.track  # берём трек из сессии (beginner/advanced)
        if track not in LESSONS:
            self.show_minecraft_message("❌ Нет уроков для этого уровня", "#FF4444")
            return

        # Создаём окно
        self.lesson_selector = tk.Toplevel(self.root)
        self.lesson_selector.title("📚 Выбор урока")
        self.lesson_selector.geometry("600x500")
        self.lesson_selector.configure(bg='#2D2D2D')
        self.lesson_selector.resizable(False, False)

        # Заголовок
        title_frame = tk.Frame(self.lesson_selector, bg='#8B8B8B', relief='raised', bd=3)
        title_frame.pack(pady=10, padx=20, fill="x")

        track_name = "НОВИЧОК" if track == "beginner" else "ПРОДВИНУТЫЙ"
        tk.Label(
            title_frame,
            text=f"📚 УРОКИ • {track_name}",
            font=("Press Start 2P", 14),
            bg='#8B8B8B',
            fg='#FFD700'
        ).pack(pady=5)

        # Основной фрейм со списком
        list_frame = tk.Frame(self.lesson_selector, bg='#3C2A1E', relief='sunken', bd=3)
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Скроллбар
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        # Список уроков
        self.lesson_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            bg='#4C4C4C',
            fg='white',
            font=("Press Start 2P", 8),
            selectbackground='#7CFC00',
            selectforeground='black',
            bd=0,
            highlightthickness=0,
            height=15
        )
        self.lesson_listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.lesson_listbox.yview)

        # Заполняем список
        self.populate_lesson_list(track)

        # Кнопки
        btn_frame = tk.Frame(self.lesson_selector, bg='#2D2D2D')
        btn_frame.pack(pady=10)

        load_btn = tk.Button(
            btn_frame,
            text="⚡ Загрузить",
            command=self.load_selected_lesson,
            bg='#7CFC00',
            fg='black',
            font=("Press Start 2P", 10),
            padx=20,
            pady=5,
            cursor='hand2'
        )
        load_btn.pack(side="left", padx=10)

        cancel_btn = tk.Button(
            btn_frame,
            text="❌ Отмена",
            command=self.lesson_selector.destroy,
            bg='#FF4444',
            fg='white',
            font=("Press Start 2P", 10),
            padx=20,
            pady=5,
            cursor='hand2'
        )
        cancel_btn.pack(side="left", padx=10)

        # Эффекты наведения
        for btn in (load_btn, cancel_btn):
            btn.bind("<Enter>", lambda e, b=btn: b.configure(bg='#D0D0D0' if b==load_btn else '#FF7777'))
            btn.bind("<Leave>", lambda e, b=btn: b.configure(bg='#7CFC00' if b==load_btn else '#FF4444'))

    def populate_lesson_list(self, track):
        self.lesson_listbox.delete(0, tk.END)
        levels = LESSONS.get(track, {})
        for key in levels.keys():
            # Берём русское название из словаря, если нет — автопреобразование
            display_name = LESSON_NAMES_RU.get(key, key.split('_', 1)[-1].replace('_', ' ').capitalize())
            self.lesson_listbox.insert(tk.END, display_name)

    def load_selected_lesson(self):
        """Загружает выбранный урок в сессию"""
        selection = self.lesson_listbox.curselection()
        if not selection:
            self.show_minecraft_message("❌ Выберите урок!", "#FF4444")
            return

        track = self.session.track
        levels = list(LESSONS.get(track, {}).keys())
        if not levels:
            return

        selected_key = levels[selection[0]]
        # Загружаем упражнения (язык берём из self.language, который сохранён в GUI)
        lesson_words = get_lesson(track, selected_key, self.language)

        if not lesson_words:
            self.show_minecraft_message("❌ Урок пуст", "#FF4444")
            return

        # Обновляем сессию
        self.session.exercises = lesson_words
        self.session.level_key = selected_key  # запоминаем текущий уровень
        self.session.index = 0
        self.session.errors = 0
        self.session.total_typed = 0
        # Если в сессии есть счётчик времени, сбросьте его (например, self.session.start_time = None)

        # Сбрасываем GUI-счётчики
        self.diamonds = 0
        self.update_diamonds_display()

        # Перерисовываем текущее слово
        self.update_prompt()

        # Закрываем окно выбора
        self.lesson_selector.destroy()

        # Показываем сообщение
        display_name = selected_key.split('_', 1)[-1].replace('_', ' ')
        self.show_minecraft_message(f"✅ Загружен: {display_name}", "#7CFC00")

    def update_diamonds_display(self):
        """Обновляет отображение счётчика алмазов"""
        if hasattr(self, 'diamonds_label') and self.diamonds_label.winfo_exists():
            self.diamonds_label.config(text=f"Алмазов: {self.diamonds}")

    def on_enter(self):
        if self.user_input:
            self.submit_current()

    def show_history(self):
        """Показывает историю в стиле терминала"""
        try:
            with open("typing_history.csv", "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            self.show_minecraft_message("❌ История не найдена", "#FF4444")
            return

        # Окно с текстом
        hist_win = tk.Toplevel(self.root)
        hist_win.title("📊 История тренировок")
        hist_win.geometry("600x400")
        hist_win.configure(bg='black')

        text_widget = tk.Text(
            hist_win,
            bg='black',
            fg='#00FF00',
            font=("Courier", 10),
            insertbackground='#00FF00',
            wrap='none'
        )
        text_widget.pack(fill="both", expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(text_widget)
        scrollbar.pack(side="right", fill="y")
        text_widget.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_widget.yview)

        # Заголовок
        text_widget.insert("end", f"{'='*50}\n")
        text_widget.insert("end", "📊 ИСТОРИЯ ТРЕНИРОВОК\n")
        text_widget.insert("end", f"{'='*50}\n\n")

        for line in lines[1:]:  # пропускаем заголовок
            parts = line.strip().split(',')
            if len(parts) >= 3:
                text_widget.insert("end", f"📅 {parts[0]}\n")
                text_widget.insert("end", f"📈 Точность: {parts[1]}%\n")
                text_widget.insert("end", f"⚡ WPM: {parts[2]}\n")
                text_widget.insert("end", f"{'-'*30}\n")

        text_widget.configure(state='disabled')
   # ТУТ НАДО ПОДУМАТЬ МЕНЯТЬ ЛИ!

    def create_chest_window(self):
        if (hasattr(self, 'chest_window') and
                self.chest_window is not None and
                self.chest_window.winfo_exists()):
            return

        self.chest_window = tk.Toplevel(self.root)
        self.chest_window.title("Сундук")
        self.chest_window.geometry("300x200")
        self.chest_window.overrideredirect(True)
        self.chest_window.attributes("-topmost", True)

        # Центрирование относительно главного окна
        root_x = self.root.winfo_rootx()
        root_y = self.root.winfo_rooty()
        root_w = self.root.winfo_width()
        root_h = self.root.winfo_height()
        x = root_x + (root_w - 300) // 2
        y = root_y + (root_h - 200) // 2
        self.chest_window.geometry(f"+{x}+{y}")

        # Canvas
        self.chest_canvas = tk.Canvas(self.chest_window, width=300, height=200, highlightthickness=0)
        self.chest_canvas.pack()

        # Загрузка изображений — безопасно
        try:
            from PIL import Image, ImageTk
            self.chest_closed_img = ImageTk.PhotoImage(
                Image.open("textures/chest_closed.png").resize((300, 200), Image.NEAREST)
            )
            self.chest_open_img = ImageTk.PhotoImage(
                Image.open("textures/chest_open.png").resize((300, 200), Image.NEAREST)
            )
        except Exception as e:
            print("Сундук не загружен:", e)
            # Создаём fallback БЕЗ использования Image.new — чтобы избежать проблемы с локальной переменной
            # Вместо этого просто ставим placeholder-текст или оставляем пустым
            # Загрузка изображений сундука — с гарантией сохранения ссылок
            self.chest_closed_img = None
            self.chest_open_img = None

            try:
                from PIL import Image, ImageTk
                closed_path = "textures/chest_closed.png"
                open_path = "textures/chest_open.png"

                if os.path.isfile(closed_path):
                    img = Image.open(closed_path).resize((300, 200), Image.NEAREST)
                    self.chest_closed_img = ImageTk.PhotoImage(img)
                if os.path.isfile(open_path):
                    img = Image.open(open_path).resize((300, 200), Image.NEAREST)
                    self.chest_open_img = ImageTk.PhotoImage(img)
            except Exception as e:
                print("Сундук: ошибка загрузки изображений:", e)

            # Создаём изображение ТОЛЬКО если оно загружено
            if self.chest_closed_img:
                self.chest_id = self.chest_canvas.create_image(150, 100, image=self.chest_closed_img)
            else:
                # Резерв: рисуем прямоугольник
                self.chest_canvas.create_rectangle(50, 50, 250, 150, fill="#8B4513", outline="black", width=3)
                self.chest_canvas.create_text(150, 100, text="Сундук", fill="white", font=("Press Start 2P", 12))

        # Кнопка
        tk.Button(
            self.chest_window,
            text="Закрыть",
            font=("Press Start 2P", 8),
            bg="#5E8C31",
            fg="white",
            command=self.close_chest
        ).pack(pady=10)

        self.chest_window.bind("<Return>", lambda e: self.close_chest())
        self.chest_window.bind("<Escape>", lambda e: self.close_chest())
        self.chest_window.withdraw()

    #скрывать окно сундука.
    def close_chest(self):
        if self.chest_window and self.chest_window.winfo_exists():
            self.chest_window.withdraw()

    def update_prompt(self):
        """Обновляет текущее слово из сессии"""
        # Защита от двойного вызова
        if not hasattr(self, 'canvas') or not self.canvas.winfo_exists():
            return

        self.canvas.delete("all")  # fallback
        self.canvas.delete(*self.canvas.find_all())  # принудительная очистка

        # Получаем текущее целевое слово из сессии
        target = self.session.get_current_target()
        if not target:
            self.show_final_report()
            return

        # Обновляем текущее слово
        self.current_word = target

        # НЕ СБРАСЫВАЕМ current_index и user_input!
        # Они должны сохранять своё значение для текущего слова

        # Обновляем scrollregion
        total_width = len(self.current_word) * 26 + 40
        self.canvas.config(scrollregion=(0, 0, total_width, 100))

        # Обновляем отображение
        self.update_display()

        # CAPS LOCK
        caps_on = self.check_caps_lock()
        if caps_on:
            self.status_label.config(text="⚠️ CAPS LOCK ВКЛ", fg="red", bg="yellow")
        else:
            self.status_label.config(text="")

            
    def show_final_report(self):
        stats = self.session.get_final_stats()
        msg = (
            f"Урок закончен!\n"
            f"{stats['time_sec']} c | {stats['words']} слов\n"
            f"Точность: {stats['accuracy']}% | WPM: {stats['wpm']}\n"
            f"\nНажмите Enter, чтобы продолжить."
        )
        self.canvas.delete("all")
        self.canvas.create_text(400, 30, text=msg, fill=FG_COLOR, font=("Press Start 2P", 14), justify="center")
        self.stats_var.set(f"Точность: {stats['accuracy']}% | WPM: {stats['wpm']}")

    def on_key_release(self, event=None):
        # ЗАМЕНИТЕ НА:
        if event and event.keysym in ("Return", "BackSpace", "Shift_L", "Shift_R"):
            return

        # Обновляем подсветку
        self.update_display()

        # CAPS LOCK
        caps_on = self.check_caps_lock()
        if caps_on:
            self.status_label.config(text="⚠️ CAPS LOCK ВКЛ", fg="red", bg="yellow")
        else:
            self.status_label.config(text="")


    def on_key_press(self, event):
        if self.is_training_ended:
            return "break"

        if not event.char or not event.char.isprintable():
            return "break"

        if self.current_index < len(self.current_word) and event.char == self.current_word[self.current_index]:
            self.current_index += 1
            self.user_input += event.char
            self.update_display()

            if self.current_index == len(self.current_word):
                self.is_training_ended = True
                self.submit_current()

        return "break"


    def update_highlighting(self, typed: str):
        # Удаляем ВСЕ дочерние элементы canvas напрямую через tags
        for item in self.canvas.find_all():
            self.canvas.delete(item)

        target = self.current_word
        block_w, block_h = 24, 24
        x0_start = 20
        typed = typed[:len(target)]

        for i, char in enumerate(target):
            if i < len(typed):
                color = CORRECT_COLOR if typed[i] == char else ERROR_COLOR
            elif i == len(typed):
                color = CURRENT_BG
            else:
                color = "#8B7D6B"

            x0 = x0_start + i * (block_w + 2)
            y0 = 10
            x1, y1 = x0 + block_w, y0 + block_h

            self.canvas.create_rectangle(x0, y0, x1, y1,
                                         fill=color, outline="#2E231C", width=2)
            self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2,
                                    text=char, fill="white",
                                    font=("Press Start 2P", 14, "bold"))

    def submit_current(self, event=None):
        if not self.user_input:
            return

        self.session.start_timer()

        result = self.session.submit(self.user_input)

        # Обработка завершения ВСЕГО УРОКА
        if result.get("done"):
            save_session_to_csv(self.session)
            next_level = get_next_level(self.session.track, self.session.level_key)
            if next_level:
                # Переход на следующий уровень
                self.session.level_key = next_level
                self.session.exercises = get_lesson(self.session.track, next_level)
                self.session.index = 0
                self.session.accuracy = []
                self.session.speed_history = []
                self.session.time_start = time.time()

                # Удаляем старые сообщения с галочкой
                for widget in self.root.winfo_children():
                    try:
                        if hasattr(widget, 'cget') and 'text' in widget.keys() and widget.cget('text').startswith('✅'):
                            widget.destroy()
                    except (tk.TclError, AttributeError):
                        pass

                # Показываем сообщение о завершении уровня
                self.message_label = tk.Label(
                    self.root,
                    text="✅ Уровень пройден!\nНажмите Enter, чтобы продолжить",
                    font=("Press Start 2P", 14, "bold"),
                    fg="lime",
                    bg=BG_COLOR,
                    relief="raised",
                    bd=3
                )
                self.message_label.place(relx=0.5, rely=0.5, anchor="center")

                # Привязываем Enter к загрузке следующего уровня
                self.root.bind("<Return>", lambda e: self.load_next_level())

                # Автоудаление через 5 секунд
                self.root.after(5000, self.auto_destroy_message)

                return  # ВЫХОДИМ, не вызывая update_prompt
            else:
                self.show_final_report()
                return  # ВЫХОДИМ

        # --- Если урок НЕ завершён ---
        accuracy = result.get("accuracy", 0)

        # Алмазы и звуки
        if accuracy >= 90.0:
            praise = "🔥 Алмаз добыт! Идеально!"
            self.diamonds += 1
            self.diamonds_label.config(text=f"Алмазов: {self.diamonds}")
            self.play_sound("победа")
        elif accuracy >= 80.0:
            praise = "🟩 Хорошо. Можно быстрее!"
            self.play_sound("закрытие_программы")
        else:
            praise = "🟥 Повторение — мать учения!"
            self.play_sound("ошибка_при_наборе")

        self.stats_var.set(f"Точность: {accuracy:.1f}% | {praise}")

        # Сброс ввода и переход к следующему слову
        self.root.after(300, self.update_prompt)
        # Сброс позиции для нового упражнения
        self.canvas.xview_moveto(0)
        self.user_input = ""
        self.current_index = 0
        self.is_training_ended = False

    def auto_destroy_message(self):
        """Автоматически удаляет сообщение и восстанавливает обработку Enter"""
        if hasattr(self, 'message_label') and self.message_label.winfo_exists():
            self.message_label.destroy()
            # Восстанавливаем стандартную обработку Enter
            self.root.unbind("<Return>")
            self.root.bind("<Return>", lambda e: self.submit_current())

    def load_next_level(self, event=None):
        """Загружает следующий уровень после завершения текущего"""

        # Удаляем сообщение, если оно ещё есть
        if hasattr(self, 'message_label') and self.message_label.winfo_exists():
            self.message_label.destroy()

        # Получаем следующий уровень
        next_level_key = get_next_level(self.session.track, self.session.level_key)

        if next_level_key:
            # Создаём новую сессию для следующего уровня
            self.session = TypingSession(
                self.session.track,
                next_level_key,
                self.session.language
            )
            # Сбрасываем счётчики
            self.current_exercise_index = 0
            self.user_input = ""
            self.current_index = 0
            self.is_training_ended = False

            # Восстанавливаем стандартную обработку Enter
            self.root.unbind("<Return>")
            self.root.bind("<Return>", lambda e: self.submit_current())

            # Обновляем отображение
            self.update_prompt()

            # Показываем сообщение о загрузке нового уровня
            self.show_minecraft_message(f"📚 Уровень {next_level_key}", "#7CFC00")

        else:
            # Конец трека — показываем сообщение
            self.show_final_report()

    def resize_background(self, event=None):
        # Не обрабатываем, если окно ещё не видимо
        if not self.root.winfo_viewable():
            return

        w = self.root.winfo_width()
        h = self.root.winfo_height()
        if w <= 1 or h <= 1:  # минимальный размер для фона
            return

        bg_name = "history" if hasattr(self, 'message_label') and self.message_label.winfo_viewable() else "training"
        bg_path = os.path.join(PROJECT_ROOT, "textures", "background", f"{bg_name}.png")

        try:
            if not os.path.isfile(bg_path):
                print(f"[ФОН] Файл не найден: {bg_path}")
                self.bg_canvas.configure(bg=BG_COLOR)
                return

            # Загружаем изображение
            img = Image.open(bg_path).resize((w, h), Image.NEAREST)
            # Масштабируем ТОЛЬКО если размеры корректны
            if w > 0 and h > 0:
                img = img.resize((w, h), Image.NEAREST)

            # Сохраняем ссылку в атрибуте — критично!чтобы GC не удалил
            self.bg_photo = ImageTk.PhotoImage(img)

            # Удаляем старое изображение
            self.bg_canvas.delete("all")
            self.bg_canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)

        except Exception as e:
            print(f"[ФОН] Ошибка: {e}")
            self.bg_canvas.configure(bg=BG_COLOR)

    def check_caps_lock(self):
        try:
            out = subprocess.check_output(['xset', 'q']).decode()
            return 'Caps Lock:   on' in out
        except:
            return False

    def load_background(self):
        """Загружает фон ПОСЛЕ того, как окно отобразилось."""
        if not self.root.winfo_exists():
            return

        bg_name = "training"
        bg_path = os.path.join("textures", "background", f"{bg_name}.png")

        try:
            if os.path.isfile(bg_path):
                img = Image.open(bg_path)
                w, h = self.root.winfo_width(), self.root.winfo_height()
                if w <= 1 or h <= 1:
                    # Если размеры ещё не готовы — подождём
                    # self.root.after(100, self.load_background)  #Удали всё, что связано с on_window_resize, draw_background_resized, after(100, ...) — они только мешают.
                    return
                img = img.resize((w, h), Image.NEAREST)
                # КРИТИЧНО: сохраняем ссылку, чтобы GC не удалил
                self.bg_photo = ImageTk.PhotoImage(img)
                self.bg_canvas.delete("all")
                self.bg_canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
            else:
                self.bg_canvas.configure(bg=BG_COLOR)
        except Exception as e:
            print(f"[ФОН] Ошибка загрузки {bg_path}: {e}")
            self.bg_canvas.configure(bg=BG_COLOR)

    def init_background(self):
        """Инициализирует фон один раз, когда окно готово."""
        if not self.root.winfo_exists():
            return

        bg_path = os.path.join("textures", "background", "training.png")
        try:
            if os.path.isfile(bg_path):
                img = Image.open(bg_path)
                w, h = self.root.winfo_width(), self.root.winfo_height()
                if w < 100 or h < 100:
                    # Если размеры ещё не готовы — подождём
                    self.root.after(200, self.init_background)
                    return

                img = img.resize((w, h), Image.NEAREST)
                # 🔑 КЛЮЧЕВОЙ ШАГ: сохраняем ссылку в атрибуте класса
                self.bg_photo = ImageTk.PhotoImage(img)  # ← Это must be kept!

                self.bg_canvas.delete("all")
                self.bg_canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
            else:
                self.bg_canvas.configure(bg=BG_COLOR)
        except Exception as e:
            print(f"[ФОН] Ошибка: {e}")
            self.bg_canvas.configure(bg=BG_COLOR)

    def on_window_click(self, event):
        """Снимает фокус с entry при клике по окну (не по entry)."""
        # Если клик не по entry — снимаем фокус

        self.root.focus_set()  # переносим фокус на root

    def on_resize(self, event):
        w, h = event.width, event.height
        if w < 100 or h < 100:
            return

        bg_path = os.path.join(os.path.dirname(__file__), "textures", "background", "training.png")
        if not os.path.isfile(bg_path):
            return

        try:
            img = Image.open(bg_path)
            # Ключ: масштабируем ТОЛЬКО если размер изображения ≠ размер окна
            if img.size != (w, h):
                img = img.resize((w, h), Image.NEAREST)
            photo = ImageTk.PhotoImage(img)

            # Удаляем старое
            if self.bg_image_id:
                self.bg_canvas.delete(self.bg_image_id)

            # Создаём новое
            self.bg_image_id = self.bg_canvas.create_image(0, 0, anchor="nw", image=photo)
            self._bg_photo = photo  # ← сохраняем ссылку

        except Exception as e:
            print(f"[ФОН] Ошибка: {e}")

    def on_backspace(self, event):
        if self.current_index > 0 and not self.is_training_ended:
            self.current_index -= 1
            self.user_input = self.user_input[:-1]  # ← ДОБАВЬТЕ ЭТУ СТРОКУ
            self.update_display()
        return "break"

    def update_display(self):
        # Очищаем Canvas
        self.canvas.delete("all")

        current_text = self.current_word
        if not current_text:
            return

        # Получаем ширину канваса
        self.canvas.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        if canvas_width <= 1:
            canvas_width = 800

        # Фиксированная позиция курсора (чуть левее центра)
        CURSOR_FIXED_X = canvas_width // 2 - 50

        # Вычисляем смещение текста
        current_char_center = 20 + self.current_index * 26 + 12
        offset = CURSOR_FIXED_X - current_char_center

        # Определяем цвета в зависимости от режима
        if self.devops_mode:
            # Terminal режим
            colors = {
                'correct': '#00FF00',      # зелёный
                'current': '#FFFF00',       # жёлтый
                'future': '#008000',         # тёмно-зелёный
                'border': '#00FF00',
                'text': '#00FF00'
            }
        else:
            # Minecraft режим
            colors = {
                'correct': '#7CFC00',       # зелёный травы
                'current': '#FFD700',        # золотой
                'future': '#808080',          # серый камень
                'border': '#2E231C',
                'text': 'white'
            }

        # Рисуем символы
        for i, char in enumerate(current_text):
            if i < self.current_index:
                color = colors['correct']
            elif i == self.current_index:
                color = colors['current']
            else:
                color = colors['future']

            x = 20 + i * 26 + offset

            # Рисуем только если символ виден (с запасом)
            if -50 < x < canvas_width + 50:
                # Основной прямоугольник
                self.canvas.create_rectangle(x, 10, x+24, 34,
                                             fill=color, outline=colors['border'], width=2)

                # Для текущего символа добавляем дополнительную обводку (чёрную в Minecraft, яркую в Terminal)
                if i == self.current_index:
                    if self.devops_mode:
                        # Жёлтая обводка в терминале
                        self.canvas.create_rectangle(x-1, 9, x+25, 35,
                                                     outline='#FFFF00', width=2, fill='')
                    else:
                        # Чёрная обводка в Minecraft
                        self.canvas.create_rectangle(x, 10, x+24, 34,
                                                     outline='black', width=2, fill='')

                # Текст с тенью (Minecraft стиль)
                if not self.devops_mode:
                    # Тень
                    self.canvas.create_text(x+13, 23, text=char,
                                            fill='#3F3F3F', font=("Press Start 2P", 14))
                # Основной текст
                self.canvas.create_text(x+12, 22, text=char,
                                        fill=colors['text'], font=("Press Start 2P", 14))

        # Опционально: нарисовать маркер позиции курсора (можно убрать)
        # self.canvas.create_line(CURSOR_FIXED_X, 5, CURSOR_FIXED_X, 40, fill='red', width=1)
