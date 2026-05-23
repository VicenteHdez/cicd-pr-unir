"""
License: Apache
Organization: UNIR
codigo mejorado para leer palabras de un fichero, eliminar duplicados y ordenarlas, con manejo de errores y argumentos de línea de comandos.

"""



import argparse
import os
import sys


DEFAULT_FILENAME = "words.txt"
DEFAULT_REMOVE_DUPLICATES = False


def sort_list(items, ascending=True):
    if not isinstance(items, list):
        raise TypeError(f"No se puede ordenar un objeto de tipo {type(items)}")
    return sorted(items, reverse=not ascending)


def remove_duplicates_from_list(items):
    return list(dict.fromkeys(items))  # conserva el orden


def read_words_from_file(path):
    if not os.path.isfile(path):
        print(f"El fichero {path} no existe. Se usarán valores por defecto.")
        return ["ravenclaw", "gryffindor", "slytherin", "hufflepuff"]

    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Lee palabras de un fichero, opcionalmente elimina duplicados y las ordena."
    )
    parser.add_argument(
        "filename",
        nargs="?",
        default=DEFAULT_FILENAME,
        help="Nombre del fichero a leer"
    )
    parser.add_argument(
        "--dedup",
        action="store_true",
        help="Eliminar duplicados antes de ordenar"
    )
    return parser.parse_args()


def main():
    args = parse_arguments()

    print(f"Se leerán las palabras del fichero: {args.filename}")
    words = read_words_from_file(args.filename)

    if args.dedup:
        words = remove_duplicates_from_list(words)

    sorted_words = sort_list(words)
    print(sorted_words)


if __name__ == "__main__":
    main()
