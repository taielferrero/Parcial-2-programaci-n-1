from validacion import *
from principal import *

lista_historica = []
opcion = 0

while opcion != 8: 
    print("""
============================================================
1- Importar y guardar datos.
2- Mostrar datos por época.
3- Modificar datos.
4- Eliminar datos.
5- Ordenar datos
6- Personaje con más logros.
7- Personaje con menos eventos históricos.
8- Guardar y salir
============================================================""")
    
    opcion = pedir_entero_rango(
        "Ingrese opcion: ",
        "ERROR: reingrese opcion: ",
        1,
        8
    )

    match opcion:
        case 1:
            lista_historica = importar_datos()

        case 2:
            if verificar_importacion(lista_historica):
                listar_por_epoca(lista_historica)  
            else:
                mostrar_error()

        case 3:
            if verificar_importacion(lista_historica):
                modificar_dato(lista_historica)    
            else:
                mostrar_error()

        case 4:
            if verificar_importacion(lista_historica):
                eliminar_dato(lista_historica)     
            else:
                mostrar_error()

        case 5:
            if verificar_importacion(lista_historica):
                ordenar_datos(lista_historica)     
            else:
                mostrar_error()

        case 6:
            if verificar_importacion(lista_historica):
                listar_mas_logros(lista_historica) 
            else:
                mostrar_error()

        case 7:
            if verificar_importacion(lista_historica):
                listar_menos_eventos(lista_historica)  
            else:
                mostrar_error()

        case 8:
            print("\n")
            guardar_datos(lista_historica)          
            print("Adiós.")
            break
        
        case _:
            print("Opcion inválida")