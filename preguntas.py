"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def load_data(name_file):
    with open(name_file, "r") as file:
        data = file.readlines()

    data = [line.replace("\n", "") for line in data]
    data = [line.split("\t") for line in data]
    return data


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = load_data("data.csv")

    val = 0
    for line in data:
        val += int(line[1])
    val
    return val


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = load_data("data.csv")

    letters = sorted(list(set([line[0] for line in data])))
    dict_count = {letter: 0 for letter in letters}
    for line in data:
        letter = line[0]
        dict_count[letter] = dict_count.get(letter, 0) + 1
    list_count = [(k, v) for k, v in dict_count.items()]

    return list_count


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = load_data("data.csv")

    letters = sorted(list(set([line[0] for line in data])))
    dict_count = {letter: 0 for letter in letters}
    for line in data:
        letter = line[0]
        val = int(line[1])
        dict_count[letter] = dict_count.get(letter, 0) + val
    list_count = [(k, v) for k, v in dict_count.items()]
    return list_count


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = load_data("data.csv")
    dict_count = {}
    for line in data:
        month = line[2].split("-")[1]
        dict_count[month] = dict_count.get(month, 0) + 1
    list_count = sorted([(k, v) for k, v in dict_count.items()])
    return list_count


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = load_data("data.csv")

    letters = sorted(list(set([line[0] for line in data])))
    dict_count = {letter: [0, 10] for letter in letters}
    for line in data:
        letter = line[0]
        val = int(line[1])
        max_, min_ = dict_count[letter]
        if val > max_:
            dict_count[letter][0] = val
        if val < min_:
            dict_count[letter][1] = val

    list_count = [(k, *tuple(v)) for k, v in dict_count.items()]
    return list_count


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = load_data("data.csv")

    dict_count = {}
    for line in data:
        dict_ = {
            string.split(":")[0]: string.split(":")[1] for string in line[4].split(",")
        }
        for k, v in dict_.items():
            v = int(v)
            if k in dict_count:
                min_, max_ = dict_count[k]
                if v > max_:
                    dict_count[k][1] = v
                if v < min_:
                    dict_count[k][0] = v
            else:
                dict_count[k] = [v, v]
    list_count = sorted([(k, *tuple(v)) for k, v in dict_count.items()])
    return list_count


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = load_data("data.csv")

    dict_count = {}
    for line in data:
        letter = line[0]
        val = int(line[1])

        if val in dict_count:
            dict_count[val].append(letter)
        else:
            dict_count[val] = [letter]
    list_count = sorted([(k, v) for k, v in dict_count.items()])

    return list_count


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    list_count = pregunta_07()

    return [(t[0], sorted(list(dict.fromkeys(t[1])))) for t in list_count]


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    data = load_data("data.csv")

    dict_count = {}
    for line in data:
        dict_ = {
            string.split(":")[0]: string.split(":")[1] for string in line[4].split(",")
        }
        for k, v in dict_.items():
            dict_count[k] = dict_count.get(k, 0) + 1
    dict_count = {k: v for k, v in sorted(dict_count.items(), key=lambda item: item[0])}
    return dict_count


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = load_data("data.csv")

    letters = sorted(list(set([line[0] for line in data])))

    list_ = []
    for line in data:
        letter = line[0]
        elements_4 = len(line[3].split(","))
        elements_5 = len(
            {
                string.split(":")[0]: string.split(":")[1]
                for string in line[4].split(",")
            }
        )
        list_.append((letter, elements_4, elements_5))
    return list_


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = load_data("data.csv")

    dict_count = {}
    for line in data:
        letters = line[3].split(",")
        val = int(line[1])
        for letter in letters:
            dict_count[letter] = dict_count.get(letter, 0) + val
    dict_count = {k: v for k, v in sorted(dict_count.items(), key=lambda item: item[0])}

    return dict_count


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    data = load_data("data.csv")

    dict_count = {}
    for line in data:
        letter = line[0]
        dict_ = {
            string.split(":")[0]: string.split(":")[1] for string in line[4].split(",")
        }
        sum_vals = sum([int(v) for v in dict_.values()])

        dict_count[letter] = dict_count.get(letter, 0) + sum_vals
    dict_count = {k: v for k, v in sorted(dict_count.items(), key=lambda item: item[0])}
    return dict_count
