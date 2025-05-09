'''
tienda_web/
│
├── app.py
├── productos.json
├── ventas.json
└── templates/
    ├── base.html
    ├── index.html
    ├── productos.html
    ├── ventas.html
    └── historial.html
'''
from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime

app = Flask(__name__)

PRODUCTS_FILE = 'productos.json'
VENTAS_FILE = 'ventas.json'

def cargar_datos(archivo):
    if os.path.exists(archivo):
        with open(archivo, 'r') as f:
            return json.load(f)
    return []

def guardar_datos(archivo, datos):
    with open(archivo, 'w') as f:
        json.dump(datos, f, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    productos = cargar_datos(PRODUCTS_FILE)

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])

        nuevo = {
            'id': len(productos) + 1,
            'nombre': nombre,
            'precio': precio,
            'stock': stock
        }
        productos.append(nuevo)
        guardar_datos(PRODUCTS_FILE, productos)
        return redirect('/productos')

    return render_template('productos.html', productos=productos)

@app.route('/ventas', methods=['GET', 'POST'])
def ventas():
    productos = cargar_datos(PRODUCTS_FILE)
    ventas = cargar_datos(VENTAS_FILE)

    if request.method == 'POST':
        producto_id = int(request.form['producto_id'])
        cantidad = int(request.form['cantidad'])

        for p in productos:
            if p['id'] == producto_id and p['stock'] >= cantidad:
                p['stock'] -= cantidad
                venta = {
                    'producto_id': producto_id,
                    'nombre': p['nombre'],
                    'cantidad': cantidad,
                    'precio_unitario': p['precio'],
                    'total': cantidad * p['precio'],
                    'fecha': datetime.now().isoformat()
                }
                ventas.append(venta)
                guardar_datos(PRODUCTS_FILE, productos)
                guardar_datos(VENTAS_FILE, ventas)
                break

        return redirect('/ventas')

    return render_template('ventas.html', productos=productos)

@app.route('/historial')
def historial():
    ventas = cargar_datos(VENTAS_FILE)
    total = sum(v['total'] for v in ventas)
    return render_template('historial.html', ventas=ventas, total=total)

if __name__ == '__main__':
    app.run(debug=True)
    input()

import pandas as pd
from flask import send_file
from io import BytesIO

@app.route('/exportar_excel')
def exportar_excel():
    try:
        with open('ventas.json', 'r') as f:
            ventas = json.load(f)
    except FileNotFoundError:
        ventas = []

    if not ventas:
        return "No hay ventas para exportar", 400

    df = pd.DataFrame(ventas)
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Ventas')

    output.seek(0)
    return send_file(output,
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     download_name='ventas.xlsx',
                     as_attachment=True)


    

