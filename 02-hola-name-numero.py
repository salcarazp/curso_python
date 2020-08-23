# -*- coding: utf-8 -*-
"""
Escribir un script que pregunte el nombre del usuario en la consola y un número entero e imprima 
por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""

name = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((name + "\n") * int(n))