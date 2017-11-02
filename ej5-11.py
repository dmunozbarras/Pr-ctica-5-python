#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 11
Escriu un programa per a jugar a endivinar un nombre (l'ordinador “pensa” el
 nombre i l'usuari l'ha d'endevinar). El programa comença demanant entre què
 nombres està el nombre a endevinar, s'”inventa” un nombre a l'atzar i després
 l'usuari va probant valors i el programa va decidint si són massa grans o petits
"""
import random
print 'Bienvenido'
num=0
r=random.randrange(0,100)

while num <> r:
    num=input("Adivina el numero entre 0 y 100: ")

    if num > r:
        print "Ingrese un numero mas pequeno"
    if num < r:
        print "Ingrese un numero mas grande"

print "Lo acertaste el numero era %d" % (num)
