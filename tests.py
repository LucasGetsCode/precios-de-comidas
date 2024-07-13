import tkinter as tk

root = tk.Tk()

# Crear un Label con wraplength
label = tk.Label(root, text="Este es un texto largo que debería ocupar dos líneas en el Label.", wraplength=150)
label.pack(pady=20)

root.mainloop()
