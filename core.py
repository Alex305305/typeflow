# core.py
# Логика тренировки: выбор урока, подсчёт точности, WPM, экспорт
import time
import  csv
import os
from datetime import datetime
from lessons import get_lesson

# Файл для сохранения истории
HISTORY_FILE = "typing_history.csv"

class TypingSession:
    """Класс, управляющий одной сессией тренировки.
    Отвечает за:
    - текущее слово/фразу,
    - подсчёт точности и скорости,
    - автоповтор сложных элементов,
    - сохранение результатов.
    """

    def __init__(self,track: str,level_key: str):
        """
        :param track: "beginner" или "advanced"
        :param level_key: например, "2_home_row"
        """
        self.track = track
        self.level_key = level_key
        # Получаем упражнения на текущем языке
        self.exercises = get_lesson(track,level_key)[:]
        self.index = 0
        self.start_time = None
        self.total_correct_chars = 0
        self.total_words = 0
        self.total_accuracy = 0.0

    def get_current_target(self)-> str:
        """
        Возвращает текущее упражнение (слово/фразу).
        Если урок закончился — возвращает пустую строку.
        """
        if self.index < len(self.exercises):
            return self.exercises[self.index]
        return ""

    def start_timer(self):
        """
        Запускает таймер при первом вводе.
        Вызывается автоматически в submit().
        """
        if self.start_time is None:
            self.start_time = time.time()

    def get_elapsed_minutes(self)->float:
        """
        Возвращает время сессии в минутах
        (минимум 0.001, чтобы избежать деления на 0).
        """
        if self.start_time is None:
            return 0.0
        return max(0.001,(time.time()-self.start_time)/60.0)

    def submit(self, user_input: str)->dict:
        """
        Обрабатывает введённый пользователем текст.
        :param user_input: то, что напечатал пользователь
        :return: словарь с результатами: точность, wpm,
         нужно ли повторить и т.д.
         """

        self.start_timer()   # запускаем таймер при первом submit

        target = self.get_current_target()
        if not target:
            return {"done": True}

        #  подсчитываем сколько символов введено верно
        correct_chars = sum(
            a == b for a, b in zip(user_input, target)
        )
        # Точность в процентах (округляем до 0,1%)
        accuracy = round(100 * correct_chars / max(len(target), 1), 1)

        # Накапливаем статистику для WPM и итогового отчета
        self.total_correct_chars += correct_chars
        self.total_words += 1
        self.total_accuracy += accuracy

        # Расчет WPM: (количество верных символов / 5) / время в мин
        # (стандарт: одно слово = 5 символов)
        wpm = round((self.total_correct_chars / 5) / self.get_elapsed_minutes(), 1)

        # Автоповтор при <80% и слово не повторялось 3 раза
        repeat_flag = False
        if accuracy < 80.0 and self.exercises.count(target) < 3:
            self.exercises.append(target)
            repeat_flag = True

        # переход к следующему упражнению
        self.index += 1

        return {
            "target": target,
            "typed": user_input,
            "accuracy": accuracy,
            "wpm": wpm,
            "repeat": repeat_flag,
            "done": self.index >= len(self.exercises)
        }

    def get_final_stats(self) -> dict:
        """
        Возвращает итоговую статистику по окончанию урока
        """
        avg_accuracy = round(self.total_accuracy / self.total_words, 1) if self.total_words else 0.0
        final_wpm = round((self.total_correct_chars / 5) / self.get_elapsed_minutes(), 1)
        return {
            "words": self.total_words,
            "accuracy": avg_accuracy,
            "wpm": final_wpm,
            "time_sec": round((time.time() - self.start_time), 1) if self.start_time else 0.0
        }

def save_session_to_csv(session: TypingSession):
    """
    Сохраняет результаты сессии в CSV-файл для последующего анализа.
    Формат: дата, трек, уровень, wpm, точность, слов, секунд.
    """
    stats = session.get_final_stats()
    record = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "track": session.track,
        "level": session.level_key,
        "wpm": stats["wpm"],
        "accuracy": stats["accuracy"],
        "words": stats["words"],
        "time_sec": stats["time_sec"]
    }


    # Проверяем, существует ли файл — если нет, создаём с заголовком
    file_exists = os.path.isfile(HISTORY_FILE)
    with open(HISTORY_FILE, "a", newline = "", encoding = "utf-8") as f:
        write = csv.DictWriter(f, fieldnames = record.keys())
        if not file_exists:
            write.writeheader()    # записываем заголовки: date,track,level,...
        write.writerow(record)

            #Теперь TypingSession принимает track и level_key, а не просто lesson_key.
            #save_session_to_csv() — отдельная функция, её вызовем в gui.py.







