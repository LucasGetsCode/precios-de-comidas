import tkinter as tk

def mostrar_info(event: tk.Event):
    widget = event.widget
    x = widget.winfo_x()
    y = widget.winfo_y()
    info_label.place(x=x, y=y-15)  # Colocar el label de información centrado
    info_label.lift()  # Asegurar que el label de información esté sobre el label principal

def ocultar_info(event):
    info_label.place_forget()  # Ocultar el label de información al salir el mouse

root = tk.Tk()

# Crear el label principal
tk.Label(root, text="Hola").pack(pady=(20,0))
main_label = tk.Label(root, text="Pasa el mouse aquí")
main_label.pack(pady=(0,20), padx=50)

# Crear el label de información (inicialmente oculto)
info_label = tk.Label(root, text="Información adicional", bg='white', relief='solid', borderwidth=1)
info_label.place_forget()  # Ocultar el label inicialmente
main_label.bind("<Enter>", mostrar_info)  # Mostrar al pasar el mouse
main_label.bind("<Leave>", ocultar_info)  # Ocultar al salir el mouse

root.mainloop()
