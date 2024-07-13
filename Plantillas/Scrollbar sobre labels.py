from tkinter import *
import tkinter as tk

# https://stackoverflow.com/questions/71677889/create-a-scrollbar-to-a-full-window-tkinter-in-python

win = Tk()
win.geometry("500x500")

# main frame con tamaño fijo
main_frame = Frame(win, width=300, height=100)
main_frame.pack(padx=10, pady=10)

# canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# scrollbar
my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)

# Crear el segundo frame dentro del canvas
second_frame = Frame(my_canvas)

# Añadir el segundo frame al canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

# Añadir contenido al segundo frame
for i in range(100):
    tk.Label(second_frame, text=str(i)).pack()

# Actualizar la región del scroll del canvas
second_frame.update_idletasks()
my_canvas.config(scrollregion=my_canvas.bbox("all"))

win.mainloop()
