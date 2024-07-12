import tkinter as tk
from tkinter import ttk
import obtener


def invertir(producto: str) -> str:
    if producto.capitalize() == producto:
        return producto.replace(" ", "_").lower()
    else:
        return producto.replace("_", " ").capitalize()

class Info(tk.Tk):
    # unidades = {'g': (1000, 'kg'), 'ml': (1000, 'l'), 'un': (12, 'doc')}
    def __init__(self, root: tk.Tk, producto: str):
        self.root = root
        self.producto = producto
        self.data = obtener.data_producto(producto)
        self.url_count = 0
        self.style = ttk.Style()
        self.style.configure('Oscuro.Label', background='#f0f0f0')
        self.style.configure('Claro.Label',  background='#f8f8f8')
        self.title_var       = tk.StringVar(value=invertir(producto))
        self.unidad_var      = tk.StringVar(value=self.data['unidad'])
        self.precio_pcn_var  = tk.StringVar()
        self.precio_pcn_var.set('800.0')
        self.precio_cant_var = tk.StringVar(value=self.data['precio'])
        self.cantidad_var    = tk.StringVar(value=self.data['porcion'])


        ### Crear el frame principal
        self.info_frame = ttk.Frame(root, padding="10")
        self.info_frame.pack(padx=5, pady=5)

        ### TÍTULO
        self.title_frame = ttk.Frame(self.info_frame)
        self.title_frame.grid(row=0,column=0, sticky='ew', columnspan=3)

        self.title_label = ttk.Label(self.title_frame, textvariable=self.title_var, font=("Helvetica", 16))
        self.title_label.pack(side='left')

        self.title_edit_button = ttk.Button(self.title_frame, command=self.iniciar_edit, text="🖉", width=3)
        self.title_edit_button.pack(side='right')

            # Entry para editar el label (inicialmente oculto)
        self.entry_text = tk.StringVar()
        self.title_entry = ttk.Entry(self.title_frame, textvariable=self.entry_text, font=("Helvetica", 14), width=26)
        self.title_entry.bind("<Return>", lambda e: self.confirmar_edit())
            # Botones de confirmación y cancelación (inicialmente ocultos)
        self.confirm_button = ttk.Button(self.title_frame, text="✓", command=self.confirmar_edit, width=3)
        self.cancel_button = ttk.Button(self.title_frame, text="❌", command=self.cancelar_edit, width=3)
            # Combobox de unidades (inicialmente oculto)
        self.unidades_selector = ttk.Combobox(self.title_frame, textvariable=self.unidad_var, 
                                              values=['g','ml','un'], width=3,state='readonly')


        ### TEXTOS
        self.text_frame_general = ttk.Frame(self.info_frame)
        self.text_frame_general.grid(row=1, column=0, columnspan=3, sticky='ew', pady=10)

            # Precio / cantidad
        self.text1_frame = ttk.Frame(self.text_frame_general)
        self.text1_frame.pack(side='left', expand=True)
        self.text1_label1 = ttk.Label(self.text1_frame, text='$').pack(side='left')
        self.text1_label2 = ttk.Label(self.text1_frame, textvariable=self.precio_cant_var).pack(side='left')
        self.text1_label3 = ttk.Label(self.text1_frame, text='/ 1000').pack(side='left')
        self.text1_label4 = ttk.Label(self.text1_frame, textvariable=self.unidad_var).pack(side='left')

            # Cantidad / porción
        self.text2_frame = ttk.Frame(self.text_frame_general)
        self.text2_frame.pack(side='left', expand=True)
        self.text2_label1 = ttk.Label(self.text2_frame, textvariable=self.cantidad_var)
        self.text2_label1.pack(side='left')
        self.text2_entry1 = ttk.Entry(self.text2_frame, textvariable=self.cantidad_var, width=4)
        self.text2_entry1.bind("<Return>", lambda e: self.confirmar_edit())
        self.text2_label2 = ttk.Label(self.text2_frame, textvariable=self.unidad_var)
        self.text2_label2.pack(side='left')
        self.text2_label3 = ttk.Label(self.text2_frame, text='/ porción').pack(side='left')

            # Precio / porción
        self.text3_frame = ttk.Frame(self.text_frame_general)
        self.text3_frame.pack(side='left', expand=True)
        self.text3_label1 = ttk.Label(self.text3_frame, text='$').pack(side='left')
        self.text3_label2 = ttk.Label(self.text3_frame, textvariable=self.precio_pcn_var).pack(side='left')
        self.text3_label3 = ttk.Label(self.text3_frame, text='/ porción').pack(side='left')

        ### URLs
        self.url_frame = ttk.Frame(self.info_frame)#, borderwidth=1, relief='solid', height=20, width=20)
        self.url_frame.grid(row=2, column=0, columnspan=3, sticky='ew')

        self.urls = self.data['links']
        # self.urls = [("http://example.com/"+str(random.randint(0,100)), i) for i in range(7)]
        for link in self.urls: self.añadir_url(link[0], link[1])

            # Frame para el input
        self.url_entry_frame = ttk.Frame(self.info_frame)#, borderwidth=1, relief='solid', height=20, width=20)
        self.url_entry_frame.grid(row=3, column=0, columnspan=3, pady=(10, 0), sticky='ew')
            # Crear el Entry para la nueva URL
        self.url_entry = ttk.Entry(self.url_entry_frame, width=56)
        self.url_entry.pack(side='left', fill='x', padx=(0,10))
        self.url_entry.bind("<Return>", lambda e: self.add_url())

            # Crear el botón para agregar la nueva URL y número
        self.add_button = ttk.Button(self.url_entry_frame, text="✓", width=3, command=self.add_url)
        self.add_button.pack(side='right', fill='x', padx=(5,0))

            # Crear el Entry para el número
        ttk.Label(self.url_entry_frame, textvariable=self.unidad_var, width=3).pack(side='right', fill='x')
        self.number_entry = ttk.Entry(self.url_entry_frame, width=4)
        self.number_entry.pack(side='right', fill='x')
        self.number_entry.bind("<Return>", lambda e: self.add_url())

            # Crea el botón para mostrar la info de los widgets
        self.print_button = ttk.Button(self.info_frame, text="Print", command=self.print)
        self.print_button.grid(row=4, column=2, pady=10)

    def print(self):
        if self.url_frame.winfo_children() == []: print("No hay urls que mostrar")
        link = []
        for widget in self.url_frame.winfo_children():
            for widget2 in widget.winfo_children():
                if widget2.widgetName == 'ttk::label':
                    if 'http' in widget2['text']:
                        if link != []: print(link)
                        link = [widget2['text']]
                    else:
                        link.append(widget2['text'])
        print(link)
        # self.destroy()
        self.actualizar('cafe')


    ## URLS
    def add_url(self):
        new_url = self.url_entry.get()
        cantidad = self.number_entry.get()
        if 'http' in new_url and cantidad.replace('.','',1).isdigit():
            self.añadir_url(new_url, cantidad)
            self.url_entry.delete(0, tk.END)
            self.number_entry.delete(0, tk.END)

    def añadir_url(self, url: str, cant: float = 1):
        estilo = "Oscuro.Label" if self.url_count % 2 == 0 else "Claro.Label"
        self.url_count += 1
        frame = ttk.Frame(self.url_frame, style=estilo)
        frame.pack(fill='x')
        url_label = ttk.Label(frame, text=url, width=60, style=estilo)
        url_label.pack(fill='x', side='left')
        url_label.bind("<Button-1>", lambda x: root.clipboard_clear() or root.clipboard_append(url))
        eliminar_boton = ttk.Button(frame, command=lambda: self.eliminar_url(frame), text='🗑', width=3)
        eliminar_boton.pack(fill='x', side='right')
        cant_info = ttk.Label(frame, text=cant, style=estilo)
        cant_info.pack(fill='x', side='right', padx=10)

    def eliminar_url(self, widget: ttk.Widget):
        for hijo in widget.winfo_children():
            self.eliminar_url(hijo)
        widget.destroy()
        self.url_count -= 1
        self.refrescar_urls()

    def refrescar_urls(self):
        for index, widget in enumerate(self.url_frame.winfo_children()):
            estilo = "Oscuro.Label" if index % 2 == 0 else "Claro.Label"
            widget.configure(style=estilo)
            for widget2 in widget.winfo_children():
                if widget2.widgetName == 'ttk::label':
                    widget2.configure(style=estilo)

    ### EDITS
    def iniciar_edit(self):
        # Guardo valores previos
        self.unidad_antigua = self.unidad_var.get()
        self.cantidad_antigua = self.cantidad_var.get()
        # Oculto los labels
        self.title_label.pack_forget()
        self.title_edit_button.pack_forget()
        self.text2_label1.pack_forget()
        # Muestro los widgets editables
        self.entry_text.set(self.title_var.get())
        self.title_entry.pack(side='left', padx=10)
        self.confirm_button.pack(side='right')
        self.cancel_button.pack(side='right', padx=5)     
        self.unidades_selector.pack(side='left')  
        self.text2_entry1.pack(side='left', before=self.text2_label2)
        self.title_entry.focus()

    def confirmar_edit(self):
        # Confirmar la edición y mostrar el Label actualizado
        if self.entry_text.get().strip() != '':
            self.title_var.set(self.entry_text.get().strip().capitalize())
            precio = float(self.precio_cant_var.get())
            cant = float(self.cantidad_var.get())
            self.precio_pcn_var.set(round(precio*cant/1000,1))
            self.terminar_edit()

    def cancelar_edit(self):
        # Cancelar la edición y restaurar el Label original
        self.cantidad_var.set(self.cantidad_antigua)
        self.unidad_var.set(self.unidad_antigua)
        self.terminar_edit()

    def terminar_edit(self):
        # Ocutlo widgets editables
        self.title_entry.pack_forget()
        self.confirm_button.pack_forget()
        self.cancel_button.pack_forget()
        self.unidades_selector.pack_forget()
        self.text2_entry1.pack_forget()
        # Muestro labels
        self.title_label.pack(side='left', padx=10)
        self.title_edit_button.pack(side='right')      
        self.text2_label1.pack(side='left', before=self.text2_label2)

    def actualizar(self, producto):
        self.producto = producto
        self.data = obtener.data_producto(producto)
        self.title_var      .set(value=invertir(producto))
        self.unidad_var     .set(self.data['unidad'])
        self.precio_pcn_var .set('800.0')
        self.precio_cant_var.set(self.data['precio'])
        self.cantidad_var   .set(self.data['porcion'])
        self.urls = self.data['links']
        for url in self.url_frame.winfo_children(): self.eliminar_url(url)
        for link in self.urls: self.añadir_url(link[0], link[1])

    def destroy(self):
        print("Destruyendo...")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = Info(root, 'pan_lactal')
    root.mainloop()
