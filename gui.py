# gui.py

import tkinter as tk  # стандартная GUI-библиотека Python (не требует установки).
from tkinter import font as tkfont  # чтобы настраивать шрифты динамически
from config import BG_COLOR, FG_COLOR, FONT_FAMILY, FONT_SIZE_INPUT, FONT_SIZE_PROMPT   #  выносим цвета/шрифты в отдельный файл → легко менять тему.
from core import TypingSession, save_session_to_csv   # логика уроков, подсчёта точности, повторов — отделена от интерфейса.


class TypingGUI:
# root — главное окно (создаётся в main.py).
# self.session — изолированная сессия тренировки: знает, какие слова идти, сколько раз повторять.
    def __init__(self, root: tk.Tk, track: str, level_key: str):
        self.root = root
        self.session = TypingSession(track, level_key)  #  передаём два параметра
        self.setup_ui()  # сборка интерфейса, базовые настройки окна


    def setup_ui(self):
        # Настройка окна
        self.root.title("Тренажер слепой печати")
        self.root.geometry("800x600")
        self.root.configure(bg=BG_COLOR)
        self.root.bind("<Escape>", lambda _: self.root.quit())  #bind("<Escape>") — удобно выйти без мыши.

        # шрифты
        mono_font = tkfont.Font(family=FONT_FAMILY, size=FONT_SIZE_INPUT)
        prompt_font = tkfont.Font(family=FONT_FAMILY, size=FONT_SIZE_PROMPT, weight="bold")
        # JetBrains Mono — хороший моноширинный шрифт (установлен на большинстве dev-систем); если нет — Tkinter подставит Courier как fallback.

        # Промпт  # (слово/фраза для ввода) — Text вместо Entry
        self.text_widget = tk.Text(  #  StringVar — привязка данных: при изменении переменной → автоматически обновляется надпись.
            self.root,
            height = 1,
            width = 40,
            bg = "#2d2d2d",
            fg = FG_COLOR,
            insertbackground = FG_COLOR,
            font = mono_font,
            relief = "flat",
            state = "disabled",   # только для чтения
            wrap = "word",
            padx = 20,
            pady = 10,
        )
        self.text_widget.pack(pady = 20, padx = 40, fill = "x")
        # Подсветка
        self.text_widget.tag_configure("correct", foreground = "#4caf50")   # зеленый
        self.text_widget.tag_configure("wrong",foreground = "#ff6b6b")   #  красный
        self.text_widget.tag_configure("current", background = "#3a3a3a")  #  серый фон текущего символа

        # Поле ввода — Entry (для ввода, но не для подсветки)
        self.input_var = tk.StringVar()
        self.entry = tk.Entry(
            self.root,
            textvariable=self.input_var,
            font=mono_font,
            bg="#2d2d2d",
            fg=FG_COLOR,
            insertbackground = FG_COLOR,
            relief="flat",
            justify="center"
        )
        self.entry.pack(pady=10, ipady=10, padx=40, fill="x")
        self.entry.focus_set()    # фокус на поле ввода при старте

        #  отслеживаем каждый ввод!
        self.entry.bind("<KeyRelease>", self.on_key_release)

        # Статистика
        self.stats_var = tk.StringVar(value="Точность: — | WPM: —")
        stats_label = tk.Label(
            self.root,
            textvariable=self.stats_var,
            bg=BG_COLOR,
            fg="#a0a0a0",
            font=("Arial", 14,"bold")
        )
        stats_label.pack(pady=15)

        # Обработка Enter — отправка ответа
        self.root.bind("<Return>", self.submit_current)

        # Показываем первое слово
        self.update_prompt()


    def update_prompt(self):
        target = self.session.get_current_target()
        if target:
            self.current_word = target
            self.text_widget.config(state = "normal")
            self.text_widget.delete(1.0, tk.END)
            self.text_widget.insert(tk.END, target)
            self.text_widget.config(state = "disabled")
            self.input_var.set("")
            self.update_highlighting("")   # сброс подсветки
        else:
            self.show_final_report()
            #
            #
            #
            # self.text_widget.config(state = "disabled")  # блокируем ввод
            # self.entry.config(state = "disabled")
    def show_final_report(self):
        stats = self.session.get_final_stats()
        self.text_widget.config(state = "normal")
        self.text_widget.delete(1.0, tk.END)
        self.text_widget.insert(
                tk.END,
          f"Урок закончен!\n"
                f"{stats['time_sec']} c | {stats['words']} слов \n"              
                f"Точность: {stats['accuracy']}% | WPM: {stats['wpm']}"
                )
        self.text_widget.config(state = "disabled")
        self.entry.config(state = "disabled")
        self.stats_var.set(f"Точность: {stats['accuracy']}% | WPM: {stats['wpm']}")

    def on_key_release(self, even=None):
        # Игнорируем служебные клавиши: Backspace, Enter, Shift и т.д.
        if even and even.keysym in ("Return", "BackSpace", "Shift_L", "Shift_R", "Control_L", "Control_R"):
            return
        user_text = self.input_var.get()
        self.update_highlighting(user_text)

    def update_highlighting(self, typed: str):
        """Обновляет подсветку в text_widget на основе введённого текста"""
        target = self.current_word
        self.text_widget.tag_remove("currect","1.0",tk.END)
        self.text_widget.tag_remove("wrong", "1.0", tk.END)
        self.text_widget.tag_remove("current", "1.0", tk.END)

        # Подсветка введённых символов
        for i, (t_char, u_char) in enumerate(zip(target, typed)):
            tag = "correct" if t_char == u_char else "wrong"
            self.text_widget.tag_add(tag, f"1.{i}", f"1.{i+1}")

        # Подсветка текущей позиции (следующий символ)
        pos = len(typed)
        if pos < len(target):
            self.text_widget.tag_add("current", f"1.{pos}", f"1.{pos+1}")

    def submit_current(self, event = None):
        user_input = self.input_var.get().strip()   # убираем пробелы в начале/конце
        if not user_input:
            return

        result = self.session.submit(user_input)

        # Обновить статистку (заглушка: wpm пока не считаем без времени)
        accuracy = result.get("accuracy", 0)
        repeat_msg = "Повтор" if result.get("repeat") else ""
        self.stats_var.set(f"Точность: {accuracy:.1f}% | {repeat_msg}")

        self.input_var.set("")   # Очищаем поле ввода
        self.update_prompt()      # Обновляем промпт (следующее слово или "урок завершён")
        if result.get("done"):   #  сохранение при завершении урока
            from core import save_session_to_csv
            save_session_to_csv(self.session)





























