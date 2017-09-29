#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = open('fichero.txt', 'r')

linea = fichero.readline()
lista = linea.split(',')

operacion = lista[0]
operandos = lista[1:]

datos = calcoohija.CalculadoraHija()

if operacion == "suma":

    resultado = datos.plus(int(operandos[0]),int(operandos[1]))
    
elif operacion == "resta":

    resultado = datos.minus(int(operandos[0]),int(operandos[1]))
  
elif operacion == "multiplica":

    resultado = datos.multiplication(int(operandos[0]),int(operandos[1]))
    
print(resultado)

    
fichero.close()
