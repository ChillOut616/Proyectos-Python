# Asignatura: Programación
# NRC: 12700
# Docente: Ismael Moreno 
# Descripción: Programa para generar un plan de una faena durante un número de días especificos.
# Programadores: Simon, Diego


## VARIABLES PARA CAPTURA DE DATOS
    ## Datos de entrada
def plan_prod():
    faena = input("Nombre de la faena: ") ## se utiliza (input(x)) para capturar datos
    dias = int(input("Cantidad de días que se faenara: ")) ## se utiliza int(input(x)) para capturar datos
    materia_prima = input("Tipo de materia prima: ") ## se utiliza (input(x)) para capturar datos
    costo_por_tonelada = float(input("Costo en dolares por tonelada de la materia prima: ")) ## aqui se utiliza float(input(x)) ya que permite representar un número positivo o negativo con decimales
    return faena, dias, materia_prima, costo_por_tonelada ## aqui devuelve los valores
    ## Datos de entrada
def datos_de_produccion(dias):  
    produccion_diaria = [] ## Lista para almacenar la cantidad de toneladas de materia prima necesarias por día
    for dia in range(1, dias + 1):  
        toneladas = float(input(f"Cantidad de toneladas necesarias en el día {dia}: "))
        produccion_diaria.append(toneladas)
    return produccion_diaria ## devuelve la lista con la cantidad de toneladas de materia prima necesarias por día
    ## Datos de entrada 
def costo_faena(produccion_diaria, costo_por_tonelada):
    total_toneladas = sum(produccion_diaria)  ## aqui utilizamos la operación matemática sum()
    costo_total = total_toneladas * costo_por_tonelada
    print(f"Total de toneladas de materia prima usadas: {total_toneladas}")
    print(f"Costo total de la faena: ${costo_total}")
    ## Datos de entrada
def parametros_produccion(produccion_diaria):
    promedio_diario = sum(produccion_diaria) / len(produccion_diaria) ## aqui utilizamos la operación matemática sum()
    maximo = max(produccion_diaria) ## se establece como dato la cantidad maxima
    minimo = min(produccion_diaria) ## se establece como dato la cantidad minima
    ## Muestra los datos de salida al usuario
    print(f"Cantidad promedio diaria de materia prima utilizada: {promedio_diario}")  
    print(f"Cantidad máxima de toneladas usadas en la faena: {maximo}")
    print(f"Cantidad mínima de toneladas usadas en la faena: {minimo}") 
    ## Aqui se genera la función menu_principal()
def menu_principal(): ## Las variables utilizadas en el programa, "None" se utiliza para que tenga un valor no especifico hasta que se le asigne uno
    faena = None               ## variable para almacenar el nombre de faena
    dias = None                ## variable para almacenar la cantidad de dias de la faena
    materia_prima = None       ## variable para almacenar el tipo de materia prima
    costo_por_tonelada = None  ## variable para almacenar el costo por tonelada
    produccion_diaria = []     ## muestra la lista que se genera en el def() de ingreso de datos previos

    while True:                                        ## Empieza la funcion While que mientras es verdadera (true) se repetira
        print("\n--- Menú ---")                        ## Se plantea el menu solicitado
        print("1. Generar plan de producción")         ## Primera opcion
        print("2. Ingresar datos de producción")       ## Segunda opcion
        print("3. Mostrar el costo de la faena")       ## Tercera opcion
        print("4. Mostrar parámetros de producción")   ## Cuarta opcion
        print("5. Finalizar el programa")              ## Quinta opcion 

        opcion = input("Seleccione una opción: ")      ## Se propone elegir una opcion

        if opcion == "1":                 ## si la opcion fue 1 se ejecutara el def(plan_prod)
            faena, dias, materia_prima, costo_por_tonelada = plan_prod()
        elif opcion == "2":               ## si se le otorgo un nombre a "faena" correra, si no tirara error
            if faena is None or dias is None:
                print("Error: primero genere el plan de producción.") ## si es que no se le fue otorgado valor al "None"
            else: 
                produccion_diaria = datos_de_produccion(dias)         
        elif opcion == "3":
            if produccion_diaria:
                costo_faena(produccion_diaria, costo_por_tonelada)
            else:
                print("Error: no se han ingresado los datos de la producción.")
        elif opcion == "4":
            if produccion_diaria:
                parametros_produccion(produccion_diaria)
            else:
                print("Error: no se han ingresado los datos de la producción.")
        elif opcion == "5":
            break  ## Aqui rompe el ciclo While True y finaliza el programa
        else:
            print("Opción inválida. reintente seleccionando una opción válida.") ## esto es por si no se selecciona una opcion del 1 al 5 que son las permitidas

menu_principal()

print('Programa terminado...')
print('Creador: Simon y Diego ')