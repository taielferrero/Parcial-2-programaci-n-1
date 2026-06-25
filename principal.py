import json
from validacion import *

# punto 1
def importar_datos():
    """Importa los datos del archivo JSON"""
    
    with open ("SEGUNDO PARCIAL/AD/dragon_ball.json", "r") as archivo_json:
        datos = json.load(archivo_json)

    print("Datos cargados:", len(datos))
    return datos

# punto 2
def listar_por_raza(lista):
    """Lista los datos de una raza especifica"""
    
    razas = obtener_categorias_unicas(lista, "raza")
    
    print("\n=== RAZAS DISPONIBLES ===")
    for raza in razas:
        print("-", raza)
    print("----------------------------------------")
    
    raza_buscar = pedir_texto(
        "Ingrese el nombre de la raza: ",
        "ERROR: No puede estar vacio. Ingrese la raza: "
    )
    
    
    datos_encontrados = []
    for dato in lista:
        if dato["raza"].lower() == raza_buscar.lower():
            datos_encontrados.append(dato)
    
    if len(datos_encontrados) > 0:
        print("\n=== DATOS DE LA RAZA", raza_buscar, "===")
        print("Total:", len(datos_encontrados), "datos\n")
        
        for i in range(len(datos_encontrados)):
            dato = datos_encontrados[i]
            print("""
Dato""" , i + 1, """
Nombre:""", dato["nombre"], """
Raza:""", dato["raza"], """
Nivel de poder:""", dato["nivel_poder"], """
Planeta:""", dato["planeta"], """
Edad:""", dato["edad"], """
Alineacion:""", dato["alineacion"])
            
            
            print("Transformaciones:")
            if len(dato["transformaciones"]) > 0:
                for transformacion in dato["transformaciones"]:
                    print("-", transformacion)
            else:
                print("Ninguna")
            
            
            print("Tecnicas:")
            if len(dato["tecnicas"]) > 0:
                for tecnica in dato["tecnicas"]:
                    print("-", tecnica)
            else:
                print("Ninguna")
            
            print("--------------------")
    else:
        print("No se encontraron datos de la raza", raza_buscar,"\n")
        raza_buscar = pedir_texto(
        "Ingrese el nombre de la raza: ",
        "ERROR: No puede estar vacio. Ingrese la raza: "
    )
        
