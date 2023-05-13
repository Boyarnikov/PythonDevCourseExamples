import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import random

window = ttk.Window(themename='simplex')
window.minsize(width=500, height=500)
window.maxsize(width=700, height=700)
window.title("Сапёр")


class Board:
    size = 10
    mines = list()
    grid = list()

    @staticmethod
    def generate(size, amount=10):
        possible_mines = [(i, j) for j in range(size) for i in range(size)]
        Board.grid = [[0 for j in range(size)] for i in range(size)]
        Board.mines = random.choices(possible_mines, k=amount)
        for y in range(size):
            for x in range(size):
                for i in range(max(0, y - 1), min(y + 2, size)):
                    for j in range(max(0, x - 1), min(x + 2, size)):
                        Board.grid[y][x] += (i, j) in Board.mines


def p(x, y):
    return lambda: print(x, y)


def print_position(x, y):
    _x = x
    _y = y

    def f():
        print(_x, _y)

    return f


def hide_button(btn: ttk.Button, x, y):
    _btn = btn
    _x = x
    _y = y

    def f():
        print(x, y)
        btn.grid_forget()

    return f


buttons = list()
labels = list()


def create_board(size):
    global buttons, labels
    for i in buttons:
        for j in i:
            j.destroy()
    for i in labels:
        for j in i:
            j.destroy()

    Board.generate(size)

    buttons = list()
    labels = list()
    print(buttons)

    for i in range(size):
        fr.columnconfigure(i, weight=1)
        fr.rowconfigure(i, weight=1)

    for y in range(size):
        buttons.append([])
        labels.append([])
        for x in range(size):
            labels[y].append(ttk.Label(master=fr, text=Board.grid[y][x]))
            labels[y][x].grid(row=x, column=y, padx=11, pady=5)

            buttons[y].append(tk.Button(master=fr, width=3, height=1, text=""))
            buttons[y][x]["command"] = hide_button(buttons[y][x], x, y)
            buttons[y][x].grid(row=x, column=y)

    print(buttons)
    print(buttons[0][0]["command"] is buttons[0][1]["command"])


board_size = tk.IntVar()

scale_board_size = tk.Scale(master=window, orient="horizontal", variable=board_size, from_=10, to=20)
scale_board_size.pack()

button = ttk.Button(master=window, command=lambda: create_board(scale_board_size.get()), text="Создать поле")
button.pack()

fr = ttk.Frame(master=window, width=20, height=200)

fr.pack()

window.mainloop()

print("end of program")
