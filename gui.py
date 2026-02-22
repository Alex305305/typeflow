# gui.py

import subprocess
import os
import tkinter as tk
import time
from config import BG_COLOR, FG_COLOR, FONT_FAMILY, FONT_SIZE_INPUT, FONT_SIZE_PROMPT, CORRECT_COLOR, ERROR_COLOR, CURRENT_BG
from core import TypingSession, save_session_to_csv
from PIL import Image, ImageTk
import config
from lessons import get_next_level, get_lesson
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
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0, font=("Press Start 2P", 8))
        menu.add_cascade(label="Файл", menu=file_menu, font=("Press Start 2P", 8))
        file_menu.add_command(label="Перезапустить", command=self.restart, font=("Press Start 2P", 8))
        file_menu.add_command(label="Выход", command=self.root.quit, font=("Press Start 2P", 8))

        stats_menu = tk.Menu(menu, tearoff=0, font=("Press Start 2P", 8))
        menu.add_cascade(label="Статистика", menu=stats_menu, font=("Press Start 2P", 8))
        stats_menu.add_command(label="История", command=self.show_history, font=("Press Start 2P", 8))

        self.root.title("Тренажер слепой печати")
        self.root.geometry("800x600")
        self.root.configure(bg=BG_COLOR)
        self.root.bind("<Escape>", lambda _: self.root.quit())


        # Поле ввода
        self.canvas = tk.Canvas(
            self.root,
            bg=BG_COLOR,
            height=60,
            highlightthickness=0
        )
        self.canvas.pack(pady=20, padx=40, fill="x")
        self.canvas.focus_set()  # Фокус на Canvas

        # Привязываем нажатия клавиш
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<BackSpace>", self.on_backspace)


        # Статистика
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
        # Алмазы — ТОЛЬКО ОДИН РАЗ!
        self.diamonds_label = tk.Label(
            self.root,
            text="Алмазов: 0",
            font=("Press Start 2P", 12),
            bg=BG_COLOR,
            fg="#4CC9F0"
        )
        self.diamonds_label.place(relx=0.98, rely=0.02, anchor="ne")

        self.root.bind("<Return>", lambda e: self.submit_current())


        # Первое слово
        self.update_prompt()

        self.root.after(500, lambda: self.play_sound("переход_на_другой_уровень"))


    def on_enter(self):
        # ЗАМЕНИТЕ НА:
        print(f"[DEBUG] on_enter: user_input = '{self.user_input}'")
        if self.user_input:
            self.submit_current()
        else:
            print("[DEBUG] on_enter: input пустой — игнорируем")

    def show_history(self):
        import tkinter.messagebox as msg
        try:
            with open("typing_history.csv", "r", encoding="utf-8") as f:
                lines = f.readlines()
            if len(lines) <= 1:
                msg.showinfo("История", "История пуста.")
            else:
                msg.showinfo("История", "".join(lines[-6:]))
        except FileNotFoundError:
            msg.showinfo("История", "Файл не найден. Пройдите урок.")    # ТУТ НАДО ПОДУМАТЬ МЕНЯТЬ ЛИ!

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
                self.chest_canvas.create_text(150, 100, text="Сундук", fill="white", font=("Arial", 12))

        # Алмазы — правый верхний угол
        self.chest_diamond_label = tk.Label(
            self.chest_window,
            text=f"Алмазов: {self.diamonds}",
            font=("Press Start 2P", 10),
            fg="#4CC9F0",
            bg="#392C23"
        )
        self.chest_diamond_label.place(relx=0.98, rely=0.02, anchor="ne")

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
        # Защита от двойного вызова
        if not hasattr(self, 'canvas') or not self.canvas.winfo_exists():
            return
        self.canvas.delete("all")  # fallback
        self.canvas.delete(*self.canvas.find_all())  # принудительная очистка
        target = self.session.get_current_target()
        if not target:
            self.show_final_report()
            return

        print(f"[DEBUG] Текущее упражнение: {target} (len={len(target)})")

        self.current_word = target

        # Сброс атрибутов (ТОЛЬКО ОДИН РАЗ!)
        self.current_index = 0
        self.user_input = ""  # ← СТРОКА, НЕ StringVar! УДАЛИТЕ .set()
        self.is_training_ended = False

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
        print("[DEBUG] submit_current вызван!")
        print(f"[DEBUG] user_input = '{self.user_input}'")

        if not self.user_input:
            print("[DEBUG] user_input пустой — выход")
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

                # Показываем сообщение
                for widget in self.root.winfo_children():
                    if hasattr(widget, 'cget') and widget.cget('text').startswith('✅'):
                        widget.destroy()
                self.message_label = tk.Label(
                    self.root,
                    text="✅ Уровень пройден!\nНажмите Enter, чтобы продолжить",
                    font=("Press Start 2P", 14, "bold"),
                    fg="lime",
                    bg=BG_COLOR
                )
                self.message_label.pack(pady=10)
                self.root.bind("<Return>", lambda e: self.load_next_level())
                return  # ← ВАЖНО: выходим, не вызывая update_prompt!
            else:
                self.show_final_report()
                return  # ← ВАЖНО: выходим

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
        print(f"[DEBUG] index={self.session.index}, exercises_len={len(self.session.exercises)}, done={result.get('done')}")

    def load_next_level(self, event=None):
        # Удаляем сообщение
        if hasattr(self, 'message_label'):
            self.message_label.destroy()

        # Получаем СЛЕДУЮЩИЙ уровень через функцию из lessons.py
        next_level_key = get_next_level(self.session.track, self.session.level_key)

        if next_level_key:
            # Создаём НОВУЮ сессию для следующего уровня
            self.session = TypingSession(self.session.track, next_level_key, self.session.language)
            self.current_exercise_index = 0
            self.update_prompt()
            self.root.unbind("<Return>")  # Убираем привязку
        else:
            # Конец трека — показываем сообщение
            self.show_completion_message()

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

        # Получаем текущее упражнение
        current_text = self.current_word
        if not current_text:
            return

        # ФИКСИРОВАННАЯ ПОЗИЦИЯ КУРСОРА (центр экрана)
        self.canvas.update_idletasks()
        canvas_width = self.canvas.winfo_width()
        if canvas_width <= 1:
            canvas_width = 800

        # Позиция курсора - чуть левее центра, чтобы было место для новых символов
        CURSOR_FIXED_X = canvas_width // 2 - 50  # Например, 350px при ширине 800

        # Вычисляем смещение для ВСЕГО текста
        # Хотим, чтобы текущий символ был в позиции CURSOR_FIXED_X
        current_char_center = 20 + self.current_index * 26 + 12
        offset = CURSOR_FIXED_X - current_char_center

        for i, char in enumerate(current_text):
            # Определяем цвет
            if i < self.current_index:
                color = CORRECT_COLOR
            elif i == self.current_index:
                color = CURRENT_BG
            else:
                color = "#8B7D6B"

            x = 20 + i * 26 + offset

            if -50 < x < canvas_width + 50:
                # Рисуем основной блок
                self.canvas.create_rectangle(x, 10, x + 24, 34, fill=color)

                # Черная обводка ТОЛЬКО для текущего символа
                if i == self.current_index:
                    self.canvas.create_rectangle(x, 10, x + 24, 34, outline="black", width=2, fill="")

                # Текст
                self.canvas.create_text(x + 12, 22, text=char, fill="white", font=("Press Start 2P", 14))