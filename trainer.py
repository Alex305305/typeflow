import sys # управление потоками
import time # замер времени ввода
#import random # выбор случайного слова
import termios # низкоуровневое управление терминалом (ввод без нажатия Enter, raw-режим)
import tty # тоже самое
from lessons import LESSONS
# --- Настройки ---
WORDS = [
    "hello", "world", "python", "linux", "type", "fast", "code", "test",
    "keyboard", "blind", "train", "speed", "accuracy", "enter", "space"
]


def select_lesson():
    print("Выберите урок:")
    lessons_keys = list(LESSONS.keys())  #  сохраняем список
    for i, keys in enumerate(lessons_keys, 1):   #  текущий элемент
        name = keys.replace("_", " ").title()
        print(f"{i}. {name} ({len(LESSONS[keys])} упр.)")
    choice = int(input("\nНомер: ")) - 1
    return lessons_keys[choice]    #   берём по индексу

GREEN = "\033[92m"   # ANSI-коды цветов для подсветки
RED = "\033[91m"
RESET = "\033[0m"    # сброс цвета (обязательно в конце)


def getch():
    """Читает один символ без ожидания Enter и без эха(Linux-only).""" #  сохраняет и восстанавливает терминал
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def train_word(target: str):
    print(f"\n-> {target}") # отображает текущее слово
    print("Набирайте посимвольно (Ctrl+C -- выход):\n")   # отоброжает подсказку

    typed = []   #  список введеных символов (лучше чем строка удобно рор() при Backspace)
    typed_str = ""    # ← защита от UnboundLocalError
    start_time = None    #  время начала ввода старт при первом символе

    i = 0   # индеск ожидаемого смвола в target
    while i < len(target):   # цикл продолжается пока не набрано слово
        ch = getch()

        # Первым символ  -- стартуем таймер
        if start_time is None:
            start_time = time.time()
        # Обработка управляющих клавиш
        if ch == '\x03':  # Ctrl+C мягкий выход из программы
            print("\n\nВыход.")
            sys.exit(0)

        elif ch == '\x7f' or ch == '\b':  # Backspace
            if typed:
                typed.pop()
                i = max(0, i - 1)
        elif ch == '\r' or ch == '\n':  # досрочный выход
            break
        else:
            # Обычный символ
            typed.append(ch)
            sys.stdout.write('\r' + ' ' * 60 + '\r')  # возврат курсора \r — CR (Carriage Return):в начало строки, чтобы перезаписать текущую строку.

            # Формируем строку с подсветкой
            display = ""
            for j in range(len(typed)):
                if j >= len(target):
                    display += RED + typed[j]  # лишние символы - красным
                elif typed[j] == target[j]:
                    display += GREEN + typed[j]
                else:
                    # Ошибка: показываем введённый красным
                    display += RED + typed[j]
            sys.stdout.write(f" -> {display}{RESET}")
            sys.stdout.flush()

            # Переход к следующему символу (даже при ошибке - идём дальше)
            i += 1  # двигаемся к следую символу даже пр ошибке
    end_time = time.time()
    elapsed = end_time - start_time if start_time else 0.01
    typed_str = ''.join(typed)


    # Статистика
    correct = sum(1 for a, b in zip(typed_str, target) if a == b)
    accuracy = round(100 * correct / max(len(target), 1), 1)
    cpm = round((len(typed_str) / elapsed) * 60, 1) if elapsed > 0 else 0

    print(f"\n\n Готово!")
    print(f"Введено: '{typed_str}'")
    print(f"Оригинал: '{target}'")
    print(f"Точность: {accuracy}% | Скорость: {cpm} CPM | Время: {elapsed:.2f} сек")

    if typed_str != target:
        print(f"\n{RED}Подсказка:{RESET} Ожидалось: {target}")    #  (Это как в RapidTyping: вы видите ошибку в процессе, но не портите позицию курсора.)

    return accuracy
def main():
    print("TypeFlow - Тренажёр слепой печати (Linux)")
    print("=" * 45)
    while True:
        lesson_key = select_lesson()
        exercises = LESSONS[lesson_key][:]  # копия списка
        i = 0
        while i < len(exercises):
            word = exercises[i]
            accuracy = train_word(word)

            # Получаем точность из train_word → пока вернём её

            if accuracy < 80.0:   #  Авто-повтор, если точность < 80% и слово ещё не повторялось 3 раза
                current_count = exercises[:i+1].count(word)   #  сколько раз уже было ДО этой позиции
                if current_count < 3:
                    print(f"{RED} - Слово '{word}' добавлено для повторения (точность: {accuracy}%)!{RESET}")
                exercises.append(word)   # добавить в конец очереди
            else:
                print(f"\n {RED} Слово '{word}' уже повторялось 3 раза - пропускаем. {RESET}")

            print("-" * 30)
            i += 1
            # Опция выхода после каждого слова
            if input("Enter — продолжить | q — выход: ").strip().lower() == 'q':
                break
        for word in exercises:
            train_word(word)
        print("\n" + "-" * 30)
        inp = input("Enter - следующее слово | q - выход: ").strip()
        if inp.lower() == 'q':
            break
if __name__ == "__main__":
    main()
