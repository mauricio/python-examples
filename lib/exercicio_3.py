# -*- coding: utf-8 -*-

__author__ = 'mauricio-linhares'

import fileinput
import unittest
import string
import arquivos

# 3. Implementar uma função que leia um arquivo e retorne uma lista de tuplas com os dados (o separador de campo do
# arquivo é vírgula), eliminando as linhas vazias. Caso ocorra algum problema, imprima uma mensagem de aviso e encerre
# o programa.

def csv_to_list( path ):
    result = []
    for line in fileinput.input(path):
        striped = string.strip(line)
        if striped != "":
            result.append( string.split(striped, ',') )
    return result


class TestExercicio3(unittest.TestCase):

    def test_csv_to_list(self):
        result = [['joe','me','whatever'], ['mary','other','waitress'], ['john','uncle','revolutionary']]
        self.assertEqual( result, csv_to_list( "sample_file.csv" ) )

    def test_split_and_join(self):
        with open( "sample_file.csv" ) as original:
            original_content = original.read()
            files = arquivos.split( "sample_file.csv", 5 )

            arquivos.join( "my_sample_file.csv", files )

            with open( "my_sample_file.csv" ) as result:

                final_content = result.read()

                self.assertEqual( original_content, final_content )

        

if __name__ == '__main__':
    unittest.main()    