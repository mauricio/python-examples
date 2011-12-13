# -*- coding: utf-8 -*-
__author__ = 'mauricio-linhares'

import unittest
import math

# implementar duas funções, converter de celcius pra fahrenheit e de fahrenheit pra celcius

def celcius_to_fahrenheit( celcius ):
    return ( 9 * celcius ) / 5 + 32

def fahrenheit_to_celcius( fah):
    return (( fah - 32 ) * 5) / 9

# implementar uma função que receba uma lista de listas e transforme em uma única lista

def flatten( *listas ):
    resultado = []
    for lista in listas:
        for item in lista:
            resultado.append( item )
    return resultado

def formula_de_bhaskara( a, b = 0, c = 0 ):
    return (-b + math.sqrt( ( (b * b) - ( 4 * a * c ) ) ) ) / ( 2 * a )

class TestExercicio2(unittest.TestCase):

    def test_flatten(self):
        values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual( flatten( [1, 2, 3, 4], [5, 6, 7, 8], [9,10] ), values )

    def test_celcius_to_fahrenheit(self):
        self.assertEqual( celcius_to_fahrenheit(10), 50 )

    def test_fahrenheit_to_celcius(self):
        self.assertEqual( fahrenheit_to_celcius(68), 20 )

    def test_fomula_de_bhaskara(self):
        self.assertEqual( formula_de_bhaskara(1, -4), 4 )
        

if __name__ == '__main__':
    unittest.main()