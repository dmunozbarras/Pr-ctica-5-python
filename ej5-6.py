# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 6
Escriu un programa que demani primer dos nombres (màxim i mínim) i que després te demani 2
nombres situats entre ells. Per a terminar d'escriure nombres, escriu un nombre que no sigui
comprès entre els dos valors inicials. El programa termina escribint la llista de nombres.
"""
num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba un numero mayor que %d: " % (num1)))
lista=[]
while num1 >= num2:
    num2 = int(input("%d no es mayor que %d vuelva a escribir otro numero: " % (num2, num1)))
else:
    num3 = int(input("Escriba un numero entre  %d y %d " % (num1, num2)))
    while num3 > num1 and num3 < num2:
        lista.append (int(num3))
        num3 = int(input("Escriba otro numero entre  %d y %d " % (num1, num2)))
print "Los numeros entre %d y %d son:" % (num1,num2), (lista)
