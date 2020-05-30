'''python program to perform mathematical operations and compare  the fractions
    author : srikanth'''

import unittest

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if (self.denominator < 0):   #if loop to correct if numerator of 1 number and denominator of other number are negative
            self.denominator = (self.denominator * -1) 
            self.numerator = (self.numerator *-1)
        if self.denominator == 0 :   #check if divide by zero
            raise ZeroDivisionError ("cant divide by zero")
    
    def __str__(self): #string to display fraction
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, a): #addition 
        resnum = (self.numerator * a.denominator) + (self.denominator * a.numerator)
        resden = (self.denominator * a.denominator)
        return Fraction(float(resnum), float(resden))
    
    def __sub__(self, a):  #subtraction
        resnum = (self.numerator * a.denominator) - (self.denominator * a.numerator)
        resden = (self.denominator * a.denominator)
        return Fraction(float(resnum), float(resden))
    
    def __mul__(self, a):   #multiplication
        resnum = (self.numerator * a.numerator)
        resden = (self.denominator * a.denominator)
        return Fraction(float(resnum), float(resden))

    def __truediv__(self,a): #division 
        resnum = (self.numerator * a.denominator)
        resden = (self.denominator * a.numerator)
        return Fraction(float(resnum), float(resden))   
    
    def __eq__(self, a):  #equal
        if (self.numerator * a.denominator) == (self.denominator * a.numerator):
            return True
        else:
            return False

    def __ne__(self, a): #not equal
        if(self.numerator * a.denominator) != (self.denominator * a.numerator):
            return True
        else:
            return False

    def __lt__(self, a): #less than
        if(self.numerator * a.denominator) < (self.denominator * a.numerator):
            return True
        else:
            return False

    def __le__(self, a): #less than or equal to
        if(self.numerator * a.denominator) <= (self.denominator * a.numerator):
            return True
        else:
            return False

    def __gt__(self, a): #greater than
        if(self.numerator * a.denominator) > (self.denominator * a.numerator):
            return True
        else:
            return False

    def __ge__(self, a): #greater than or equal to
        if(self.numerator * a.denominator) >= (self.denominator * a.numerator):
            return True
        else:
            return False

class FractionTest(unittest.TestCase): #class for unit testing.
    
    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f = Fraction(3, 4)
        self.assertEqual(f.numerator, 3)
        self.assertEqual(f.denominator, 4)
        
    def test_str(self): #str test
        """ verify that __str__() works properly """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')
        
    def test_equal(self):
        """test fraction equality"""
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f2)
        self.assertTrue(f1 == f3)
        self.assertTrue(f2 ==f3)
        self.assertFalse(f1 == Fraction(3, 5))
    
    #def test_divideByZero(self):
    #    f1 = Fraction(3, 0)
    #    self.assertRaises(ZeroDivisionError, f1)


    def test_divideByZero1(self):
        """test for dividing by zero error"""
        self.assertRaises(ZeroDivisionError, lambda: Fraction(6, 0) )       

    def test_plus(self):
        """ test fraction addition"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 + f1) == Fraction(6, 4))
        self.assertTrue((f1 + f2) == Fraction(5, 4))
        self.assertTrue((f1 + f3) == Fraction(13, 12))
    
    def test_minus(self):
        """test fraction subtraction"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        self.assertTrue((f1 - f2) == Fraction(1, 4))
    
    def test_times(self):
        """test fraction multiplication"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        self.assertTrue((f1 * f2) == Fraction(3, 8))

    def test_div(self):
        """test fraction division"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        self.assertTrue((f1 / f2) == Fraction(3, 2))
    
    def test_notequal(self):
        """test fraction not equal"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(2, 4)
        self.assertTrue(f1 != f2)
        self.assertFalse(f2 != f3)
        
    def test_greater(self):
        """test fraction greater"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(2, 4)
        self.assertTrue(f1 > f2)
        self.assertFalse(f2 > f3)    
        self.assertTrue(Fraction(1, -3) > Fraction(-1, 2))

    def test_greater_or_equal(self):
        """test fraction greater than or equal"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(2, 4)
        self.assertTrue(f1 >= f2)
        self.assertTrue(f2 >= f3)
        self.assertFalse(f3 >= f1)
        self.assertTrue(Fraction(1, -3) >= Fraction(-1, 2)) 
        

    def test_lesser(self):
        """test fraction lesser than"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(2, 4)
        self.assertTrue(f2 < f1)
        self.assertFalse(f2 < f3)
        self.assertTrue(f3 < f1)
        self.assertTrue(Fraction(-1, 2) < Fraction(1, -3)) 


    def test_lesser_or_equal(self):
        """test fraction lesserthan or equal"""
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(2, 4)
        self.assertTrue(f2 <= f1)
        self.assertTrue(f3 <= f2)
        self.assertFalse(f1 <= f3)
        self.assertTrue(Fraction(-1, 2) <= Fraction(1, -3)) 

        
def get_number(prompt): #input is passed is checked here if its number or not.
    while True:
        inp = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print('Error:', inp, 'is not a number. Please try again...')


def main():    
    print('Welcome to the fraction calculator!')
    num1 = get_number("Fraction 1 numerator: ")
    den1 = get_number("Fraction 1 denominator: ")
    opr = ["+", "-", "*", "/", "=", "!=", "<", "<=", ">", ">="]
    op = input("Operations +, -, *, /, = , !=, <, <=, >, >=  ")
    if op not in opr:           #check if the operator is valid or not
        print("invalid operator")
        return
    num2 = get_number("Fraction 2 numerator: ")
    den2 = get_number("Fraction 2 denominator: ")
   

    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)
    

    if op == "+":
        print(f1, '+', f2, '=', f1 + f2)
    elif op == "-":
        print(f1, '-', f2, '=', f1 - f2)
    elif op == "*":
        print(f1, '*', f2, '=', f1 * f2)
    elif op=="/":
        print(f1, '/', f2, '=', f1 / f2)
    elif op == "=":
        print(f1, '=', f2, (f1 == f2))
    elif op == "!=":
        print(f1, '!=', f2, (f1 != f2))
    elif op == "<":
        print(f1, '<', f2, (f1 < f2))
    elif op == "<=":
        print(f1, '<=', f2, (f1 <= f2))
    elif op == ">":
        print(f1, '>', f2, (f1 > f2)) 
    elif op == ">=":
        print(f1, '>=', f2, (f1 >= f2))
       

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
        
    