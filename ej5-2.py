# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 2
Escriu un programa que te demani nombres i els guardi en una llista. Per a terminar d'introduir
nombres, simplement pitja Enter. El programa termina escrivint la llista de nombres.
  """
num1 = raw_input("Escribe un numero: ")
lista= []
while num1 <> "":
    lista.append (int(num1))
    num1=raw_input("Escribe otro numero ")
print "Los numeros que a escrito son:", lista
