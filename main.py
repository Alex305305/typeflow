# main.py

import tkinter as tk
from tkinter import font as tkfont
from config import BG_COLOR, FG_COLOR, ACCENT_COLOR, set_language
from gui import TypingGUI
from PIL import Image, ImageTk
from lessons import get_lesson, get_next_level
from user_manager import UserManager  # импортируем менеджер пользователей


class StartScreen:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.selected_language = "ru"
        self.selected_level = "beginner"
        self.user_manager = UserManager()          # создаём менеджер
        self.username = None                       # будет выбран позже
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Тренажёр слепой печати")
        self.root.geometry("700x600")               # увеличил высоту для поля пользователя
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

        title_font = tkfont.Font(family="Press Start 2P", size=14, weight="bold")
        label_font = tkfont.Font(family="Press Start 2P", size=14)
        button_font = tkfont.Font(family="Press Start 2P", size=12, weight="bold")

        tk.Label(
            self.root, text="Да прибудет с тобой Сила ученик",
            bg=BG_COLOR, fg=FG_COLOR, font=title_font
        ).pack(pady=20)

        # --- Выбор языка ---
        tk.Label(
            self.root, text="Выберите язык интерфейса и уроков:",
            bg=BG_COLOR, fg=FG_COLOR, font=label_font
        ).pack(pady=15)

        lang_frame = tk.Frame(self.root, bg=BG_COLOR)
        lang_frame.pack()

        ru_btn = tk.Button(
            lang_frame, text="Славянский",
            command=lambda: self.select_language("ru"),
            font=button_font, bg=ACCENT_COLOR if self.selected_language == "ru" else "#5a5a5a",
            fg="white", width=15, height=2)
        en_btn = tk.Button(
            lang_frame, text="Буржуйский",
            command=lambda: self.select_language("en"),
            font=button_font, bg=ACCENT_COLOR if self.selected_language == "en" else "#5a5a5a",
            fg="white", width=15, height=2)
        ru_btn.pack(side="left", padx=10)
        en_btn.pack(side="left", padx=10)

        # --- Выбор уровня ---
        tk.Label(
            self.root, text="Выберите Ваш уровень:",
            bg=BG_COLOR, fg=FG_COLOR, font=label_font
        ).pack(pady=25)

        self.track_var = tk.StringVar(value="beginner")
        beginner_rb = tk.Radiobutton(
            self.root, text="Junior (Тренирую скилл)",
            variable=self.track_var, value="beginner",
            bg=BG_COLOR, fg=FG_COLOR,
            selectcolor=ACCENT_COLOR,
            indicatoron=1,
            font=("Press Start 2P", 10), anchor="w"
        )
        advanced_rb = tk.Radiobutton(
            self.root, text="Senior (Варюсь в этом)",
            variable=self.track_var, value="advanced",
            bg=BG_COLOR, fg=FG_COLOR,
            selectcolor=ACCENT_COLOR,
            indicatoron=1,
            font=("Press Start 2P", 10), anchor="w"
        )
        beginner_rb.pack(pady=5, padx=50, anchor="w")
        advanced_rb.pack(pady=5, padx=50, anchor="w")

        # --- Выбор пользователя (встроенный) ---
        self.setup_user_selection()

        # --- Кнопка старта ---
        start_btn = tk.Button(
            self.root,
            text="Поехали",
            command=self.start_training,
            font=button_font,
            bg="#4caf50",
            fg="white",
            width=25,
            height=2
        )
        start_btn.pack(pady=20)

        tk.Label(
            self.root,
            text="После выбора нажмите Enter для отправки слова.\nТочность < 80% - слово повторится.",
            bg=BG_COLOR, fg="#a0a0a0", font=("Press Start 2P", 10)
        ).pack(pady=10)

    def setup_user_selection(self):
        """Создаёт фрейм для выбора пользователя"""
        user_frame = tk.LabelFrame(
            self.root,
            text="👤 Пользователь",
            font=("Press Start 2P", 10),
            bg='#3C2A1E',
            fg='white',
            relief='raised',
            bd=2
        )
        user_frame.pack(pady=15, padx=40, fill="x")

        # Список существующих пользователей
        users = self.user_manager.get_all_users()

        if users:
            tk.Label(
                user_frame,
                text="Выберите существующего:",
                bg='#3C2A1E',
                fg='white',
                font=("Press Start 2P", 8)
            ).pack(pady=(10, 5))

            self.user_listbox = tk.Listbox(
                user_frame,
                height=min(5, len(users)),
                font=("Press Start 2P", 8),
                bg='#4C4C4C',
                fg='white',
                selectbackground='#7CFC00',
                selectforeground='black'
            )
            for user in users:
                self.user_listbox.insert(tk.END, user)
            self.user_listbox.pack(pady=5, padx=20, fill="x")
        else:
            self.user_listbox = None

        # Поле для нового пользователя
        tk.Label(
            user_frame,
            text="Или создайте нового:",
            bg='#3C2A1E',
            fg='white',
            font=("Press Start 2P", 8)
        ).pack(pady=(10, 5))

        self.new_user_entry = tk.Entry(
            user_frame,
            font=("Press Start 2P", 10),
            bg='white',
            fg='black',
            insertbackground='black'
        )
        self.new_user_entry.pack(pady=5, padx=20, fill="x")
        self.new_user_entry.bind("<Return>", lambda e: self.start_training())

    def select_language(self, lang: str):
        self.selected_language = lang
        set_language(lang)
        # Обновляем цвета кнопок
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame):
                for btn in widget.winfo_children():
                    if isinstance(btn, tk.Button):
                        if btn["text"] == "Славянский":
                            btn.config(bg=ACCENT_COLOR if lang == "ru" else "#5a5a5a")
                        elif btn["text"] == "Буржуйский":
                            btn.config(bg=ACCENT_COLOR if lang == "en" else "#5a5a5a")

    def start_training(self):
        # Определяем пользователя
        username = None
        if self.user_listbox and self.user_listbox.curselection():
            username = self.user_listbox.get(self.user_listbox.curselection()[0])
        elif self.new_user_entry.get().strip():
            username = self.new_user_entry.get().strip()
            self.user_manager.create_user(username)
        else:
            # Если ничего не выбрано, показываем сообщение
            import tkinter.messagebox as mb
            mb.showwarning("Внимание", "Выберите или создайте пользователя!")
            return

        # Загружаем данные пользователя (если есть)
        user_data = self.user_manager.load_user(username)
        track = self.track_var.get()
        level_key = "1_base_position" if track == "beginner" else "1_bash_scripts"
        language = self.selected_language

        # Если у пользователя уже есть прогресс, используем его
        if user_data and user_data.get("level_key"):
            track = user_data.get("track", track)
            level_key = user_data.get("level_key", level_key)
            language = user_data.get("language", language)

        # Скрываем все виджеты стартового экрана
        for widget in self.root.winfo_children():
            widget.pack_forget()
            widget.place_forget()

        # Запускаем тренажёр в том же окне, передаём имя пользователя
        self.typing_app = TypingGUI(self.root, track, level_key, language, username)


if __name__ == "__main__":
    root = tk.Tk()
    StartScreen(root)
    root.mainloop()