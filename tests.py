import tkinter as tk
from tkinter import ttk
import obtener


def invertir(producto):
    if producto.capitalize() == producto:
        return producto.replace(" ", "_").lower()
    else:
        return producto.replace("_", " ").capitalize()

class Info:
    def __init__(self, root):
        self.root = root
        self.root.title("Frame con Título, Textos, URLs con Scrollbar y Entradas")
        self.url_count = 0
        self.style = ttk.Style()
        self.style.configure('Oscuro.Label', background='#f0f0f0')
        self.style.configure('Claro.Label',  background='#f8f8f8')


        ### Crear el frame principal
        self.info_frame = ttk.Frame(root, padding="10")
        self.info_frame.pack(padx=10, pady=10)

        ### Título
        self.title_frame = ttk.Frame(self.info_frame)
        self.title_frame.grid(row=0,column=0, sticky='ew', columnspan=3)

        self.label_text = tk.StringVar(value="Título")
        self.title_label = ttk.Label(self.title_frame, textvariable=self.label_text, font=("Helvetica", 16))
        self.title_label.pack(side='left', padx=10)

        self.title_edit_button = ttk.Button(self.title_frame, command=self.edit_label, text="🖉", width=3)
        self.title_edit_button.pack(side='left', padx=10)

            # Entry para editar el label (inicialmente oculto)
        self.entry_text = tk.StringVar()
        self.entry = ttk.Entry(self.title_frame, textvariable=self.entry_text, font=("Helvetica", 16))
            # Botones de confirmación y cancelación (inicialmente ocultos)
        self.confirm_button = ttk.Button(self.title_frame, text="✓", command=self.confirm_edit, width=3)
        self.cancel_button = ttk.Button(self.title_frame, text="❌", command=self.cancel_edit, width=3)


        ### Textos
        self.text_label = ttk.Label(self.info_frame)#)
        self.text_label.grid(row=1, column=0, columnspan=3, sticky='ew')

        self.text1 = ttk.Label(self.text_label, text="$50/g")
        self.text1.pack(side='left', expand=True)

        self.text2 = ttk.Label(self.text_label, text="2g/porción")
        self.text2.pack(side='left', expand=True)

        self.text3 = ttk.Label(self.text_label, text="$100/porción")
        self.text3.pack(side='left', expand=True)

        ### URLs
        self.url_frame = ttk.Frame(self.info_frame)#, borderwidth=1, relief='solid', height=20, width=20)
        self.url_frame.grid(row=2, column=0, columnspan=3, pady=(10, 0), sticky='ew')

        # self.urls = list(map(invertir, obtener.precios().keys()))
        self.urls = ["http://example.com/"+str(i) for i in range(7)]
        for i in self.urls: self.añadir_url(i)

        # Frame para el input
        self.url_entry_frame = ttk.Frame(self.info_frame)#, borderwidth=1, relief='solid', height=20, width=20)
        self.url_entry_frame.grid(row=3, column=0, columnspan=3, pady=(10, 0), sticky='ew')
            # Crear el Entry para la nueva URL
        self.url_entry = ttk.Entry(self.url_entry_frame, width=60)
        self.url_entry.pack(side='left', fill='x', padx=(0,10))

            # Crear el Entry para el número
        self.number_entry = ttk.Entry(self.url_entry_frame, width=5)
        self.number_entry.pack(side='left', fill='x')
        ttk.Label(self.url_entry_frame, text='g').pack(side='left', fill='x')

            # Crear el botón para agregar la nueva URL y número
        self.add_button = ttk.Button(self.url_entry_frame, text="✓", width=3, command=self.add_url)
        self.add_button.pack(side='left', fill='x', padx=(5,0))

            # Crear el botón para eliminar la URL seleccionada
        # self.remove_button = ttk.Button(self.info_frame, text="Eliminar URL", command=self.remove_selected_url)
        # self.remove_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.print_button = ttk.Button(self.info_frame, text="Print", command=self.print)
        self.print_button.grid(row=4, column=2, pady=10)

    def print(self):
        if self.url_frame.winfo_children() == []: print("No hay urls que mostrar")
        link = []
        for widget in self.url_frame.winfo_children():
            for widget2 in widget.winfo_children():
                if widget2.widgetName == 'ttk::label':
                    if 'http' in widget2['text']:
                        print(link)
                        link = [widget2['text']]
                    else:
                        link.append(widget2['text'])
        print(link)

    def añadir_url(self, url):
        estilo = "Oscuro.Label" if self.url_count % 2 == 0 else "Claro.Label"
        self.url_count += 1
        frame = ttk.Frame(self.url_frame, style=estilo)
        frame.pack(fill='x')

        label = ttk.Label(frame, text=url, width=60, style=estilo)
        label.pack(fill='x', side='left')
        boton = ttk.Button(frame, command=lambda: self.eliminar_widget(frame), text='🗑', width=3)
        boton.pack(fill='x', side='right')
        info = ttk.Label(frame, text="pedro", width=5, style=estilo)
        info.pack(fill='x', side='right', padx=10)

    def eliminar_widget(self, widget: ttk.Widget):
        for hijo in widget.winfo_children():
            self.eliminar_widget(hijo)
        widget.destroy()
        self.url_count -= 1
        self.refresh_urls()

    def refresh_urls(self):
        for index, widget in enumerate(self.url_frame.winfo_children()):
            estilo = "Oscuro.Label" if index % 2 == 0 else "Claro.Label"
            widget.configure(style=estilo)
            for widget2 in widget.winfo_children():
                pass

    def add_url(self):
        new_url = self.url_entry.get()
        number = self.number_entry.get()
        if new_url and number.replace('.','',1).isdigit():
            self.añadir_url(new_url)
            self.url_entry.delete(0, tk.END)
            self.number_entry.delete(0, tk.END)

    def edit_label(self):
        # Mostrar el Entry y los botones, ocultar el Label
        self.title_label.pack_forget()
        self.title_edit_button.pack_forget()
        self.entry_text.set(self.label_text.get())
        self.entry.pack(side='left', padx=10)
        self.confirm_button.pack(side='left', padx=10)
        self.cancel_button.pack(side='left', padx=10)
        self.entry.focus()

    def confirm_edit(self):
        # Confirmar la edición y mostrar el Label actualizado
        if self.entry_text.get().strip() != '':
            self.label_text.set(self.entry_text.get().strip().capitalize())
            self.terminar_edit()

    def cancel_edit(self):
        # Cancelar la edición y restaurar el Label original
        self.terminar_edit()

    def terminar_edit(self):
        self.entry.pack_forget()
        self.confirm_button.pack_forget()
        self.cancel_button.pack_forget()
        self.title_label.pack(side='left', padx=10)
        self.title_edit_button.pack(side='left', padx=10)        

if __name__ == "__main__":
    root = tk.Tk()
    app = Info(root)
    root.mainloop()
