import openpyxl

def precios():
    path = "precios.xlsx"
    wb = openpyxl.load_workbook(filename=path)
    hoja = wb.active

    # print(ws['A1'].value)   # Nombre
    # print(ws.cell(row=1,column=1).value) # Nombre
    productos = {}
    cant_filas = hoja.max_row
    for fila in range(2,cant_filas+1):
        producto     = hoja.cell(row=fila, column=1).value
        precio       = hoja.cell(row=fila, column=2).value
        productos[producto] = {'precio':precio}

    return productos

precios() # {'cafe': {'precio': 30.97}, 'oreo': {'precio': 343.33}, 'pan_lactal': {'precio': 374.83}}