# punto 3
def modificar_dato(lista):
    """Modifica un dato existente en la lista"""
    
    nombre_buscar = pedir_texto(
        "Ingrese el nombre del dato a modificar: ",
        "ERROR: No puede estar vacio. Ingrese el nombre: "
    )
    
    dato_encontrado = None
    for dato in lista:
        if dato["nombre"].lower() == nombre_buscar.lower():
            dato_encontrado = dato
            break
    
    if dato_encontrado == None:
        print("No se encontro un dato con ese nombre")
        return
    
    seguir_modificando = True

    while seguir_modificando == True:
        print("""
Dato encontrado:
Nombre:""", dato_encontrado["nombre"], """
Raza:""", dato_encontrado["raza"], """
Nivel de poder:""", dato_encontrado["nivel_poder"], """
Planeta:""", dato_encontrado["planeta"], """
Edad:""", dato_encontrado["edad"], """
Alineacion:""", dato_encontrado["alineacion"])
        
        if len(dato_encontrado["transformaciones"]) > 0:
            texto = ""
            for i in range(len(dato_encontrado["transformaciones"])):
                if i == len(dato_encontrado["transformaciones"]) - 1:
                    texto = texto + dato_encontrado["transformaciones"][i]
                else:
                    texto = texto + dato_encontrado["transformaciones"][i] + ", "
            print("Transformaciones:", texto)
        else:
            print("Transformaciones: Ninguna")
        
        if len(dato_encontrado["tecnicas"]) > 0:
            texto = ""
            for i in range(len(dato_encontrado["tecnicas"])):
                if i == len(dato_encontrado["tecnicas"]) - 1:
                    texto = texto + dato_encontrado["tecnicas"][i]
                else:
                    texto = texto + dato_encontrado["tecnicas"][i] + ", "
            print("Tecnicas:", texto)
        else:
            print("Tecnicas: Ninguna")

        print("""
=== QUE DESEA MODIFICAR ===
1- Nombre
2- Raza
3- Nivel de poder
4- Planeta
5- Edad
6- Alineacion
7- Transformaciones
8- Tecnicas
9- salir (volver al menu)""")
    
        opcion = pedir_entero_rango(
            "Ingrese opcion: ",
            "ERROR: reingrese opcion: ",
            1,
            9
        )
        
        if opcion == 9:
            print("Modificaciones finalizadas")
            seguir_modificando = False
            break
        
        if opcion == 1:
            nuevo_valor = pedir_texto(
                "Ingrese el nuevo nombre: ",
                "ERROR: No puede estar vacio. Ingrese el nuevo nombre: "
            )
            dato_encontrado["nombre"] = nuevo_valor
            print("Nombre modificado correctamente")
        
        elif opcion == 2:
            nuevo_valor = pedir_texto(
                "Ingrese la nueva raza: ",
                "ERROR: No puede estar vacio. Ingrese la nueva raza: "
            )
            dato_encontrado["raza"] = nuevo_valor
            print("Raza modificada correctamente")
        
        elif opcion == 3:
            nuevo_valor = pedir_float_positivo(
                "Ingrese el nuevo nivel de poder: ",
                "ERROR: Ingrese un numero positivo: "
            )
            dato_encontrado["nivel_poder"] = nuevo_valor
            print("Nivel de poder modificado correctamente")
        
        elif opcion == 4:
            nuevo_valor = pedir_texto(
                "Ingrese el nuevo planeta: ",
                "ERROR: No puede estar vacio. Ingrese el nuevo planeta: "
            )
            dato_encontrado["planeta"] = nuevo_valor
            print("Planeta modificado correctamente")
        
        elif opcion == 5:
            nuevo_valor = pedir_entero_rango(
                "Ingrese la nueva edad: ",
                "ERROR: Ingrese una edad valida (mayor a 0): ",
                1,
                999
            )
            dato_encontrado["edad"] = nuevo_valor
            print("Edad modificada correctamente")
        
        elif opcion == 6:
            nuevo_valor = pedir_texto(
                "Ingrese la nueva alineacion: ",
                "ERROR: No puede estar vacio. Ingrese la nueva alineacion: "
            )
            dato_encontrado["alineacion"] = nuevo_valor
            print("Alineacion modificada correctamente")
        
        elif opcion == 7:
            print("Transformaciones actuales:", dato_encontrado["transformaciones"])
            print("Ingrese las nuevas transformaciones (una por una)")
            print("Para finalizar, ingrese 'fin'")
            
            nueva_lista = []
            while True:
                transformacion = input("Ingrese transformacion: ")
                if transformacion.lower() == "fin":
                    break
                if transformacion != "":
                    nueva_lista.append(transformacion)
            
            dato_encontrado["transformaciones"] = nueva_lista
            print("Transformaciones modificadas correctamente")

        elif opcion == 8:
            print("Tecnicas actuales:", dato_encontrado["tecnicas"])
            print("Ingrese las nuevas tecnicas (una por una)")
            print("Para finalizar, ingrese 'fin'")
            
            nueva_lista = []
            while True:
                tecnica = input("Ingrese tecnica: ")
                if tecnica.lower() == "fin":
                    break
                if tecnica != "":
                    nueva_lista.append(tecnica)
            
            dato_encontrado["tecnicas"] = nueva_lista
            print("Tecnicas modificadas correctamente")

        # Mostrar dato actualizado DESPUES de cualquier modificacion
        print("""
--- DATO ACTUALIZADO ---
Nombre:""", dato_encontrado["nombre"], """
Raza:""", dato_encontrado["raza"], """
Nivel de poder:""", dato_encontrado["nivel_poder"], """
Planeta:""", dato_encontrado["planeta"], """
Edad:""", dato_encontrado["edad"], """
Alineacion:""", dato_encontrado["alineacion"])
        
        if len(dato_encontrado["transformaciones"]) > 0:
            texto = ""
            for i in range(len(dato_encontrado["transformaciones"])):
                if i == len(dato_encontrado["transformaciones"]) - 1:
                    texto = texto + dato_encontrado["transformaciones"][i]
                else:
                    texto = texto + dato_encontrado["transformaciones"][i] + ", "
            print("Transformaciones:", texto)
        else:
            print("Transformaciones: Ninguna")
        
        if len(dato_encontrado["tecnicas"]) > 0:
            texto = ""
            for i in range(len(dato_encontrado["tecnicas"])):
                if i == len(dato_encontrado["tecnicas"]) - 1:
                    texto = texto + dato_encontrado["tecnicas"][i]
                else:
                    texto = texto + dato_encontrado["tecnicas"][i] + ", "
            print("Tecnicas:", texto)
        else:
            print("Tecnicas: Ninguna")

        print("""
------------------------

¿Desea modificar otro dato?
1- Si
2- No (volver al menu)""")
        
        opcion_seguir = pedir_entero_rango(
            "Ingrese opcion: ",
            "ERROR: Ingrese 1 o 2: ",
            1,
            2
        )
        
        if opcion_seguir == 2:
            print("Modificaciones finalizadas")
            seguir_modificando = False

