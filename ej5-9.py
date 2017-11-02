# -*- coding: cp1252 -*-
"""DAVID MUÑOZ BARRAS - 1º DAW - PRACTICA 5 - EJERCICIO 9
Escriu un programa que et demani noms de persones i els seus números de telèfon. Per a
terminar de escriure nombres i numeros s'ha de pulsar Intro quan et demani el nom. El programa
termina escribint noms i números de telèfon. Nota: La llista en la que es guarden els noms i
números de telèfon és [ [nom1, telef1], [nom2, telef2], [nom3, telef3], etc]
"""

nom=raw_input("Escribe un nombre ")
telef=raw_input("Escriba un numero de telefono ")
lista= []
guia=[]
while nom <> "":
    lista.append(nom)
    lista.append(int(telef))
    guia.append(lista)
    lista=[]
    nom=raw_input("Escribe otro nombre ")
    telef=raw_input("Escribe otro telefono ")
print "Los nombres y telefonos son: "

for i in guia:
    print (i)
