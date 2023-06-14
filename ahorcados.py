# limpieza
import os
import sys
# juego
import random
import openpyxl

# variables, excel
book = openpyxl.load_workbook(r"C:\Users\saral\PycharmProjects\pythonProject\Programas "
                              r"noobs\ahorcados_game\palabras_ahocados.xlsx")
sheet = book.active
palabras_lista = sheet["A"]

# variables, juego
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", "l"]
espacio = "-----------"

# variables pa limpar despues
letras_correctas = []
letras_incorrectas = []
palabra = ""
intentos = 0

# variables de estadistica
partidas_ganadas = 0
partidas_perdidas = 0


# funciones de limpieza de consola


def instant_clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def inp_clear():
    input("Presione ENTER para continuar\n>>> ")
    instant_clear()


# mayor pulcritud


def intentar_letra_base(text):
    global abecedario, espacio, letras_correctas, letras_incorrectas

    while True:
        valor = str(input(text)).lower()
        if valor not in abecedario:
            print(f"{espacio}\n Lo siento! Usted no coloco una letra!\nIntente de nuevo")
        elif valor in (letras_incorrectas or letras_correctas):
            print(f"{espacio}\n Lo siento! Esa letra ya fue utilizada\nIntente de nuevo")
        else:
            return valor


# Evitar errores con el input, usar siempre al necesitar int
def anti_error_menu(text):
    global espacio
    while True:
        try:
            valor = int(input(text))
            if valor < 3:
                return valor
            else:
                print("Lo siento! Usted no coloco una de las opciones anteriores")
        except ValueError:
            print(f"{espacio}\n Lo siento! Usted coloco un valor el cual no es un numero")


# funciones ctrl c ctrl v overflow
def find(letra):
    global palabra
    return [i for i, ltr in enumerate(palabra) if ltr == letra]


def replace_at(word, indice, letra):
    return word[:indice] + letra + word[indice + 1:]


def visuales(fase):
    phase_6 = ("      _______\n"
               "     |/      |\n"
               "     |      (_)\n"
               "     |      \|/\n"
               "     |       |\n"
               "     |      / \ \n"
               "     |\n"
               " ____|___\n")
    phase_5 = ("      _______\n"
               "     |/      |\n"
               "     |      (_)\n"
               "     |      \|/\n"
               "     |       |\n"
               "     |      /\n"
               "     |\n"
               " ____|___\n")
    phase_4 = ("      _______\n"
               "     |/      |\n"
               "     |      (_)\n"
               "     |      \|/\n"
               "     |       |\n"
               "     |\n"
               "     |\n"
               " ____|___\n")
    phase_3 = ("      _______\n"
               "     |/      |\n"
               "     |      (_)\n"
               "     |      \|\n"
               "     |       |\n"
               "     |\n"
               "     |\n"
               " ____|___\n")
    phase_2 = ("      _______\n"
               "     |/      |\n"
               "     |      (_)\n"
               "     |       |\n"
               "     |       |\n"
               "     |\n"
               "     |\n"
               " ____|___\n")
    phase_1 = ("      _______\n"
               "     |/      |\n"
               "     |      (_)\n"
               "     |\n"
               "     |\n"
               "     |\n"
               "     |\n"
               " ____|___\n")
    phase_0 = ("      _______\n"
               "     |/      |\n"
               "     |\n"
               "     |\n"
               "     |\n"
               "     |\n"
               "     |\n"
               " ____|___\n")
    if fase == 0:
        print(phase_0)
    elif fase == 1:
        print(phase_1)
    elif fase == 2:
        print(phase_2)
    elif fase == 3:
        print(phase_3)
    elif fase == 4:
        print(phase_4)
    elif fase == 5:
        print(phase_5)
    elif fase == 6:
        print(phase_6)
    else:
        print("error")
        sys.exit()


# USAR ESTO SI O SI
def lista_creator():
    global palabras_lista
    lista = []
    for word in palabras_lista:
        lista.append(word.value)
    return lista


def generador_palabra():
    lista = lista_creator()
    return random.choice(lista)


def limpiador_variables_nueva_partida():
    global letras_correctas, letras_incorrectas, intentos, palabra
    intentos = 0
    letras_incorrectas.clear()
    letras_correctas.clear()
    palabra = generador_palabra()


