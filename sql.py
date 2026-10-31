import sqlite3
import colorama
from colorama import Back, Fore, init
init()

    #APERTURA
try:
    archivo = "inventario.db"
    conexion = sqlite3.connect(archivo)
    print(Fore.GREEN + "Conexión exitosa" + Fore.RESET)
    cursor = conexion.cursor()
except Exception as error:
    print(Fore.RED + error + Fore.RESET)

def crear_db():
    #CREAR TABLA
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL,
        categoria TEXT)
        """)

def menu():
    print("Bienvenido al sistema de gestión de productos.\n")
    print("Seleccione una opción:\n")
    print("1. Agregar producto\n")
    print("2. Ver productos\n")
    print("3. Actualizar producto\n")
    print("4. Eliminar producto\n")
    print("5. Buscar producto\n")
    print(Fore.YELLOW + "-1. Salir\n" + Fore.RESET)

    op = int(input("Ingrese la opción deseada: "))
    while op != -1 and (op < 1 or op > 5):
        print(Fore.RED + "Opción no válida. " + Fore.RESET)
        op = int(input("Por favor, ingrese una opción entre 1 y 5, o -1 para salir: "))

    return op
    
def agregar_producto(): # case 1
    try:
        nombre = input("Ingrese el nombre del producto: ")
        while nombre == "" or nombre.isnumeric() == True:
            print(Fore.RED + "El nombre no puede estar vacío ni puede ser un numero." + Fore.RESET)
            nombre = input("Por favor, ingrese el nombre del producto: ")    
        nombre = nombre.capitalize()

        descripcion = input("Ingrese una descripcion al producto (no obligatorio):")

        cantidad = int(input("Ingrese cantidad del producto: "))
        while cantidad <= 0:
            print(Fore.RED + "ErRoR " + Fore.RESET)
            cantidad = int(input("ingrese una cantidad valida: "))

        precio = float(input("Ingrese el precio del producto: "))
        while precio <= 0:
            print(Fore.RED + "El precio no puede ser negativo ni cero" + Fore.RESET)
            precio = float(input("Por favor, ingrese el precio del producto: "))

        categoria = input("Ingrese la categoria del producto: ")
        while categoria == "" or categoria.isnumeric() == True:
            print(Fore.RED + "El nombre no puede estar vacío ni puede ser un numero." + Fore.RESET)
            categoria = input("Por favor, ingrese el nombre del producto: ")
            categoria = categoria.capitalize()
        cursor.execute("INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)", (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
    except Exception as error:
        conexion.rollback()
        print(Fore.RED + str(error) + Fore.RESET)

def ver_productos(): # case 2
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print(productos)

def actualizar_datos(): #case 3
    try:
        id_producto = int(input("ingrese el ID del producto: "))
        precioProducto = float(input("Ingrese el nuevo precio del producto: "))
        while (precioProducto <= 0):
            print(Fore.RED + "ErRoR" + Fore.RESET)
            precioProducto = float(input("el precio del producto tiene que ser mayor a 0: "))
        cursor.execute("UPDATE productos SET precio = ? WHERE id = ?", (precioProducto, id_producto))
        conexion.commit()
    except Exception as error:
        conexion.rollback()
        print(Fore.RED + str(error) + Fore.RESET)

def eliminar_producto(): # case 4
    try:
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
    except Exception as error:
        conexion.rollback()
        print(Fore.RED + str(error) + Fore.RESET)

def buscar_producto(): # case 5
    id_producto = int(input("ingrese el ID del producto: "))
    cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
    producto = cursor.fetchone()
    print(producto)

def reportar_productos():
    limite = int(input("ingrese la cantidad del producto a buscar: "))
    cursor.execute("SELECT * FROM productos WHERE cantidad = ?", (limite,))
    producto = cursor.fetchall()
    print(producto)
    

def cerrar_programa(): # FIN
    conexion.close()