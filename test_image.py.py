from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("300x300")

try:
    img = Image.open("textures/stone.png").resize((300, 300), Image.NEAREST)
    photo = ImageTk.PhotoImage(img)
    canvas = Canvas(root, width=300, height=300)
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.pack()
except Exception as e:
    print("Ошибка загрузки изображения:", e)
    Label(root, text="Изображение не загружено", fg="red").pack()

root.mainloop()