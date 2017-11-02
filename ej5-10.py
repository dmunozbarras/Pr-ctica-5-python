# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 10
Escriu un programa que et demani els noms i notes d'alumnes. Si escrius una nota
fora de l'interval de 0 a 10, el programa entendrà que no vols introduir més notes
d'aquest alumne. Si no escrius el nom, el programa entendrà que no vols introduir
més alumnes. Nota: La llista en la que es guarden els noms i notes és
[ [nom1, nota1, nota2, etc], [nom2, nota1, nota2, etc],[nom3, nota1, nota2, etc], etc] """
nom= 0
lista= []
notas= []
while nom <> "":
    nom = raw_input ("Escribe un nombre ")
    if nom <> "":
        lista.append(nom)
        nota = input("Escriba una nota: ")
        while nota <= 10 and nota > 0:
            lista.append(nota)
            nota = input("Escriba otra nota: ")
        notas.append(lista)
        lista=[]
print "Las notas son"
for i in notas:
    print (i)
