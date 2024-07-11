import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Editable Label")

        # Crear el frame
        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(padx=10, pady=10)

        # Label inicial
        self.label_text = tk.StringVar(value="Texto inicial")
        self.label = ttk.Label(self.frame, textvariable=self.label_text)
        self.label.grid(row=0, column=0, padx=5, pady=5)
        # self.label.bind("<Button-1>", self.edit_label)

        self.label_button = ttk.Button(self.frame, command=self.edit_label, text="🖉")
        self.label_button.grid(row=0, column=1)

        # Entry para editar el label (inicialmente oculto)
        self.entry_text = tk.StringVar()
        self.entry = ttk.Entry(self.frame, textvariable=self.entry_text)
        self.entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        self.entry.grid_remove()

        # Botones de confirmación y cancelación (inicialmente ocultos)
        self.confirm_button = ttk.Button(self.frame, text="✓", command=self.confirm_edit)
        self.confirm_button.grid(row=0, column=1, padx=5, pady=5)
        self.confirm_button.grid_remove()

        self.cancel_button = ttk.Button(self.frame, text="❌", command=self.cancel_edit)
        self.cancel_button.grid(row=0, column=2, padx=5, pady=5)
        self.cancel_button.grid_remove()

    def edit_label(self):
        # Mostrar el Entry y los botones, ocultar el Label
        self.label.grid_remove()
        self.label_button.grid_remove()
        self.entry_text.set(self.label_text.get())
        self.entry.grid()
        self.confirm_button.grid()
        self.cancel_button.grid()
        self.entry.focus()

    def confirm_edit(self):
        # Confirmar la edición y mostrar el Label actualizado
        if self.entry_text.get().strip() != '':
            self.label_text.set(self.entry_text.get().strip())
            self.entry.grid_remove()
            self.confirm_button.grid_remove()
            self.cancel_button.grid_remove()
            self.label.grid()
            self.label_button.grid()

    def cancel_edit(self):
        # Cancelar la edición y restaurar el Label original
        self.entry.grid_remove()
        self.confirm_button.grid_remove()
        self.cancel_button.grid_remove()
        self.label.grid()
        self.label_button.grid()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
