import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import obtener
from InfoApp import Info

path_flecha = "Media/Flecha derecha.png"


def invertir(producto):
    if producto.capitalize() == producto:
        return producto.replace(" ", "_").lower()
    else:
        return producto.replace("_", " ").capitalize()

class App:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Precios de las comidas")
        self.data = obtener.precios()
        self.producto_seleccionado = ''
        # Lista de opciones
        self.all_options = list(map(invertir, self.data.keys()))
        self.available_options = self.all_options.copy()

        ### TÍTULOS
        tk.Label(root, text='Productos disponibles').grid(row=0, column=0)
        tk.Label(root, text='Ingredientes').grid(row=0, column=2)
        self.info_button = tk.Button(root, text='i', font=('Terminal', 12), command=self.show_info)
        self.info_button.grid(row=0, column=3, sticky='w')
        self.info_title = tk.Label(root, text='Info del producto')

        ### LISTBOX PRODUCTOS
        # Disponibles
        self.listbox_available = tk.Listbox(root, height=12, selectmode=tk.SINGLE)
        for option in self.available_options:
            self.listbox_available.insert(tk.END, option)
        self.listbox_available.grid(row=1, column=0, rowspan=3, padx=10, pady=10)
        self.listbox_available.bind("<<ListboxSelect>>", self.update_label)

        # Agregados
        self.listbox_selected = tk.Listbox(root, height=12, selectmode=tk.SINGLE)
        self.listbox_selected.grid(row=1, column=2, rowspan=3, padx=10, pady=10)
        self.listbox_selected.bind("<<ListboxSelect>>", self.update_label)

        ### MANEJO PRODUCTOS
        # Botones -> y <-
        imagen = Image.open("Media/Flecha derecha.png").resize((30, 30))
        self.flecha_der = ImageTk.PhotoImage(imagen)
        self.flecha_izq = ImageTk.PhotoImage(imagen.rotate(180))
        self.agregar_button = tk.Button(root, text="-->", command=self.add_to_list, image=self.flecha_der)
        self.agregar_button.grid(row=1, column=1, padx=10)
        self.quitar_button = tk.Button(root, text="<--", command=self.remove_from_list, image=self.flecha_izq)
        self.quitar_button.grid(row=3, column=1, padx=10)
        # Input cantidad y unidad
        self.cantidad_frame = tk.Frame(root)
        self.cantidad_frame.grid(row=2, column=1)
        vcmd = (root.register(self.validate_entry), '%P')   # Verifica que se ingresen solo números
        self.cantidad_input = tk.Entry(self.cantidad_frame, width=5, validate='all', validatecommand=vcmd)
        self.cantidad_input.grid(row=1, column=0)
        self.cantidad_tipo = ttk.Combobox(self.cantidad_frame, values = ['g', 'ml', 'un'], width=4, state='readonly')
        self.cantidad_tipo.grid(row=1, column=1)

        ### INFO PRODUCTO
        self.info_frame = tk.Frame(root, height=200, borderwidth=1, relief='solid')
        # self.info_frame.pack_propagate(False) 
        self.info = Info(self.info_frame, invertir(option))


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

    def validate_entry(self, P: str):
        return P == "" or P.replace('.','',1).isdigit()

        
    def update_label(self, event: tk.Event):
        widget: tk.Widget = event.widget
        selected = widget.curselection()
        if selected:
            option = widget.get(selected)
            if option != self.producto_seleccionado:
                self.producto_seleccionado = option
                self.info.actualizar(invertir(option))

    def show_info(self):
        self.info_title.grid(row=0, column=3)
        self.info_frame.grid(row=1, column=3, rowspan=3, padx=3, pady=3)
        self.info_button['command'] = self.hide_info

    def hide_info(self):
        self.info_title.grid_forget()
        self.info_frame.grid_forget()
        self.info_button['command'] = self.show_info

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
