#juego de adivinar el numero, todos juntos adivinar un numero generado aleatoriamente, ir introduciendo el dato a adivinar

from random import randint
generado=randint(0,10) #generamos el numero aleatorio
print(generado) #trampa
condicion=True
intento=10
while condicion:
    if intento>0:
        numero=input("Dame un numero del 0 al 10: ")
        intento=intento-1 #intento +-1
        if generado==int(numero): #compramos el numero introduccion
            print("ganaste una anvotgesa que Lore paga")
            condicion= False
        else:
            print("El perdedor compra pizza a Lore")
            print("Te quedan", intento, "intentos")
    else:
        condicion=False
        print("perdiste")



#se puede mas corto