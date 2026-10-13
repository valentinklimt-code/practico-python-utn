
"""
Biblioteca de funciones para procesar los datos de estudiantes.
Se trabaja con listas paralelas de legajos, nombres, generos y notas.
"""


def validar_legajo():
    """Solicita un legajo y valida que sea un numero entero positivo."""
    while True:
        legajo = input("Ingrese el legajo: ")

        if legajo.isdigit():
            return int(legajo)

        print("Error. El legajo debe ser numerico.")


def validar_nombre():
    """Solicita apellido y nombre y valida que contenga solo letras y espacios."""
    while True:
        nombre = input("Ingrese apellido y nombre: ").strip()

        if nombre and nombre.replace(" ", "").isalpha():
            return nombre

        print("Error. Ingrese solo letras y espacios.")


def validar_genero():
    """Valida que el genero ingresado sea F, M o X."""
    while True:
        genero = input("Ingrese el genero (F/M/X): ").strip().upper()

        if genero in ("F", "M", "X"):
            return genero

        print("Error. Ingrese F, M o X.")


def validar_parcial1():
    """Valida una nota entera entre 1 y 10 para el primer parcial."""
    while True:
        nota = input("Ingrese la nota del primer parcial (1-10): ")

        if nota.isdigit() and 1 <= int(nota) <= 10:
            return int(nota)

        print("Error. Ingrese un numero entero entre 1 y 10.")


def validar_parcial2():
    """Valida una nota entera entre 1 y 10 para el segundo parcial."""
    while True:
        nota = input("Ingrese la nota del segundo parcial (1-10): ")

        if nota.isdigit() and 1 <= int(nota) <= 10:
            return int(nota)

        print("Error. Ingrese un numero entero entre 1 y 10.")


def cargar_datos(legajos, nombres, generos, parcial1, parcial2):
    """Carga los datos de los 30 estudiantes usando las validaciones."""
    for i in range(30):
        print("\nEstudiante", i + 1)
        legajos[i] = validar_legajo()
        nombres[i] = validar_nombre()
        generos[i] = validar_genero()
        parcial1[i] = validar_parcial1()
        parcial2[i] = validar_parcial2()


def mostrar_un_estudiante(
    legajos, nombres, generos, parcial1, parcial2, i, promedios=None
):
    """Muestra todos los datos de un estudiante y, si se indica, su promedio."""
    print("Legajo:", legajos[i])
    print("Apellido y nombre:", nombres[i])
    print("Genero:", generos[i])
    print("Primer parcial:", parcial1[i])
    print("Segundo parcial:", parcial2[i])

    if promedios is not None:
        print("Promedio:", format(promedios[i], ".2f"))

    print("-" * 30)


def calcular_promedios(parcial1, parcial2, promedios):
    """Calcula y guarda el promedio de los dos parciales de cada estudiante."""
    for i in range(len(parcial1)):
        promedios[i] = (parcial1[i] + parcial2[i]) / 2


def ordenar_promedios(
    legajos, nombres, generos, parcial1, parcial2, promedios, ascendente
):
    """Ordena todas las listas paralelas por promedio ASC o DESC."""
    for i in range(len(promedios) - 1):
        for j in range(i + 1, len(promedios)):
            if ascendente:
                condicion = promedios[i] > promedios[j]
            else:
                condicion = promedios[i] < promedios[j]

            if condicion:
                promedios[i], promedios[j] = promedios[j], promedios[i]
                legajos[i], legajos[j] = legajos[j], legajos[i]
                nombres[i], nombres[j] = nombres[j], nombres[i]
                generos[i], generos[j] = generos[j], generos[i]
                parcial1[i], parcial1[j] = parcial1[j], parcial1[i]
                parcial2[i], parcial2[j] = parcial2[j], parcial2[i]


def mostrar_todos(
    legajos, nombres, generos, parcial1, parcial2, promedios=None
):
    """Recorre la lista y llama a la funcion que muestra cada estudiante."""
    print("\n===== INFORME DE ESTUDIANTES =====")

    for i in range(len(legajos)):
        mostrar_un_estudiante(
            legajos, nombres, generos, parcial1, parcial2, i, promedios
        )


def mostrar_mayor_promedio(
    legajos, nombres, generos, parcial1, parcial2, promedios
):
    """Muestra todos los estudiantes que comparten el mayor promedio."""
    if len(promedios) == 0:
        print("No hay estudiantes cargados.")
        return

    mayor = max(promedios)

    print("\n===== ESTUDIANTE/S CON MAYOR PROMEDIO =====")

    for i in range(len(promedios)):
        if promedios[i] == mayor:
            mostrar_un_estudiante(
                legajos, nombres, generos, parcial1, parcial2, i, promedios
            )


def buscar_por_legajo(
    legajos, nombres, generos, parcial1, parcial2, promedios
):
    """Busca por legajo, recorre todos los registros y muestra coincidencias."""
    legajo_buscado = validar_legajo()
    encontrado = False

    for i in range(len(legajos)):
        if legajos[i] == legajo_buscado:
            mostrar_un_estudiante(
                legajos, nombres, generos, parcial1, parcial2, i, promedios
            )
            encontrado = True

    if not encontrado:
        print("No se encontro un estudiante con ese legajo.")


def mostrar_menu():
    """Muestra las opciones disponibles del programa."""
    print("\n===== MENU PRINCIPAL =====")
    print("1. Cargar datos de estudiantes")
    print("2. Mostrar todos los estudiantes")
    print("3. Mostrar promedios")
    print("4. Mostrar estudiantes ordenados por promedio DESC")
    print("5. Mostrar estudiante/s con mayor promedio")
    print("6. Buscar estudiante por legajo")
    print("7. Salir")


def opcion_cargar(legajos, nombres, generos, parcial1, parcial2, promedios):
    """Ejecuta la opcion 1: carga los datos y calcula los promedios."""
    cargar_datos(legajos, nombres, generos, parcial1, parcial2)
    calcular_promedios(parcial1, parcial2, promedios)
    print("Datos cargados correctamente.")


def opcion_mostrar(legajos, nombres, generos, parcial1, parcial2):
    """Ejecuta la opcion 2: muestra todos los estudiantes."""
    mostrar_todos(legajos, nombres, generos, parcial1, parcial2)


def opcion_promedios(nombres, promedios):
    """Ejecuta la opcion 3: muestra los promedios."""
    print("\n===== PROMEDIOS DE ESTUDIANTES =====")

    for i in range(len(promedios)):
        print(nombres[i], ":", format(promedios[i], ".2f"))


def opcion_ordenar(
    legajos, nombres, generos, parcial1, parcial2, promedios
):
    """Ejecuta la opcion 4: ordena y muestra todos los datos en DESC."""
    ordenar_promedios(
        legajos, nombres, generos, parcial1, parcial2, promedios, False
    )
    mostrar_todos(
        legajos, nombres, generos, parcial1, parcial2, promedios
    )


def opcion_mayor(
    legajos, nombres, generos, parcial1, parcial2, promedios
):
    """Ejecuta la opcion 5: muestra al estudiante con mayor promedio."""
    mostrar_mayor_promedio(
        legajos, nombres, generos, parcial1, parcial2, promedios
    )


def opcion_buscar(
    legajos, nombres, generos, parcial1, parcial2, promedios
):
    """Ejecuta la opcion 6: busca estudiantes por legajo."""
    buscar_por_legajo(
        legajos, nombres, generos, parcial1, parcial2, promedios
    )
