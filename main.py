import sql

sql.crear_db()
op = 0
op_txt = "\0"

op = sql.menu()
while op != -1:
    match op:
        case 1: #Ingreso del producto
            while op_txt != "no":
                sql.agregar_producto()
                op_txt = input("¿Desea agregar otro producto? (si/no): ")
                while op_txt.lower() != "si" and op_txt.lower() != "no":
                    op_txt = input(sql.Fore.RED + "Respuesta no válida. Por favor, ingrese 'si' o 'no': " + sql.Fore.RESET)
                op_txt = op_txt.lower()
        case 2: #Ver productos
            sql.ver_productos()
        case 3: #actualizar producto
            sql.actualizar_datos()
        case 4: #Eliminar producto
            sql.eliminar_producto()
        case 5:
            sql.buscar_producto()
    #termina el match

    op = sql.menu()
    #termina el while
sql.cerrar_programa()
print("fin del programa")
