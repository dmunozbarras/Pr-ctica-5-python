# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 5
Escriu un programa que te demani dos nombres cada vegada més grans i els guardi en una llista.
Per a terminar d'escriure els nombres, escriu un nombre que no sigui major a l'anterior. El
programa termina escribint la llista de nombres.
"""
num1 = int(input("Escriba un numero: "))
num2 = num1
lista=[]
while num1 >= num2:
    num2 = num1
    lista.append (int(num1))
    num1 = int(input("Introduzca otro numero: "))

else:
    print "Los numeros que a escrito son:", (lista)
