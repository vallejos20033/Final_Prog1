# Definición de la clase PyS (Película o Serie)
class PyS:
    def __init__(self, titulo, productora, generos,tipo, fecha_estreno, valoracion):
        self.titulo = titulo
        self.productora = productora
        self.generos = generos
        self.tipo = tipo
        self.fecha_estreno = fecha_estreno
        self.valoracion = valoracion

# Lista de películas y series (PyS)
pys_list = [
    PyS("Lavida continua", "Rw", ["Romance"], "Película", "1969-09-04",5),
    PyS("Mi primera vez", "Rw", ["Romance"], "Serie", "2023-02-13",8),
    PyS("Barbie", "Sony", ["Comedia"], "Película", "2023-07-30",10),
    PyS("Matilda", "Netgli", ["Musical, Fantasia"], "Serie", "2022-12-02",10),
    PyS("Intensamente", "Rw", ["Aventura, Infantil"], "Película", "2020-10-06",12),
]

# Función para listar las PyS almacenadas
def listar_pys():
    print("Listado de Películas y Series:")
    for pys in pys_list:
        imprimir(pys)
# Función para agregar una nueva PyS a la lista
def agregar_pys():
    titulo = input("Ingrese el título: ")
    productora = input("Ingrese la productora: ")
    generos = input("Ingrese los géneros (separados por comas): ").split(",")
    tipo = input("Ingrese el tipo (Película o Serie): ")
    fecha_estreno = input("Ingrese la fecha de estreno (YYYY-MM-DD): ")
    valoracion = (input("Ingrese la valoración de usuarios: "))

    nueva_pys = PyS(titulo, productora, generos, tipo, fecha_estreno, valoracion)
    pys_list.append(nueva_pys)
    print("Película o Serie agregada con éxito.")
# Función para buscar una PyS por su nombre
def buscar_pys_por_nombre(nombre):
    for pys in pys_list:
        ## Se lleva todo a miniscula para realizar la comparacion
        if pys.titulo.lower() == nombre.lower():
            return pys
    return None
#Imprimir los datos de una pelicula o serie
def imprimir(Pys):
    if(Pys!= None):
        print("Título:", Pys.titulo)
        print("Productora:", Pys.productora)
        print("Géneros:", ", ".join(Pys.generos))
        print("Tipo:", Pys.tipo)
        print("Fecha de estreno:", Pys.fecha_estreno)
        print("Valoración de usuarios:", Pys.valoracion)
        print("")
    else:
        print("No se encontro la Pelicula o Serie en la lista")    
#Modificar una pys  solo un atributo
def modificar_pys(pys):
    if(pys!= None):
        print("¿Qué datos desea modificar?")
        print("1. Título")
        print("2. Productora")
        print("3. Géneros")
        print("4. Tipo")
        print("5. Fecha de estreno")
        print("6. Valoración de usuarios")
        opcion = int(input("Ingrese el número de opción: "))

        if opcion == 1:
            pys.titulo = input("Ingrese el nuevo título: ")
        elif opcion == 2:
            pys.productora = input("Ingrese la nueva productora: ")
        elif opcion == 3:
            generos = input("Ingrese los nuevos géneros (separados por comas): ").split(",")
            pys.generos = generos
        elif opcion == 4:
            pys.tipo = input("Ingrese el nuevo tipo (Película o Serie): ")
        elif opcion == 5:
            pys.fecha_estreno = input("Ingrese la nueva fecha de estreno (YYYY-MM-DD): ")
        elif opcion == 6:
            pys.valoracion = float(input("Ingrese la nueva valoración de usuarios: "))
        else:
            print("Opción inválida.")
    else:
        print("No se encontro la Pelicula o Serie para modificar") 
##FUNCIONES ADICIONALES
# Función para listar PyS según el tipo (Película o Serie)
def listar_pys_por_tipo(tipo):
    print("Listado de PyS del tipo", tipo + ":")
    for pys in pys_list:
        if pys.tipo.lower() == tipo.lower():
            imprimir(pys)
## Buscar por el tipo 
def buscarTipo():
    print("¿Qué desea buscar?")
    print("1. Película")
    print("2. Serie")
    opcion = int(input("Ingrese el número de opción: "))
    if opcion==1:
        listar_pys_por_tipo("Película")
    elif opcion==2:
        listar_pys_por_tipo("Serie")
    else:
        print("Esta opcion no existe")
        
# Función para listar PyS según un valor de valoración de usuario
def listar_pys_por_valoracion(valoracion):
        for pys in pys_list:
            if valoracion==pys.valoracion:
                imprimir(pys)
# Función para listar PyS según un género dado
def listar_pys_por_genero(genero):
    print("Listado de PyS del género", genero + ":")
    for pys in pys_list:
        for g in ",".join(pys.generos).split():
            if genero.lower()== g.lower():
                imprimir(pys)

# Funcion para eliminar una pys
def eliminarpys(pysEliminar):
    if (pysEliminar!=None):
        for pys in pys_list:
            if pys==pysEliminar:
                pys_list.remove(pysEliminar)

    else:
        print("No existe esa pelicula o serie")             

# Menú principal
i=0
while i==0:
    print("\n--- Menú Principal ---")
    print("1. Listar todas las Películas y Series")
    print("2. Agregar una nueva Película o Serie")
    print("3. Buscar Película o Serie por nombre")
    print("4. Modificar datos de una Película o Serie")
    print("5. Listar Películas o Series por tipo")
    print("6. Listar Películas o Series por valoración")
    print("7. Listar Películas o Series por género")
    print("8. Eliminar una pelicula o serie segun el nombre")
    print("9. Salir")
    opcion = int(input("Ingrese el número de opción: "))
    if opcion == 1:
        listar_pys()
    elif opcion == 2:
        agregar_pys()
    elif opcion == 3:
        nombre_buscar = input("Ingrese el nombre de la Película o Serie a buscar: ")
        pysEncontrada=buscar_pys_por_nombre(nombre_buscar)
        imprimir(pysEncontrada)
    elif opcion == 4:
        nombre_modificar = input("Ingrese el nombre de la Película o Serie a modificar: ")
        pysEncontrada=buscar_pys_por_nombre(nombre_modificar)
        modificar_pys(pysEncontrada) 
    elif opcion == 5: 
        buscarTipo()
    elif opcion ==6:
        valoracion=int(input("Ingrese  la valoracion a buscar: "))
        listar_pys_por_valoracion(valoracion)
    elif opcion==7:
        genero_buscar = input("Ingrese el genero de la Película o Serie a buscar: ")
        listar_pys_por_genero(genero_buscar)
    elif opcion==8:
        nombre= input("Ingrese el nombre de la pelicula o serie a eliminar: ")
        pysEliminar=buscar_pys_por_nombre(nombre)
        eliminarpys(pysEliminar)    
    elif opcion==9:
        exit()
    else:
        print("Opcion invalida")