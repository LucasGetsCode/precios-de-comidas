import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import obtener_precios

path_flecha = "Media/Flecha derecha.png"

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI con Listbox")
        self.data = obtener_precios.obtener_precios()

        # Lista de opciones
        self.all_options = list(map(lambda x: x.capitalize().replace("_", " "), self.data.keys()))
        self.available_options = self.all_options.copy()

        # Listbox para mostrar opciones disponibles
        self.listbox_available = tk.Listbox(root, selectmode=tk.SINGLE)
        for option in self.available_options:
            self.listbox_available.insert(tk.END, option)
        self.listbox_available.grid(row=0, column=0, rowspan=3, padx=10, pady=10)

        # # Botones de flecha
        # self.up_button = tk.Button(root, text="⬆", command=self.navigate_up_available)
        # self.up_button.grid(row=0, column=1, padx=10)

        # self.down_button = tk.Button(root, text="⬇", command=self.navigate_down_available)
        # self.down_button.grid(row=1, column=1, padx=10)

        # Listbox para mostrar elementos agregados
        self.listbox_selected = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox_selected.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

        # Botón para agregar y quitar de la lista
        imagen = Image.open("Media/Flecha derecha.png").resize((30, 30))
        self.flecha_der = ImageTk.PhotoImage(imagen)
        self.flecha_izq = ImageTk.PhotoImage(imagen.rotate(180))
        self.agregar_button = tk.Button(root, text="-->", command=self.add_to_list, image=self.flecha_der)
        self.agregar_button.grid(row=0, column=1, padx=10)
        self.quitar_button = tk.Button(root, text="<--", command=self.remove_from_list, image=self.flecha_izq)
        self.quitar_button.grid(row=2, column=1, padx=10)


        # Manejo de la cantidad
        self.cantidad_frame = tk.Frame(root)
        self.cantidad_frame.grid(row=1, column=1)

        vcmd = (root.register(self.validate_entry), '%P')   # Verifica que se ingresen solo números
        self.cantidad_input = tk.Entry(self.cantidad_frame, width=5, validate='all', validatecommand=vcmd)
        self.cantidad_input.grid(row=0, column=0)
        # self.cantidad_input.trace_add('write', self.validate_entry) # Verifica que se ingrese un número

        self.cantidad_tipo = ttk.Combobox(self.cantidad_frame, values = ['g', 'mg', 'ml'], width=3)
        self.cantidad_tipo.grid(row=0, column=1)

        # Botón para mostrar información
        self.info_button = tk.Button(root, text="Info", command=self.show_info)
        self.info_button.grid(row=1, column=3, padx=10)

    def add_to_list(self):
        selection = self.listbox_available.curselection()
        if selection and self.cantidad_input.get() != '' and self.cantidad_tipo.get() != '':
            index = selection[0]
            option = self.listbox_available.get(index)
            # Remover opción seleccionada de la Listbox de disponibles
            self.listbox_available.delete(index)
            self.available_options.remove(option)
            # Agregar opción a la Listbox de seleccionados
            self.listbox_selected.insert(tk.END, option)
            self.cantidad_input
            self.cantidad_input.delete(0, tk.END)


    def remove_from_list(self):
        selection = self.listbox_selected.curselection()
        if selection:
            index = selection[0]
            option = self.listbox_selected.get(index)
            # Remover opción seleccionada de la Listbox de seleccionados
            self.listbox_selected.delete(index)
            # Agregar opción de vuelta a la Listbox de disponibles
            self.available_options.append(option)
            self.available_options.sort()  # Ordenar opciones
            self.listbox_available.delete(0, tk.END)
            for option in self.available_options:
                self.listbox_available.insert(tk.END, option)

    def show_info(self):
        selection = self.listbox_selected.curselection()
        if selection:
            index = selection[0]
            option = self.listbox_selected.get(index)
            messagebox.showinfo("Información", f"Esta es la información de {option}")

    def navigate_up_available(self):
        current_selection = self.listbox_available.curselection()
        if current_selection:
            index = current_selection[0]
            if index > 0:
                self.listbox_available.select_clear(index)
                self.listbox_available.select_set(index - 1)
                self.listbox_available.see(index - 1)

    def navigate_down_available(self):
        current_selection = self.listbox_available.curselection()
        if current_selection:
            index = current_selection[0]
            if index < self.listbox_available.size() - 1:
                self.listbox_available.select_clear(index)
                self.listbox_available.select_set(index + 1)
                self.listbox_available.see(index + 1)

    def validate_entry(self, P):
        return P == "" or P.replace('.','',1).isdigit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
