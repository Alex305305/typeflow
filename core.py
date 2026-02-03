# core.py
# Логика тренировки: выбор урока, подсчёт точности, WPM, экспорт

import time
import csv
import os
from datetime import datetime
from lessons import get_lesson

# Файл для сохранения истории
HISTORY_FILE = "typing_history.csv"


class TypingSession:
    """Класс, управляющий одной сессией тренировки."""

    def __init__(self, track: str, level_key: str, language: str):
        self.track = track
        self.level_key = level_key
        self.language = language
        try:
            exercises = get_lesson(track, level_key, language)
            if not exercises:
                raise ValueError(f"Уровень {track}/{level_key} пуст")
            self.exercises = exercises
        except Exception as e:
            print(f"[ОШИБКА] Не удалось загрузить урок: {e}")
            self.exercises = ["ф", "ы", "в", "а"] if language == "ru" else ["f", "j", "d", "k"]

        self.index = 0
        self.accuracy = []
        self.speed_history = []
        self.time_start = time.time()

        # Для расчёта статистики
        self.total_correct_chars = 0
        self.total_words = 0
        self.total_accuracy = 0.0
        self.repetition_count = {}  # счётчик повторов для каждого слова

    def get_current_target(self) -> str:
        if self.index < len(self.exercises):
            return self.exercises[self.index]
        return ""

    def start_timer(self):
        # Таймер уже запущен в __init__, но оставим для совместимости
        pass

    def get_elapsed_minutes(self) -> float:
        elapsed = time.time() - self.time_start
        return max(0.001, elapsed / 60.0)

    def submit(self, user_input: str) -> dict:
        target = self.get_current_target()
        if not target:
            return {"done": True, "accuracy": 100.0}

        # Подсчёт точности
        min_len = min(len(user_input), len(target))
        correct_chars = sum(1 for i in range(min_len) if user_input[i] == target[i])
        accuracy = round(100 * correct_chars / max(len(target), 1), 1)

        # Обновляем статистику
        self.total_correct_chars += correct_chars
        self.total_words += 1
        self.total_accuracy += accuracy

        # 🚫 Убираем динамическое добавление слов — фиксированный урок
        # Повтор только если <80% и ещё не последнее слово
        repeat_flag = False
        if accuracy < 80.0 and self.index < len(self.exercises) - 1:
            repeat_flag = True
        else:
            self.index += 1  # только здесь увеличиваем index
        done = self.index >= len(self.exercises)
        wpm = round((self.total_correct_chars / 5) / self.get_elapsed_minutes(), 1)

        return {
            "target": target,
            "typed": user_input,
            "accuracy": accuracy,
            "wpm": wpm,
            "repeat": repeat_flag,
            "done": done
        }

    def get_final_stats(self) -> dict:
        avg_accuracy = round(self.total_accuracy / self.total_words, 1) if self.total_words > 0 else 0.0
        final_wpm = round((self.total_correct_chars / 5) / self.get_elapsed_minutes(), 1)
        time_sec = round(time.time() - self.time_start, 1)
        return {
            "words": self.total_words,
            "accuracy": avg_accuracy,
            "wpm": final_wpm,
            "time_sec": time_sec
        }


def save_session_to_csv(session: TypingSession):
    """Сохраняет результаты сессии в CSV-файл."""
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

    file_exists = os.path.isfile(HISTORY_FILE)
    with open(HISTORY_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=record.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(record)