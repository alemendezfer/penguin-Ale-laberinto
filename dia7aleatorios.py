#uso de numeros aleatorios
#guardamos en la carpeta del repositorio
#con la extesion.py
#uso de numeros aleatorios
"""
from random import randint 
aleatorio=randint(0,20) #creamos una variable y generamos un numero aleatorio entre 0 y 20
print(aleatorio) #imprimimos el numero generado
"""
#ejercicio 
# escribir una funcion sorteo() que reciba una lista de participantes, y elegir a uno de los partcipantes aleatoriamente, y retornar esa persona elegida
#desafio: no imprimir una persona ya sorteada

from random import randint #importamos la funcion randin de libreria random
lista_de_participantes=["Ale", "Fede","Adolf", "Vero", "Lore", "Willi", "Yumi"]

#al pedo
def sorteo(lista):
    numero_participantes=len(lista)
    aleatorio=randint(0,numero_participantes-1) #creamos una variable y generamos un numero aleatorio entre 0 y 20
    for ganador in range(len(lista)):
        if ganador==aleatorio:
            win=lista[ganador]
            return win
        else:
            pass

lista_de_participantes=["Ale", "Fede","Adolf", "Vero", "Lore", "Willi", "Yumi"]  
sorteo(lista_de_participantes)

#mas corto

def sorteo2(listaa): #definimos una funcion
    numero_participantes=len(listaa) -1 
    #utilizamos len para saber la cantidad de personas y guardamos en numero_participantes para que no salga del rango
    indice=randint(0,numero_participantes) #generamos un indice aleatorio
    ganadores=listaa[indice] #generamos ganador de acuerdo al indice aleatorio generado seleccionado de la lista
    return ganadores #retornamos ganador

#creamos la lista de los participantes

lista_de_participantes=["Ale", "Fede","Adolf", "Vero", "Lore", "Willi", "Yumi"]  

#llamamos a la funcion y lo guardamos en una variable 

felicidades=sorteo2(lista_de_participantes)

print(felicidades) #imprimimos ganador


