import unittest
from io import StringIO
import sys
from unittest.mock import patch
from patterns import *

class MyTestCase(unittest.TestCase):

    def test_1_shape(self):
           #Mocking to test if all lower cases are returned
        sys.stdin = StringIO("TriAngLe\n")
        self.assertEqual(get_shape(), "triangle")

        sys.stdin = StringIO("SquAre\n")
        self.assertEqual(get_shape(), "square")

        sys.stdin = StringIO("PyRamiD\n")
        self.assertEqual(get_shape(), "pyramid")

    

    # Test if get_shape only returns numbers below 80 only
    @patch('builtins.input', side_effect = ["85","70", "100"])
    def test_get_height(self,mock_input):
        self.assertEqual(get_height(),70)


    @patch('builtins.input', side_effect=['abc', 'xyz', '@', '/'])
    def test_get_height(self, mock_input):
        with self.assertRaises(ValueError):
            get_height()

    def test_4_square(self):
        pass

    def test_5_square(self):
        
        pass

    def test_6_triangle(self):
        
        pass

    def test_7_triangle(self):
        
        pass

    def test_8_triangle(self):
        
        pass
    def test_9_triangle(self):
        
        pass

    def test_10_triangle_multiplication(self):
        
        pass

    def test_11_triangle_multiplication(self):
        
        pass


    def test_12_pyramid(self):
        
        pass

    def test_13_pyramid(self):
        
        pass

    def test_14_primes(self):
        # Test Case for prime numbers
        self.assertTrue(draw_triangle_prime(2))
        self.assertTrue(draw_triangle_prime(47))
        self.assertTrue(draw_triangle_prime(193))

        # Test Case for non-prime numbers
        self.assertFalse(draw_triangle_prime(1))
        self.assertFalse(draw_triangle_prime(60))
        self.assertFalse(draw_triangle_prime(200))
        
        
    @patch('sys.stdout', new_callable=StringIO)
    def test_15_prime(self, mock_stdout):
        draw_triangle_prime(3)
        output = mock_stdout.getvalue()
        expected_output = "2 \n3 5 \n7 11 13 \n"
        self.assertEqual(output, expected_output)
        

    def test_tower_of_hanoi_3_disks(self):
        """
        *This function tests how the rings move from one pole to the next.
        it uses an instance of n=3 to check if the poles are ordered from biggest pole to
        smallest pole. 
        """
        n = 3
        source_peg = "A"
        auxiliary_peg = "B"
        target_peg = "C"

        moves = tower_of_hanoi(n, source_peg, auxiliary_peg, target_peg)

        expected_moves = [
            ("A", "C"),
            ("A", "B"),
            ("C", "B"),
            ("A", "C"),
            ("B", "A"),
            ("B", "C"),
            ("A", "C"),
        ]

        self.assertEqual(moves, expected_moves)  
if __name__ == '__main__':
    unittest.main()