# main.py

# Точка входа: начальный экран выбора языка и уровня

import tkinter as tk
from tkinter import font as tkfont
from config import BG_COLOR, FG_COLOR, ACCENT_COLOR, set_language
from gui import TypingGUI

class StartScreen:
    """
    Начальный экран программы.
    Позволяет выбирать:
    - язык (русский/английский),
    -уровень(новичок/продвинутый)
    После выбора запускает тренажёр.
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self.selected_language = "ru"
        self.selected_level = "beginner"
        self.setup_ui()

    def setup_ui(self):
        # Настройка окна
        self.root.title("Тренажёр слепой печати")
        self.root.geometry("700x500")
        self.root.configure(bg = BG_COLOR)

        # Шрифты
        title_font = tkfont.Font(family = "Arial", size = 20, weight = "bold")
        label_font = tkfont.Font(family = "Arial", size = 14)
        button_font = tkfont.Font(family = "Arial", size = 12, weight = "bold")

        # Заголовок
        tk.Label(
            self.root, text = "Приветствую тебя ученик",
            bg = BG_COLOR, fg = FG_COLOR, font = title_font
        ).pack(pady = 20)

        # Выбор языка
        tk.Label(
            self.root, text = "Выберите язык интерфйса и уроков:",
            bg = BG_COLOR, fg = FG_COLOR, font = label_font
        ).pack(pady = 15)

        lang_frame = tk.Frame(self.root, bg = BG_COLOR)
        lang_frame.pack()

        ru_btn = tk.Button(
            lang_frame, text = "Русский",
            command = lambda: self.select_language("ru"),
            font = button_font, bg = ACCENT_COLOR, fg = "white", width = 15, height = 2)
        en_btn = tk.Button(
            lang_frame, text = "English",
            command = lambda: self.select_language("en"),
            font = button_font, bg = "#5a5a5a", fg = "white", width = 15, height = 2)
        ru_btn.pack(side = "left", padx = 10)
        ru_btn.pack(side = "left", padx = 10)

        # Выбор уровня
        tk.Label(
            self.root, text = "Выберете Ваш уровень:",
            bg = BG_COLOR, fg = FG_COLOR, font = label_font
        ).pack(pady = 25)

        self.track_var = tk.StringVar(value = "beginner")
        beginner_rb = tk.Radiobutton(
            self.root, text = "Новичок(с нуля: позиция пальцев - слова",
            variable = self.track_var, value = "beginner",
            bg = BG_COLOR, fg = FG_COLOR, font = ("Arial", 12), anchor = "w"
        )
        advanced_rb = tk.Radiobutton(
            self.root, text = "Продвинутый(уже печатаю, хочу скорость",
            variable = self.track_var, value = "advanced",
            bg = BG_COLOR, fg = FG_COLOR, font = ("Arial",12), anchor = "w"
        )
        beginner_rb.pack(pady = 5, padx = 50, anchor = "w")
        advanced_rb.pack(pady = 5, padx = 50, anchor = "w")

        # Кнопака старта
        start_bnt = tk.Button(
            self.root, text = "Начать обучение",
            command = self.start_training,
            font = button_font, bg = "#4caf50", fg = "white",
            width = 25, height = 2
        )
        start_bnt.pack(pady = 30)

        #Подсказка
        tk.Label(
            self.root,
            text = "После выбора нажмите Enter для отправки слова.\nТочность < 80% - слово повториться.",
            bg = BG_COLOR, fg = "#a0a0a0", font = ("Arial", 10)
        ).pack(pady = 10)
    def select_language(self, lang: str):
        """Меняем выбранный язык и обновляем кнопки(визуальная обратная связь)"""
        self.selected_language = lang
        set_language(lang)  # глобальная смена языка

        # Обновляем стиль кнопок (активная — яркая, неактивная — тусклая)
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for btn in widget.winfo_children():
                    if isinstance(btn, tk.Button):
                        if "Русский" in btn["text"] and lang == "ru":
                            btn.config(bg = ACCENT_COLOR)
                        elif "English" in btn["text"] and lang == "en":
                            btn.config(bg = ACCENT_COLOR)
                        else:
                            btn.config(bg = "#5a5a5a")

    def start_training(self):
        """Запускаем тренажёр с выбранными настройками"""
        self.root.destroy()  # закрываем стартовый экран

        # Создаем новое окно
        new_root = tk.Tk()
        track = self.track_var.get()

        #Определяем первый уровень в зависимости от трека
        if track == "beginner":
            level_key = "1_fingers"  # начинаем с поозиции пальцев
        else:
            level_key = "1_drills"  # продвинутые - с дриллов

        # Запускаем GUI
        app = TypingGUI(new_root, track, level_key)
        new_root.mainloop()

# Точка выхода
if __name__ == "__main__":
    root = tk.Tk()
    StartScreen(root)
    root.mainloop()

        #Что делает этот код:
        #Показывает красивый стартовый экран.
        #При клике на язык — вызывает set_language() → все уроки становятся на выбранном языке.
        #При старте — автоматически выбирает первый уровень (1_fingers или 1_drills).
        #Можно легко расширить: добавить выбор уровня вручную (через Combobox), но пока — авто.




