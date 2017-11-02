# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 1
Escriu un programa que te demani paraules i les guardi en una llista. Per a terminar d'introduir
paraules, simplement pitja Enter. El programa termina escribint la llista de paraules.  """

a=raw_input("Escribe una palabra ")
lista= []
while a <> "":
    lista.append(a)
    a=raw_input("Escribe otra palabra ")
print "Las palabras que a escrito son:", lista
