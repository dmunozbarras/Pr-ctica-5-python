# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 8
Escriu un programa que et demani primer un nombre i després et demani nombres fins a què la
suma dels nombres introduïts coincideixi amb el nombre inicial. El programa termina escribint la
llista de nombres.
"""
limite = int(input("Introduzca un numero limite "))
suma = 0
lista=[]
while suma < limite:
    num1 = int(input("Introduzca un numero "))
    if num1 < limite and num1 <= (limite-suma):
        lista.append (int(num1))
        suma = num1 + suma

    else:
        print "Error su numero es superior al limite"


print "El limite a superar es %d :" % (limite),"La lista creada es: ", (lista)
