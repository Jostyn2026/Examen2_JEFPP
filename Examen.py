# Importa la librería que permite conectar Python con MySQL
import mysql.connector

# Conexión a MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="restaurante_bd"
)

# Crea un cursor, que sirve para enviar instrucciones
# SQL desde Python hacia MySQL.
cursor = conexion.cursor()

# Programa de simulasion de restaurante. JP:]
print( "--- PROGRAMA RESTAURANTE  ---\n")

# Lista que almacenara datos del restaurante. JP:]
menu = []


print( "️ Bienvenido al Sistema de Menú de Restaurante")

# Iniciamos un bucle while: JP:]
while True:
    # Mostramos las opciones del menú. JP:]
    print( "\n Seleccione una opción: :)")
    print( "1. Agregar un plato")
    print( "2. Eliminar un plato")
    print( "3. Mostrar el menú actual")
    print("4. Salir")

    # Solicitamos al usuario la opcion. JP:]
    opcion = input( "Ingrese el numero de la opcion deseada: ")

    # Opciónn agregar plato. JP:]
    if opcion == "1":
        plato_nuevo = input( "Ingrese el nombre del plato a agregar: ").strip()
        menu.append(plato_nuevo)
        print( f" Plato '{plato_nuevo}' agregado correctamente al menu.")

    # Opción elimibar plato. JP:]
    elif opcion == "2":
        plato_eliminado = input( "Ingrese el nombre del plato a eliminar: ").strip()
        if plato_eliminado in menu:
            menu.remove(plato_eliminado)
            print(f" Plato '{plato_eliminado}' eliminado del menú.")
        else:
            print(f" El plato '{plato_eliminado}' no se encuentra en el menú.")

    # Opción vista al menu. JP:]
    elif opcion == "3":
        if len(menu) == 0:
            print(" No hay nada en el menu. Agregate otro plato")
        else:
            print( "\n Menú del Restaurante:")
            for idx, plato in enumerate(menu, start=1):
                print(f"{idx}. {plato}")

    # Opción salir del programa. JP:]
    elif opcion == "4":
        print( " Graciaspor visitar nuestro restaurante digital, !Espero verte pronto¡")
        break # usamos un break para romper el bucle

    # Si el ususario elige otra opcion. JP:]
    else:
        print(" Opción inválida. Por favor ingrese un número del 1 al 4.")

# Cierra el cursor.
cursor.close()
# Cierra la conexión con MySQL.
conexion.close()

