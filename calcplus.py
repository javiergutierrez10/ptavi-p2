#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija

fichero = open('fichero.csv', 'r')

linea = fichero.readline()
lista = linea.split(',')

operacion = lista[0]
operandos = lista[1:]

datos = calcoohija.CalculadoraHija()

if operacion == "suma":
    
    i = 1
    resultado = operandos[0]
    
    while i < len(operandos):
       
        resultado = datos.plus(int(resultado),int(operandos[i]))
        i = i + 1
        
    print(resultado)
    
elif operacion == "resta":
    
    i = 1
    resultado = operandos[0]

    while i < len(operandos):
        
        resultado = datos.minus(int(resultado),int(operandos[i]))
        i = i + 1
        
    print(resultado)
    
    
elif operacion == "multiplica":
    
    i = 0
    resultado = 1
    
    while i < len(operandos):
       
        resultado = datos.multiplication(int(resultado),int(operandos[i]))
        i = i + 1
        
    print(resultado)

elif operacion == "divide":

    i = 1
    resultado = operandos[0]
    
    while i < len(operandos):
       
        resultado = datos.division(int(resultado),int(operandos[i]))
        i = i + 1
        
    print(resultado)
    
fichero.close()
