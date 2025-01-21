import unittest
import EX1 as ex1
import Ex2 as ex2
import EX3 as ex3
import EX5 as ex5 

class MyTestCase(unittest.TestCase):
    def test_safe_division(self):
        with self.assertRaises(ZeroDivisionError):
            ex1.safe_division(10, 1)
    def test_convert_to_int(self):
        with self.assertRaises(ValueError):
            ex2.convert_to_int(-4.5)
    def test_read_file(self):
        ex3.read_file("flsdgùkfd\qdsfc")
    
    def test_process_input(self):
        ex5.process_input("4")
          

if __name__ == "__main__":
    unittest.main()
    