# punto 4
def eliminar_dato(lista):
    """Elimina un dato de la lista por nombre"""
    
    nombre_buscar = pedir_texto(
        "Ingrese el nombre del dato a eliminar: ",
        "ERROR: No puede estar vacio. Ingrese el nombre: "
    )
    
    indice_encontrado = -1
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre_buscar.lower():
            indice_encontrado = i
            break
    
    if indice_encontrado == -1:
        print("No se encontro un dato con ese nombre")
        return
    
    
    print("""
Dato encontrado:
Nombre:""", lista[indice_encontrado]["nombre"], """
Raza:""", lista[indice_encontrado]["raza"], """
Nivel de poder:""", lista[indice_encontrado]["nivel_poder"], """
Planeta:""", lista[indice_encontrado]["planeta"], """
Edad:""", lista[indice_encontrado]["edad"], """
Alineacion:""", lista[indice_encontrado]["alineacion"])
    
    
    print("""
¿Esta seguro que desea eliminar este dato?
1- Si
2- No (volver al menu)""")
    
    opcion = pedir_entero_rango(
        "Ingrese opcion: ",
        "ERROR: Ingrese 1 o 2: ",
        1,
        2
    )
    
    if opcion == 1:
        lista.pop(indice_encontrado)
        print("Dato eliminado correctamente")
    else:
        print("Eliminacion cancelada")

# punto 5
def ordenar_datos(lista):
    """Ordena una copia de la lista por nombre, raza o edad"""
    
    print("""
=== CRITERIOS DE ORDENAMIENTO ===
1- Nombre
2- Raza
3- Edad""")
    
    opcion = pedir_entero_rango(
        "Ingrese el criterio de ordenamiento: ",
        "ERROR: Ingrese 1, 2 o 3: ",
        1,
        3
    )
    
    
    if opcion == 1:
        clave = "nombre"
        print("\nLista ordenada por NOMBRE")
    elif opcion == 2:
        clave = "raza"
        print("\nLista ordenada por RAZA")
    else:
        clave = "edad"
        print("\nLista ordenada por EDAD")
    
    
    copia_lista = []
    for dato in lista:
        copia_lista.append(dato)
    
    
    for i in range(len(copia_lista)):
        for j in range(i + 1, len(copia_lista)):
            if copia_lista[i][clave] > copia_lista[j][clave]:
                aux = copia_lista[i]
                copia_lista[i] = copia_lista[j]
                copia_lista[j] = aux
    
    
    print("\n=== LISTA ORDENADA ===")
    for i in range(len(copia_lista)):
        print("Dato", i + 1)
        print("Nombre:", copia_lista[i]["nombre"])
        print("Raza:", copia_lista[i]["raza"])
        print("Edad:", copia_lista[i]["edad"])
        print("--------------------")

# punto 6:
def listar_mas_tecnicas(lista):
    """Lista los datos del personaje con mas tecnicas"""
    
    if len(lista) == 0:
        print("No hay datos en la lista")
        return
    
    
    indice_maximo = 0
    for i in range(len(lista)):
        if len(lista[i]["tecnicas"]) > len(lista[indice_maximo]["tecnicas"]):
            indice_maximo = i
    
    
    print("""
=== DATO CON MAS TECNICAS ===
Nombre:""", lista[indice_maximo]["nombre"], """
Raza:""", lista[indice_maximo]["raza"], """
Nivel de poder:""", lista[indice_maximo]["nivel_poder"], """
Planeta:""", lista[indice_maximo]["planeta"], """
Edad:""", lista[indice_maximo]["edad"], """
Alineacion:""", lista[indice_maximo]["alineacion"])
    
    if len(lista[indice_maximo]["transformaciones"]) > 0:
        texto = ""
        for i in range(len(lista[indice_maximo]["transformaciones"])):
            if i == len(lista[indice_maximo]["transformaciones"]) - 1:
                texto = texto + lista[indice_maximo]["transformaciones"][i]
            else:
                texto = texto + lista[indice_maximo]["transformaciones"][i] + ", "
        print("Transformaciones:", texto)
    else:
        print("Transformaciones: Ninguna")
    
    if len(lista[indice_maximo]["tecnicas"]) > 0:
        texto = ""
        for i in range(len(lista[indice_maximo]["tecnicas"])):
            if i == len(lista[indice_maximo]["tecnicas"]) - 1:
                texto = texto + lista[indice_maximo]["tecnicas"][i]
            else:
                texto = texto + lista[indice_maximo]["tecnicas"][i] + ", "
        print("Tecnicas:", texto)
    else:
        print("Tecnicas: Ninguna")
    
    print("\nCantidad de tecnicas:", len(lista[indice_maximo]["tecnicas"]))

