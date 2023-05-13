import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.minsize(width=200, height=200)
window.maxsize(width=400, height=400)
window.title("Пример простой программы на ткинтер")


def example_f_for_escape(w):
    print(w)
    print("ESCAPE нажат")
    window.quit()


window.bind("<Escape>", example_f_for_escape)

print(window.configure())


def example_f_for_button_press():
    print("Кнопка была нажата")
    print(lbl["text"])
    lbl["text"] = "Новый текст"
    # lbl.configure(text="Новый текст")


btn = ttk.Button(master=window, text="Кнопка", command=example_f_for_button_press)
btn.pack(padx=10, pady=10)

lbl = ttk.Label(master=window, text="Текст")
lbl.pack(padx=10, pady=10)

window.mainloop()

print("end of program")
