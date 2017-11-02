# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 3
Escriu un programa que demani notes i les guardi en una llista. Per a terminar d'introduir notes,
escriu una nota que no estigui entre 0 i 10. El programa termina escrivint la llista de notes.
"""

nota = input("Escriba una nota: ")
lista= []
while nota <= 10 and nota > 0:
    lista.append(float(nota))
    nota = input("Escriba otra nota: ")
print "Sus notas son", lista
