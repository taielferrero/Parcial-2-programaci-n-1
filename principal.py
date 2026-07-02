import json
from validacion import *

# punto 1
def importar_datos()->list:
    '''
    brief: Importa los datos del archivo JSON y los carga en una lista de diccionarios.
    recibe: None (lee el archivo "historia.json" desde la misma carpeta).
    retorna: una lista de diccionarios con los datos de los personajes.
    '''
    
    with open ("historia.json", "r") as archivo_json:
        datos = json.load(archivo_json)

    print("Datos cargados:", len(datos))
    return datos

# punto 2
def mostrar_datos(lista:list)->None:
    '''
    brief: Muestra de forma amigable una lista de personajes históricos con todos sus atributos.
    recibe: una lista de diccionarios, donde cada diccionario contiene los datos de un personaje.
    retorna: None (solo imprime en pantalla).
    '''
    for i in range(len(lista)):
        dato = lista[i]
        
        print("""
Dato""" , i + 1, """
Nombre:""", dato["nombre"], """
Epoca:""", dato["epoca"], """
Pais:""", dato["pais"], """
Anio_nacimiento:""", dato["anio_nacimiento"], """
Profesion:""", dato["profesion"])
        
        print("Logros:")
        if len(dato["logros"]) > 0:
            for logro in dato["logros"]:
                print("-", logro)
        else:
            print("Ninguno")
        
        print("Eventos:")
        if len(dato["eventos"]) > 0:
            for evento in dato["eventos"]:
                print("-", evento)
        else:
            print("Ninguno")
        
        print("--------------------")

def filtrar_por_epoca(lista:list, epoca_buscar:str)->list:
    '''
    brief: Filtra los personajes por época específica.
    recibe: una lista de diccionarios y un string con la época a buscar.
    retorna: una lista con los personajes que coinciden con la época buscada.
    '''
    datos_encontrados = []
    for dato in lista:
        if dato["epoca"].lower() == epoca_buscar.lower():
            datos_encontrados.append(dato)
    return datos_encontrados

def listar_por_epoca(lista:list)->None:
    '''
    brief: Lista los datos de una época específica. Muestra las épocas disponibles, pide al usuario una época, filtra y muestra los resultados.
    recibe: una lista de diccionarios con los datos de los personajes.
    retorna: None (solo imprime en pantalla).
    '''
    epocas = obtener_categorias_unicas(lista, "epoca")
    
    print("\n=== EPOCAS DISPONIBLES ===")
    for epoca in epocas:
        print("-", epoca)
    print("----------------------------------------")
    
    encontrado = False
    
    while encontrado == False:
        epoca_buscar = pedir_texto(
            "Ingrese el nombre de la epoca: ",
            "ERROR: No puede estar vacio. Ingrese la epoca: "
        )
        
        datos_encontrados = filtrar_por_epoca(lista, epoca_buscar)
        
        if len(datos_encontrados) > 0:
            print("\n=== DATOS DE LA EPOCA", epoca_buscar.upper(), "===")
            print("Total:", len(datos_encontrados), "datos\n")
            mostrar_datos(datos_encontrados)
            encontrado = True
        else:
            print("No se encontraron datos de la epoca", epoca_buscar)
            print("Intente con otra epoca\n")
            

# punto 3
def buscar_por_nombre(lista:list, nombre_buscar:str)->int:
    '''
    brief: Busca un dato por nombre y retorna su índice.
    recibe: una lista de diccionarios y un string con el nombre a buscar.
    retorna: un entero con el índice del dato encontrado, o -1 si no existe.
    '''
    for i in range(len(lista)):
        if lista[i]["nombre"].lower() == nombre_buscar.lower():
            return i
    return -1

def modificar_campo(dato:dict, campo:str, nuevo_valor)->None:
    '''
    brief: Modifica un campo específico de un dato y muestra mensaje de confirmación.
    recibe: un diccionario con los datos del personaje, un string con el campo a modificar y el nuevo valor.
    retorna: None (modifica el diccionario y imprime en pantalla).
    '''
    dato[campo] = nuevo_valor
    print(campo.capitalize() + " modificado correctamente")

