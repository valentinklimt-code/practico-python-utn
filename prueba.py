
"""Prueba de las funciones con cinco estudiantes de ejemplo."""

import funciones


def probar_funciones():
    """Comprueba el calculo de promedios y el ordenamiento."""

    legajos = [23, 17, 8, 89, 77]
    nombres = [
        "Gerardo Antunez",
        "Graciela Bordon",
        "Tania Klimt",
        "Damian Antunez",
        "Fabrizio Naselli"
    ]
    generos = ["M", "F", "F", "M", "M"]
    parcial1 = [9, 9, 7, 10, 7]
    parcial2 = [8, 9, 9, 10, 7]
    promedios = [0] * len(legajos)

    funciones.calcular_promedios(parcial1, parcial2, promedios)

    print("===== PROMEDIOS =====")
    for i in range(len(promedios)):
        print(nombres[i], ":", format(promedios[i], ".2f"))

    funciones.ordenar_promedios(
        legajos, nombres, generos,
        parcial1, parcial2, promedios, False
    )

    print("\n===== PROMEDIOS ORDENADOS DE MAYOR A MENOR =====")
    funciones.mostrar_todos(
        legajos, nombres, generos,
        parcial1, parcial2, promedios
    )

    funciones.mostrar_mayor_promedio(
        legajos, nombres, generos,
        parcial1, parcial2, promedios
    )


if __name__ == "__main__":
    probar_funciones()