# punto 7:
def listar_transformaciones(lista):
    """Lista los datos del personaje con mas o menos transformaciones"""
    
    if len(lista) == 0:
        print("No hay datos en la lista")
        return
    
    print("""
=== OPCIONES ===
1- Personaje con MAS transformaciones
2- Personaje con MENOS transformaciones""")
    
    opcion = pedir_entero_rango(
        "Ingrese opcion: ",
        "ERROR: Ingrese 1 o 2: ",
        1,
        2
    )
    
    indice_encontrado = 0
    for i in range(len(lista)):
        if opcion == 1:
            if len(lista[i]["transformaciones"]) > len(lista[indice_encontrado]["transformaciones"]):
                indice_encontrado = i
        else:
            if len(lista[i]["transformaciones"]) < len(lista[indice_encontrado]["transformaciones"]):
                indice_encontrado = i
    
    
    if len(lista[indice_encontrado]["transformaciones"]) > 0:
        texto_transformaciones = ""
        for i in range(len(lista[indice_encontrado]["transformaciones"])):
            if i == len(lista[indice_encontrado]["transformaciones"]) - 1:
                texto_transformaciones = texto_transformaciones + lista[indice_encontrado]["transformaciones"][i]
            else:
                texto_transformaciones = texto_transformaciones + lista[indice_encontrado]["transformaciones"][i] + ", "
    else:
        texto_transformaciones = "Ninguna"
    
    
    if len(lista[indice_encontrado]["tecnicas"]) > 0:
        texto_tecnicas = ""
        for i in range(len(lista[indice_encontrado]["tecnicas"])):
            if i == len(lista[indice_encontrado]["tecnicas"]) - 1:
                texto_tecnicas = texto_tecnicas + lista[indice_encontrado]["tecnicas"][i]
            else:
                texto_tecnicas = texto_tecnicas + lista[indice_encontrado]["tecnicas"][i] + ", "
    else:
        texto_tecnicas = "Ninguna"
    
    if opcion == 1:
        print("""
=== PERSONAJE CON MAS TRANSFORMACIONES ===
Nombre:""", lista[indice_encontrado]["nombre"], """
Raza:""", lista[indice_encontrado]["raza"], """
Nivel de poder:""", lista[indice_encontrado]["nivel_poder"], """
Planeta:""", lista[indice_encontrado]["planeta"], """
Edad:""", lista[indice_encontrado]["edad"], """
Alineacion:""", lista[indice_encontrado]["alineacion"], """
Transformaciones:""", texto_transformaciones, """
Tecnicas:""", texto_tecnicas, """
Cantidad de transformaciones:""", len(lista[indice_encontrado]["transformaciones"]))
    else:
        print("""
=== PERSONAJE CON MENOS TRANSFORMACIONES ===
Nombre:""", lista[indice_encontrado]["nombre"], """
Raza:""", lista[indice_encontrado]["raza"], """
Nivel de poder:""", lista[indice_encontrado]["nivel_poder"], """
Planeta:""", lista[indice_encontrado]["planeta"], """
Edad:""", lista[indice_encontrado]["edad"], """
Alineacion:""", lista[indice_encontrado]["alineacion"], """
Transformaciones:""", texto_transformaciones, """
Tecnicas:""", texto_tecnicas, """
Cantidad de transformaciones:""", len(lista[indice_encontrado]["transformaciones"]))
        
# punto 8:
import json

def guardar_datos(lista):
    """Guarda los datos en el archivo JSON"""
    with open("SEGUNDO PARCIAL/AD/dragon_ball.json", "w") as archivo_json:
        json.dump(lista, archivo_json, indent=4)
    print("Datos guardados correctamente")