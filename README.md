# 🛒 Tienda Familiar Web

https://tienda-familiar.onrender.com

Una aplicación web simple para el control de una tienda familiar. Permite gestionar productos, registrar ventas y consultar un historial con ingresos generados.

---

## 🧰 Tecnologías usadas

- Python 3
- Flask
- HTML + Bootstrap (para la interfaz)
- JSON (para almacenamiento local)

---

## ⚙️ Funcionalidades

- ✅ Agregar productos con nombre, precio y stock.
- ✅ Registrar ventas restando del inventario.
- ✅ Ver historial de ventas.
- ✅ Calcular ingresos totales.

---

## 📁 Estructura del proyecto

tienda_web/
│
├── app.py # Lógica principal de la app Flask
├── productos.json # Datos de productos
├── ventas.json # Datos de ventas
├── requirements.txt # Dependencias
├── Procfile # Instrucción de ejecución para hosting
└── templates/ # Archivos HTML
├── base.html
├── index.html
├── productos.html
├── ventas.html
└── historial.html

📌 Notas
Este proyecto usa archivos JSON para guardar datos (no se borra al reiniciar).

Se puede adaptar fácilmente para usar SQLite o MySQL si se desea.

🚀 Mejoras futuras
Autenticación de usuarios (login/admin)

Reportes en PDF o Excel

Gráficas de ventas

App móvil con React Native o Flutter

📬 Contacto
Hecho con ❤️ para prácticas familiares.
Desarrollado por [icaito-ricodi]
Contactame ["https://forms.gle/BDHXrtLWut9Uy8Qe8"]
