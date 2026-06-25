from validacion import *
from principal import *

lista_dragon_ball = []
opcion = 0

while opcion != 9:
    print("\n", "===================", "\n",
    "1- Importar y guardar datos.", "\n",
    "2- Mostrar datos.", "\n",
    "3- Modificar datos.", "\n",
    "4- Eliminar datos.", "\n",
    "5- Ordenar datos", "\n",
    "6- Listar los datos del personaje con más cantidad de técnicas.", "\n",
    "7- Listar los datos del personaje con más/menos"
        " cantidad de transformaciones", "\n",
    "8- Salir", "\n",
    "===================", "\n")
    
    opcion = pedir_entero_rango(
        "Ingrese opcion: ",
        "ERROR: reingrese opcion: ",
        1,
        8
    )

    match opcion:
        case 1:
            lista_dragon_ball = importar_datos()

        case 2:
            if verificar_importacion(lista_dragon_ball) == True: 
                listar_por_raza(lista_dragon_ball)
            else:
                mostrar_error()

        case 3:
            if verificar_importacion(lista_dragon_ball) == True:
                modificar_dato(lista_dragon_ball)
            else:
                mostrar_error()

        case 4:
            if verificar_importacion(lista_dragon_ball) == True:
                eliminar_dato(lista_dragon_ball)
            else:
                mostrar_error()

        case 5:
            if verificar_importacion(lista_dragon_ball) == True:
                ordenar_datos(lista_dragon_ball)
            else:
                mostrar_error()

        case 6:
            if verificar_importacion(lista_dragon_ball) == True:
                listar_mas_tecnicas(lista_dragon_ball)
            else:
                mostrar_error()

        case 7:
            if verificar_importacion(lista_dragon_ball) == True:
                listar_transformaciones(lista_dragon_ball)
            else:
                mostrar_error()

        case 8:
            print("\n")
            print("Adiós.")
            break
        
        case _:
            print("Opcion inválida")

