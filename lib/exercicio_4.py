__author__ = "mauricio"

import unittest

import mat.so

class TestExercicio2(unittest.TestCase):

    def test_fatorial(self):
        self.assertEqual( mat.so.fatorial( 5 ), 120 )

    def test_quadrado(self):
        self.assertEqual( mat.so.quadrado(4), 16 )

if __name__ == '__main__':
    unittest.main()