# main.py

import tkinter as tk
from tkinter import font as tkfont
from config import BG_COLOR, FG_COLOR, ACCENT_COLOR, set_language
from gui import TypingGUI
from PIL import Image, ImageTk


class StartScreen:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.selected_language = "ru"
        self.selected_level = "beginner"
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Тренажёр слепой печати")
        self.root.geometry("700x500")
        self.root.configure(bg=BG_COLOR)

        self.bg_canvas = tk.Canvas(self.root, highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

        def resize_bg(event=None):
            w = self.root.winfo_width()
            h = self.root.winfo_height()
            if w <= 1 or h <= 1:
                return
            try:
                bg_img = Image.open("textures/background/start.png").resize((w, h), Image.NEAREST)
                self.bg_photo = ImageTk.PhotoImage(bg_img)
                self.bg_canvas.delete("all")
                self.bg_canvas.create_image(0, 0, anchor="nw", image=self.bg_photo)
            except Exception as e:
                print("Фон не загружен:", e)
                self.bg_canvas.configure(bg=BG_COLOR)

        self.root.bind("<Configure>", resize_bg)
        resize_bg()

        title_font = tkfont.Font(family="Arial", size=20, weight="bold")
        label_font = tkfont.Font(family="Arial", size=14)
        button_font = tkfont.Font(family="Arial", size=12, weight="bold")

        tk.Label(
            self.root, text="Приветствую тебя ученик",
            bg=BG_COLOR, fg=FG_COLOR, font=title_font
        ).pack(pady=20)

        tk.Label(
            self.root, text="Выберите язык интерфейса и уроков:",
            bg=BG_COLOR, fg=FG_COLOR, font=label_font
        ).pack(pady=15)

        lang_frame = tk.Frame(self.root, bg=BG_COLOR)
        lang_frame.pack()

        ru_btn = tk.Button(
            lang_frame, text="Русский",
            command=lambda: self.select_language("ru"),
            font=button_font, bg=ACCENT_COLOR, fg="white", width=15, height=2)
        en_btn = tk.Button(
            lang_frame, text="English",
            command=lambda: self.select_language("en"),
            font=button_font, bg="#5a5a5a", fg="white", width=15, height=2)
        ru_btn.pack(side="left", padx=10)
        en_btn.pack(side="left", padx=10)

        tk.Label(
            self.root, text="Выберите Ваш уровень:",
            bg=BG_COLOR, fg=FG_COLOR, font=label_font
        ).pack(pady=25)

        self.track_var = tk.StringVar(value="beginner")
        beginner_rb = tk.Radiobutton(
            self.root, text="Новичок (с нуля: позиция пальцев → слова)",
            variable=self.track_var, value="beginner",
            bg=BG_COLOR, fg=FG_COLOR,
            selectcolor=ACCENT_COLOR,
            indicatoron=1,
            font=("Press Start 2P", 10), anchor="w"
        )
        advanced_rb = tk.Radiobutton(
            self.root, text="Продвинутый (уже печатаю, хочу скорость)",
            variable=self.track_var, value="advanced",
            bg=BG_COLOR, fg=FG_COLOR,
            selectcolor=ACCENT_COLOR,
            indicatoron=1,
            font=("Press Start 2P", 10), anchor="w"
        )
        beginner_rb.pack(pady=5, padx=50, anchor="w")
        advanced_rb.pack(pady=5, padx=50, anchor="w")

        start_btn = tk.Button(
            self.root,
            text="Начать обучение",
            command=self.start_training,
            font=button_font,
            bg="#4caf50",
            fg="white",
            width=25,
            height=2
        )
        start_btn.pack(pady=30)

        tk.Label(
            self.root,
            text="После выбора нажмите Enter для отправки слова.\nТочность < 80% - слово повторится.",
            bg=BG_COLOR, fg="#a0a0a0", font=("Arial", 10)
        ).pack(pady=10)

    def select_language(self, lang: str):
        self.selected_language = lang
        set_language(lang)
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for btn in widget.winfo_children():
                    if isinstance(btn, tk.Button):
                        if btn["text"] == "Русский":
                            btn.config(bg=ACCENT_COLOR if lang == "ru" else "#5a5a5a")
                        elif btn["text"] == "English":
                            btn.config(bg=ACCENT_COLOR if lang == "en" else "#5a5a5a")

    def start_training(self):
        self.root.withdraw()  # ← СКРЫВАЕМ, НЕ УНИЧТОЖАЕМ!

        new_root = tk.Tk()
        new_root.geometry(self.root.geometry())
        new_root.attributes("-fullscreen", self.root.attributes("-fullscreen"))

        track = self.track_var.get()
        if track == "beginner":
            level_key = "1_fingers"
        else:
            level_key = "1_drills"

        app = TypingGUI(new_root, track, level_key, self.selected_language)
        new_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    StartScreen(root)
    root.mainloop()