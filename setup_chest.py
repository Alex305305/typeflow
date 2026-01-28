# setup_chest.py
import os
from PIL import Image

# Путь к текстурам
TEXTURES_DIR = "textures"
os.makedirs(TEXTURES_DIR, exist_ok=True)

# Картинка сундука (вставьте вашу картинку в папку textures/)
# Пример: textures/chest_closed.png

# Если у вас нет chest_open.png — скопируем closed
if not os.path.exists(f"{TEXTURES_DIR}/chest_open.png"):
    if os.path.exists(f"{TEXTURES_DIR}/chest_closed.png"):
        from shutil import copyfile
        copyfile(f"{TEXTURES_DIR}/chest_closed.png", f"{TEXTURES_DIR}/chest_open.png")
        print("✅ chest_open.png создан как копия chest_closed.png")
    else:
        print("⚠️ Нет файла textures/chest_closed.png — загрузите его вручную")

print("✨ Готово! Теперь запустите main.py")