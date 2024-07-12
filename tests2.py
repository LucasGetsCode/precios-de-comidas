import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Crear una StringVar para el texto del label
label_text = tk.StringVar()

# Valores iniciales
variable1 = 10
variable2 = 20

# Función para actualizar el texto del label
def update_label():
    global variable1, variable2
    fixed_text = "El resultado es:"
    label_text.set(f"{fixed_text} {variable1} y {variable2}")

# Crear el label y asignarle la StringVar
label = tk.Label(root, textvariable=label_text)
label.pack()

# Botón para cambiar los valores y actualizar el label
def change_values():
    global variable1, variable2
    variable1 += 1
    variable2 += 2
    update_label()

button = tk.Button(root, text="Cambiar valores", command=change_values)
button.pack()

# Inicializar el texto del label
update_label()

# Ejecutar el bucle principal de la aplicación
root.mainloop()
