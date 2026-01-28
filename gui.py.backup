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


class TypingGUI:
    def __init__(self, root: tk.Tk, track: str, level_key: str, language: str):
        self.root = root
        self.language = language
        self.track = track
        self.level_key = level_key
        self.session = TypingSession(track, level_key, language)
        self.diamonds = 0

        # Обязательно: создаём ВСЕ атрибуты ДО setup_ui() Фон сразу
        self.bg_canvas = tk.Canvas(self.root, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        self.status_label = tk.Label(
            self.root,
            text="",
            font=("Press Start 2P", 10),
            bg=BG_COLOR,
            fg="white"
        )
        self.status_label.pack(side="bottom", pady=2)

        self.setup_ui()

        self.entry.bind("<Return>", lambda e: self.submit_current()) # or self.root.bind("<Configure>", self.resize_background)
        self.chest_window = None
        self.create_chest_window()

        # Запуск живой статистики
        # self.root.after(100, self.update_live_stats)

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

        # Canvas для слова
        self.canvas = tk.Canvas(
            self.root,
            bg=BG_COLOR,
            height=60,
            highlightthickness=0
        )
        self.canvas.pack(pady=20, padx=40, fill="x")

        # Поле ввода
        self.entry = tk.Entry(
            self.root,
            font=("Press Start 2P", 16),
            bg="#2d2d2d",
            fg="#F0F0F0",
            insertbackground="#F0F0F0",
            relief="flat",
            justify="center",
            highlightthickness=0
        )
        self.entry.pack(pady=10, ipady=10, padx=40, fill="x")
        self.root.after(300, self.entry.focus_set)
        self.entry.bind("<KeyRelease>", self.on_key_release)

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
        self.diamond_label = tk.Label(
            self.root,
            text="Алмазов: 0",
            font=("Press Start 2P", 12),
            bg=BG_COLOR,
            fg="#4CC9F0"
        )
        self.diamond_label.place(relx=0.98, rely=0.02, anchor="ne")

        # Enter — отправка
        self.entry.bind("<Return>", lambda e: self.on_enter())

        # Первое слово
        self.update_prompt()

        self.root.after(500, lambda: self.play_sound("переход_на_другой_уровень"))


    def on_enter(self):
        # Принудительно обновляем StringVar перед чтением
        self.root.update_idletasks()  # ← КЛЮЧЕВО: синхронизируем GUI
        user_input = self.entry.get().strip()
        print(f"[DEBUG] on_enter: user_input = '{user_input}'")
        if user_input:
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
        target = self.session.get_current_target()
        if not target:
            self.show_final_report()
            return

        print(f"[DEBUG] Текущее упражнение: {target} (len={len(target)})") # ← ВЫВОД В КОНСОЛЬ
        self.root.after(100, self.entry.focus_set)
        self.current_word = target
        self.entry.delete(0, tk.END)
        self.update_highlighting("")

        self.entry.focus_set()

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
        self.entry.config(state="disabled")
        self.stats_var.set(f"Точность: {stats['accuracy']}% | WPM: {stats['wpm']}")

    def on_key_release(self, event=None):
        if event and event.keysym in ("Return", "BackSpace", "Shift_L", "Shift_R", "Control_L", "Control_R"):
            return

        typed = self.entry.get()
        target_len = len(self.current_word)

        # Обрезаем, но ВСЕГДА обновляем подсветку
        if len(typed) > target_len:
            self.entry.delete(target_len, tk.END)

        # Обновляем подсветку ДО проверки на отправку
        self.update_highlighting(typed)

        # Если ввод полный — отправляем через after
        if len(typed) == target_len:
            self.root.after(50, self.submit_current)

        # CAPS LOCK
        caps_on = self.check_caps_lock()
        if caps_on:
            self.status_label.config(text="⚠️ CAPS LOCK ВКЛ", fg="red", bg="yellow")
        else:
            self.status_label.config(text="")

    def update_highlighting(self, typed: str):
        self.canvas.delete("all")
        target = self.current_word
        block_w, block_h = 24, 24
        x0_start = 20

        # Обрезаем typed до длины target, чтобы избежать IndexError
        typed = typed[:len(target)]

        for i, char in enumerate(target):
            if i < len(typed):
                if typed[i] == char:
                    color = CORRECT_COLOR  # зелёный
                else:
                    color = ERROR_COLOR  # красный
            elif i == len(typed):
                color = CURRENT_BG  # текущая позиция (серый/тёмный)
            else:
                color = "#8B7D6B"  # не введено (древесина)

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
        user_input = self.entry.get().strip()
        print(f"[DEBUG] user_input = '{user_input}'")
        if not user_input:
            print("[DEBUG] user_input пустой — выход")
            return

        self.session.start_timer()
        user_input = self.entry.get()
        if not user_input:
            return

        result = self.session.submit(user_input)

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
            self.diamond_label.config(text=f"Алмазов: {self.diamonds}")
            self.play_sound("победа")
        elif accuracy >= 80.0:
            praise = "🟩 Хорошо. Можно быстрее!"
            self.play_sound("закрытие_программы")
        else:
            praise = "🟥 Повторение — мать учения!"
            self.play_sound("ошибка_при_наборе")

        self.stats_var.set(f"Точность: {accuracy:.1f}% | {praise}")

        # Сброс ввода и переход к следующему слову
        self.entry.delete(0, tk.END)
        self.root.after(300, self.update_prompt)

    def load_next_level(self, event=None):
        # Удаляем сообщение
        if hasattr(self, 'message_label'):
            self.message_label.destroy()
        self.root.unbind("<Return>")
        self.root.bind("<Return>", self.submit_current)
        self.update_prompt()

    def resize_background(self, event=None):
        # Временно отключено для стабильности
        self.bg_canvas.configure(bg=BG_COLOR)
        return

    def check_caps_lock(self):
        try:
            out = subprocess.check_output(['xset', 'q']).decode()
            return 'Caps Lock:   on' in out
        except:
            return False

    # def update_live_stats(self):
    #     if not hasattr(self, 'root') or not self.root.winfo_exists():
    #         return
    #     if not hasattr(self, 'session') or not self.session.time_start:
    #         self.root.after(500, self.update_live_stats)
    #         return
    #
    #     elapsed = time.time() - self.session.time_start
    #     if elapsed > 0:
    #         cpm = len(self.input_var.get()) / (elapsed / 60)
    #         wpm = cpm / 5
    #         color = "green" if wpm > 20 else "red"
    #         self.stats_label.config(
    #             text=f"WPM: {wpm:.0f} | CPM: {cpm:.0f}",
    #             fg=color,
    #             font=("Press Start 2P", 14, "bold")
    #         )
    #     # Только если окно ещё живо
    #     if self.root.winfo_exists():
    #         self.root.after(500, self.update_live_stats)