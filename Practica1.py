"""
Practica 1

Autor : @davisalex22


"""
# Importar archivos y lectura de archivos
import codecs
import json
archivo = codecs.open("datos.txt", "r")
lineas = archivo.readlines()

diccionario = [json.loads(l) for l in lineas]

# Encontrar todos los que han hecho mas de 3 goles

def funcion(x): return list(x.items())[1][1] > 3

print("* Jugadores mas de 3 goles:\n\n", list(filter(funcion, diccionario)))

print("------------------------------------------\n")

# Encontrar los que son del país Nigeria


def funcion1(x): return list(x.items())[0][1] == "Nigeria"

print("* Jugadores de NIGERIA:\n\n", list(filter(funcion1, diccionario)))

print("------------------------------------------\n")

# El valor mínimo y máximo de la caracteristica Height

l = list(map(lambda x: list(x.items())[2][1], diccionario))

maximo = list(filter(lambda x: list(x.items())[2][1] == max(l), diccionario))
minimo = list(filter(lambda x: list(x.items())[2][1] == min(l), diccionario))

print("* El jugador con mayor altura es: \n\n", list(maximo))
print("------------------------------------------\n")
print("* El jugador con menor altura es: \n\n", list(minimo))
