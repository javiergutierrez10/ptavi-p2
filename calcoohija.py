#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

class Calculadora():

    def plus(self, op1,op2):
    
        return op1 + op2


    def minus(self,op1, op2):

        return op1 - op2
        
class CalculadoraHija(Calculadora):
        
    def multiplication(self, op1,op2):
    
        return op1 * op2


    def division(self,op1, op2):
        
        try:
            return op1 / op2
        except ZeroDivisionError:
            sys.exit("Division by zero is not allowed")

if __name__ == "__main__":
    
    datos = CalculadoraHija()
    
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = datos.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = datos.minus(operando1, operando2)
    elif sys.argv[2] == "multiplica":
        result = datos.multiplication(operando1, operando2)
    elif sys.argv[2] == "divide":
        result = datos.division(operando1, operando2)
    else:
        sys.exit('Operación sólo puede ser sumar, restar, multiplicar y dividir.')

    print(result)
