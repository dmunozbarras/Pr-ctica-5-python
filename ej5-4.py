# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 4
Escriu un programa que te demani dos nombres, de manera que el segon sigui major que el
primer. El programa termina escrivint els dos nombre tal i com es demana.
"""
num1 = int(input("Escriba un numero: "))
num2 = int(input("Escriba un numero mayor que %d: " % (num1)))
while num1 >= num2:
    num2 = int(input("%d no es mayor que %d vuelva a escribir otro numero: " % (num2, num1)))
else:
    print "Los numeros que a introducido son %d y %d " % (num1, num2)
