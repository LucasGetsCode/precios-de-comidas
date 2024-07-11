import tkinter as tk
from tkinter import ttk

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Labels con Botones de Borrado")

        # Lista de ejemplo
        self.lista = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]

        # Crear un frame para contener los labels
        self.main_frame = ttk.Frame(self.root, padding=10)
        self.main_frame.pack()

        # Crear los labels y botones dinámicamente
        self.labels = []
        for index, item in enumerate(self.lista):
            label = ttk.Label(self.main_frame, text=item)
            label.grid(row=index, column=0, sticky="w", padx=10, pady=5)

            # Botón para borrar
            delete_button = ttk.Button(self.main_frame, text="Borrar", command=lambda i=index: self.borrar_label(i))
            delete_button.grid(row=index, column=1, padx=10, pady=5)

            # Guardar referencia al label y botón
            self.labels.append((label, delete_button))

    def borrar_label(self, index):
        # Eliminar label y botón del frame y de la lista
        self.labels[index][0].grid_forget()  # Oculta el label
        self.labels[index][1].grid_forget()  # Oculta el botón
        del self.labels[index]  # Elimina la referencia de la lista de labels

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
