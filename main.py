
"""Programa principal para administrar los datos de 30 estudiantes."""

import funciones


def main():
    """Inicializa los datos y ejecuta el menu principal."""

    legajos = [
        23, 17, 8, 89, 77, 31, 42, 56, 64, 12,
        95, 28, 36, 71, 84, 19, 53, 62, 47, 91,
        14, 38, 69, 25, 82, 44, 58, 73, 11, 97
    ]

    nombres = [
        "Gerardo Antunez", "Graciela Bordon", "Tania Klimt",
        "Damian Antunez", "Fabrizio Naselli", "Valentin Klimt",
        "Luciano Iriarte", "Sebastian Perez", "Ariadna Burrieza",
        "Victoria", "Gustavo Fernandez", "Ailen Rodriguez",
        "Nicolas Perez", "Valentina Lopez", "Franco Diaz",
        "Milagros Castro", "Thiago Ruiz", "Martina Silva",
        "Benjamin Acosta", "Catalina Vega", "Joaquin Molina",
        "Agustina Herrera", "Santiago Medina", "Florencia Rojas",
        "Lautaro Cabrera", "Renata Suarez", "Emiliano Ortiz",
        "Micaela Navarro", "Facundo Gimenez", "Abril Morales"
    ]

    generos = [
        "M", "F", "F", "M", "M", "M", "M", "M", "F", "F",
        "M", "F", "M", "F", "M", "F", "M", "F", "M", "F",
        "M", "F", "M", "F", "M", "F", "M", "F", "M", "F"
    ]

    parcial1 = [
        9, 9, 7, 10, 7, 8, 6, 9, 5, 10,
        7, 8, 4, 9, 6, 10, 7, 8, 5, 9,
        6, 10, 8, 7, 4, 9, 6, 8, 10, 7
    ]

    parcial2 = [
        8, 9, 9, 10, 7, 7, 8, 10, 6, 9,
        8, 6, 7, 8, 9, 10, 6, 9, 8, 7,
        9, 8, 7, 10, 5, 9, 8, 7, 9, 8
    ]

    promedios = [0] * 30
    funciones.calcular_promedios(parcial1, parcial2, promedios)

    # Los datos de ejemplo ya estan cargados.
    datos_cargados = True
    opcion = 0

    while opcion != 7:
        funciones.mostrar_menu()
        entrada = input("Ingrese una opcion: ")

        if not entrada.isdigit():
            print("Error. Ingrese un numero del 1 al 7.")
            continue

        opcion = int(entrada)

        if opcion < 1 or opcion > 7:
            print("Opcion invalida. Ingrese un numero del 1 al 7.")

        elif opcion == 1:
            funciones.opcion_cargar(
                legajos, nombres, generos,
                parcial1, parcial2, promedios
            )
            datos_cargados = True

        elif opcion == 7:
            print("Programa finalizado.")

        elif not datos_cargados:
            print("Primero debe cargar los datos con la opcion 1.")

        elif opcion == 2:
            funciones.opcion_mostrar(
                legajos, nombres, generos, parcial1, parcial2
            )

        elif opcion == 3:
            funciones.opcion_promedios(nombres, promedios)

        elif opcion == 4:
            funciones.opcion_ordenar(
                legajos, nombres, generos,
                parcial1, parcial2, promedios
            )

        elif opcion == 5:
            funciones.opcion_mayor(
                legajos, nombres, generos,
                parcial1, parcial2, promedios
            )

        elif opcion == 6:
            funciones.opcion_buscar(
                legajos, nombres, generos,
                parcial1, parcial2, promedios
            )


if __name__ == "__main__":
    main()
