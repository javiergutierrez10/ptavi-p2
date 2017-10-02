#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

with open('fichero.csv') as fichero

for linea in fichero.readlines():
    lista = linea.split(',')

    operacion = lista[0]
    operandos = lista[1:]

    datos = calcoohija.CalculadoraHija()

    resultado = int(operandos[0])
    operandos = operandos[1:]
    
    if operacion == "suma":
        
        for suma in operandos:
            resultado = datos.plus((resultado),int(suma))
        
        print(resultado)
        
    elif operacion == "resta":
        
        for resta in operandos:
            resultado = datos.minus((resultado),int(resta))
            
        print(resultado)
        
    elif operacion == "multiplica":
        
        for multiplica in operandos:
            resultado = datos.multiplication((resultado),int(multiplica)) 
            
        print(resultado)

    elif operacion == "divide":

        for divide in operandos:
            resultado = datos.division((resultado),int(divide))
            
        print(resultado)
        
fichero.close()