def dibujar_lineas_intern():
    global palabra

    cantidad_letras = len(palabra)
    resultado = "_ " * cantidad_letras
    return resultado[:-1]


def posicion_letras():
    global letras_correctas, palabra

    dibujo = dibujar_lineas_intern()
    posiciones_letra = []
    for letra in letras_correctas:
        posiciones_letra.clear()
        posiciones_letra = find(letra)
        for indice in posiciones_letra:
            indice = indice * 2
            dibujo = replace_at(dibujo, indice, letra)
    return dibujo


def probar_letra():
    global letras_incorrectas, letras_correctas, palabra, intentos

    intento_letra = intentar_letra_base("\nIngrese una letra: \n>>> ")
    instant_clear()
    if intento_letra in palabra:
        letras_correctas.append(intento_letra)
    else:
        letras_incorrectas.append(intento_letra)
        intentos += 1
    return verificador_ganaste()


def verificador_ganaste():
    global letras_correctas, palabra, partidas_ganadas, partidas_perdidas

    walltext_youlose = " █████ █████                        ████\n" \
                       "░░███ ░░███                        ░░███\n" \
                       " ░░███ ███    ██████  █████ ████    ░███   ██████   █████   ██████\n" \
                       "  ░░█████    ███░░███░░███ ░███     ░███  ███░░███ ███░░   ███░░███\n" \
                       "   ░░███    ░███ ░███ ░███ ░███     ░███ ░███ ░███░░█████ ░███████\n" \
                       "    ░███    ░███ ░███ ░███ ░███     ░███ ░███ ░███ ░░░░███░███░░░\n" \
                       "    █████   ░░██████  ░░████████    █████░░██████  ██████ ░░██████\n" \
                       "   ░░░░░     ░░░░░░    ░░░░░░░░    ░░░░░  ░░░░░░  ░░░░░░   ░░░░░░\n"
    walltext_youwin = "____    ____  ______    __    __     ____    __    ____  __  .__   __.\n" \
                      "\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / |  | |  \ |  |\n" \
                      " \   \/   / |  |  |  | |  |  |  |     \   \/    \/   /  |  | |   \|  |\n" \
                      "  \_    _/  |  |  |  | |  |  |  |      \            /   |  | |  . `  |\n" \
                      "    |  |    |  `--'  | |  `--'  |       \    /\    /    |  | |  |\   |\n" \
                      "    |__|     \______/   \______/         \__/  \__/     |__| |__| \__|"
    verdadero_o_falso = True
    if intentos > 5:
        visuales(intentos)
        print(posicion_letras())
        print(f"{walltext_youlose}\n\n\nLa palabra era {palabra}\n")
        partidas_perdidas += 1
        inp_clear()
        return menu()
    for letra in palabra:
        if letra not in letras_correctas:
            verdadero_o_falso = False
    if verdadero_o_falso:
        visuales(intentos)
        print(posicion_letras())
        print(f"{walltext_youwin}\n\n")
        partidas_ganadas += 1
        inp_clear()
        return menu()
        # ignorar cuando no se gana o pierde


def mostrar_letras_ya_usadas():
    global letras_incorrectas

    valor = "Letras usadas:  "
    for letras in letras_incorrectas:
        valor = valor + f"{letras}, "
    return valor[:-2]


def juego():
    global palabra, partidas_perdidas, partidas_ganadas, intentos

    limpiador_variables_nueva_partida()
    while True:
        probar_letra()
        visuales(intentos)
        print(posicion_letras())
        print(mostrar_letras_ya_usadas())
        print(f"Intentos restantes: {6 - intentos}")


def estadisticas():
    global partidas_ganadas, partidas_perdidas

    print("Tus estadisticas:")
    print(f"  Partidas ganadas: {partidas_ganadas}\n  Partidas perdidas {partidas_perdidas}")
    inp_clear()
    return menu()


def selector(decision):
    if decision == 0:
        instant_clear()
        return juego()
    elif decision == 1:
        instant_clear()
        estadisticas()
    else:
        print("Adios!")
        sys.exit()


def menu():
    instant_clear()
    decision = anti_error_menu("Que desa hacer?\n  Jugar: 0\n  Estadisticas: 1\n  Salir: 2\n>>> ")
    selector(decision)


menu()