def modificar_lista(dato:dict, campo:str)->None:
    '''
    brief: Modifica una lista (logros o eventos) del dato, permitiendo ingresar elementos uno por uno.
    recibe: un diccionario con los datos del personaje y un string con el campo a modificar ("logros" o "eventos").
    retorna: None (modifica el diccionario y imprime en pantalla).
    '''
    print(campo.capitalize() + " actuales:", dato[campo])
    print("Ingrese los nuevos " + campo + " (uno por uno)")
    print("Para finalizar, ingrese 'fin'")
    
    nueva_lista = []
    while True:
        
        if campo == "logros":
            item = input("Ingrese logro: ")
        else:  
            item = input("Ingrese evento: ")
        
        if item.lower() == "fin":
            break
        if item != "":
            nueva_lista.append(item)
    
    dato[campo] = nueva_lista
    print(campo.capitalize() + " modificados correctamente")

def modificar_dato(lista:list)->None:
    '''
    brief: Modifica un dato existente en la lista. Permite modificar nombre, época, país, año de nacimiento, profesión, logros y eventos.
    recibe: una lista de diccionarios con los datos de los personajes.
    retorna: None (modifica la lista y imprime en pantalla).
    '''
    nombre_buscar = pedir_texto(
        "Ingrese el nombre del dato a modificar: ",
        "ERROR: No puede estar vacio. Ingrese el nombre: "
    )
    
    indice = buscar_por_nombre(lista, nombre_buscar)
    
    if indice == -1:
        print("No se encontro un dato con ese nombre")
        return
    
    dato = lista[indice]
    seguir_modificando = True

    while seguir_modificando == True:
        
        print("\n--- DATO ENCONTRADO ---")
        mostrar_datos([dato])
        
        
        print("""
=== QUE DESEA MODIFICAR ===
1- Nombre
2- Epoca
3- Pais
4- Anio_nacimiento
5- Profesion
6- Logros
7- Eventos
8- salir (volver al menu)""")
        
        opcion = pedir_entero_rango(
            "Ingrese opcion: ",
            "ERROR: reingrese opcion: ",
            1,
            8
        )
        
        if opcion == 8:
            print("Modificaciones finalizadas")
            break
        
        
        if opcion == 1:
            nuevo_valor = pedir_texto(
                "Ingrese el nuevo nombre: ",
                "ERROR: No puede estar vacio: "
            )
            modificar_campo(dato, "nombre", nuevo_valor)
        
        elif opcion == 2:
            nuevo_valor = pedir_texto(
                "Ingrese la nueva epoca: ",
                "ERROR: No puede estar vacio: "
            )
            modificar_campo(dato, "epoca", nuevo_valor)
        
        elif opcion == 3:
            nuevo_valor = pedir_texto(
                "Ingrese el nuevo pais: ",
                "ERROR: No puede estar vacio: "
            )
            modificar_campo(dato, "pais", nuevo_valor)
        
        elif opcion == 4:
            nuevo_valor = pedir_entero_rango(
                "Ingrese el nuevo año de nacimiento: ",
                "ERROR: Ingrese un año valido: ",
                -5000,  
                2026    
            )
            modificar_campo(dato, "anio_nacimiento", nuevo_valor)
        
        elif opcion == 5:
            nuevo_valor = pedir_texto(
                "Ingrese la nueva profesion: ",
                "ERROR: No puede estar vacio: "
            )
            modificar_campo(dato, "profesion", nuevo_valor)
        
        elif opcion == 6:
            modificar_lista(dato, "logros")
        
        elif opcion == 7:
            modificar_lista(dato, "eventos")
        
        
        print("\n--- DATO ACTUALIZADO ---")
        mostrar_datos([dato])
        
        
        print("""
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
def eliminar_dato(lista:list)->None:
    '''
    brief: Elimina un dato de la lista por nombre. Muestra el dato encontrado y solicita confirmación antes de eliminar.
    recibe: una lista de diccionarios con los datos de los personajes.
    retorna: None (modifica la lista y imprime en pantalla).
    '''
    
    nombre_buscar = pedir_texto(
        "Ingrese el nombre del dato a eliminar: ",
        "ERROR: No puede estar vacio. Ingrese el nombre: "
    )
    
    indice_encontrado = buscar_por_nombre(lista, nombre_buscar)
    
    if indice_encontrado == -1:
        print("No se encontro un dato con ese nombre")
        return
    
    print("\n--- DATO ENCONTRADO ---")
    mostrar_datos([lista[indice_encontrado]])
    
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
def ordenar_datos(lista:list)->None:
    '''
    brief: Ordena una copia de la lista por nombre, año de nacimiento o época. 
    Crea una copia superficial de la lista original y la ordena sin modificar la original.
    recibe: una lista de diccionarios con los datos de los personajes.
    retorna: None (imprime la lista ordenada en pantalla).
    '''
    
    print("""
=== CRITERIOS DE ORDENAMIENTO ===
1- Nombre
2- Año de nacimiento
3- Época""")
    
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
        clave = "anio_nacimiento"
        print("\nLista ordenada por ANIO_NACIMIENTO")
    else:
        clave = "epoca"
        print("\nLista ordenada por EPOCA")
    
    
    copia_lista = lista.copy()
    
    
    for i in range(len(copia_lista)):
        for j in range(i + 1, len(copia_lista)):
            if copia_lista[i][clave] > copia_lista[j][clave]:
                aux = copia_lista[i]
                copia_lista[i] = copia_lista[j]
                copia_lista[j] = aux
    
    
    print("\n=== LISTA ORDENADA ===")
    mostrar_datos(copia_lista)

# punto 6:
def listar_mas_logros(lista:list)->None:
    '''
    brief: Lista los datos del personaje que posee la mayor cantidad de logros registrados.
    recibe: una lista de diccionarios con los datos de los personajes.
    retorna: None (imprime en pantalla el personaje con más logros y su cantidad).
    '''
    
    if len(lista) == 0:
        print("No hay datos en la lista")
        return
    
    indice_maximo = 0
    for i in range(len(lista)):
        if len(lista[i]["logros"]) > len(lista[indice_maximo]["logros"]):
            indice_maximo = i
    
    print("\n=== PERSONAJE CON MAS LOGROS ===")
    mostrar_datos([lista[indice_maximo]])
    print("Cantidad de logros:", len(lista[indice_maximo]["logros"]))

# punto 7:
def listar_menos_eventos(lista:list)->None:
    '''
    brief: Lista los datos del personaje que posee la menor cantidad de eventos históricos registrados.
    recibe: una lista de diccionarios con los datos de los personajes.
    retorna: None (imprime en pantalla el personaje con menos eventos y su cantidad).
    '''
    
    if len(lista) == 0:
        print("No hay datos en la lista")
        return
    
    indice_minimo = 0
    for i in range(len(lista)):
        if len(lista[i]["eventos"]) < len(lista[indice_minimo]["eventos"]):
            indice_minimo = i
    
    print("\n=== PERSONAJE CON MENOS EVENTOS ===")
    mostrar_datos([lista[indice_minimo]])
    print("Cantidad de eventos:", len(lista[indice_minimo]["eventos"]))
        
# punto 8:
def guardar_datos(lista:list)->None:
    '''
    brief: Guarda los datos en el archivo JSON, sobrescribiendo el contenido existente.
    recibe: una lista de diccionarios con los datos de los personajes.
    retorna: None (guarda en el archivo y imprime un mensaje de confirmación).
    '''
    with open("SEGUNDO PARCIAL/AD/historia.json", "w") as archivo_json:
        json.dump(lista, archivo_json, indent=4)
    print("Datos guardados correctamente")