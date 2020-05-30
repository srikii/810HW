'''python program to perform basic mathematical operations on fractions
    author : srikanth'''

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator <= 0 :   #check if divide by zero
            raise ValueError ("denominator = 0 , cant dividie by zero")

    
    def __str__(self): #string to display fraction   
        return str(self.numerator) + '/' + str(self.denominator)

    def plus(self, a): #addition 
        resnum = (self.numerator * a.denominator) + (self.denominator * a.numerator)
        resden = (self.denominator * a.denominator)
        return Fraction(float(resnum), float(resden))
    
    def minus(self, a):  #subtraction
        resnum = (self.numerator * a.denominator) - (self.denominator * a.numerator)
        resden = (self.denominator * a.denominator)
        return Fraction(float(resnum), float(resden))
    
    def times(self, a):   #multiplication
        resnum = (self.numerator * a.numerator)
        resden = (self.denominator * a.denominator)
        return Fraction(float(resnum), float(resden))

    def divide(self,a): #division 
        resnum = (self.numerator * a.denominator)
        resden = (self.denominator * a.numerator)
        return Fraction(float(resnum), float(resden))   
    
    def equal(self,a):  #equal
        if (self.numerator * a.denominator) == (self.denominator * a.numerator):
            return True
        else:
            return False

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
    opr = ["+", "-", "*", "/", "="]
    op = input("Operation (+, -, *, /, =): ")
    if op not in opr:           #check if the operator is valid or not
        print("invalid operator")
        return
    num2 = get_number("Fraction 2 numerator: ")
    den2 = get_number("Fraction 2 denominator: ")
   

    f1 = Fraction(num1, den1)
    f2 = Fraction(num2, den2)
    

    if op == "+":
        print(f1, '+', f2, '=', f1.plus(f2))
    elif op == "-":
        print(f1, '-', f2, '=', f1.minus(f2))
    elif op == "*":
        print(f1, '*', f2, '=', f1.times(f2))
    elif op=="/":
        print(f1, '/', f2, '=', f1.divide(f2))
    elif op == "=":
        print(f1, '=', f2, f1.equal(f2))
    #apply f1 operator f2 and return result

if __name__ == '__main__':
    test()
    main()