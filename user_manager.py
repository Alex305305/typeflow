import json
import os
from datetime import datetime


class UserManager:
    def __init__(self, users_dir="users"):
        self.users_dir = users_dir
        if not os.path.exists(users_dir):
            os.makedirs(users_dir)

    def get_all_users(self):
        """Возвращает список всех пользователей"""
        users = []
        for file in os.listdir(self.users_dir):
            if file.endswith('.json'):
                users.append(file[:-5])
        return users

    def create_user(self, username):
        """Создаёт нового пользователя"""
        user_data = {
            "username": username,
            "created_at": datetime.now().isoformat(),
            "track": "beginner",  # beginner или advanced
            "level_key": "1_base_position",
            "language": "ru",
            "history": []  # история тренировок
        }
        self._save_user(username, user_data)
        return user_data

    def load_user(self, username):
        """Загружает данные пользователя"""
        filepath = os.path.join(self.users_dir, f"{username}.json")
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        return None

    def save_user(self, username, user_data):
        """Сохраняет данные пользователя"""
        self._save_user(username, user_data)

    def update_progress(self, username, track, level_key, language, accuracy=None, wpm=None):
        """Обновляет прогресс пользователя"""
        user_data = self.load_user(username)
        if user_data:
            user_data["track"] = track
            user_data["level_key"] = level_key
            user_data["language"] = language

            # Добавляем запись в историю
            if accuracy is not None and wpm is not None:
                user_data["history"].append({
                    "date": datetime.now().isoformat(),
                    "level": level_key,
                    "accuracy": accuracy,
                    "wpm": wpm
                })

            self._save_user(username, user_data)

    def _save_user(self, username, user_data):
        """Внутренний метод сохранения"""
        filepath = os.path.join(self.users_dir, f"{username}.json")
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, ensure_ascii=False, indent=2)