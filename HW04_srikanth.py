'''python program to perform few string and mathematical operation
    author srikanth'''


import unittest
import random


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if (self.denominator < 0):   #if loop to correct if numerator of 1 number and denominator of other number are negative
            self.denominator = (self.denominator * -1) 
            self.numerator = (self.numerator *-1)
        if self.denominator == 0 :   #check if divide by zero
            raise ZeroDivisionError ("cant divide by zero")

    def simplify(self):
        a = self.numerator
        b = self.denominator
        r = 1
        while r != 0:
            r = a % b
            a, b = b, r
        self.numerator /= a
        self.denominator /= a
        print(self.numerator, "/" , self.denominator)
        #return Fraction(int(self.numerator), int(self.denominator))



def count_vowel(s1):
    ss1 = s1.lower()
    num = 0
    for char in ss1:
        if char in "aeiou":
            num=num+1
    print("there are", num, "vowels in the sentence")
    return num

def list_travel(ele, list):
    print("list is", list)
    count = len(list)
    for i in list[::-1]:
        count = count-1
        if i == ele:
            print(ele,"latest list index is", count)
            return count
    return None

def my_enumerate(seq):
    #y=list(seq)
    i=0
    for item in seq:
        print(i, item)
        i=i+1
        #input("press enter for next element")


def find_target(target, min_value, max_value, max_attempts):
    a=1
    while max_attempts >= a:
        
        r = random.randint(min_value, max_value)
        if(target == r):
            print("guessed",r,"target reached in ", a, "tries" )
            break
        elif (target != r):
            print("number guessed is", r,"trying again" )
            a=a+1
            continue
    else:
        print("target couldnt be reached in",a-1,"attempts try again" )




class Tests(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowel('helloworld'), 3)
        self.assertEqual(count_vowel('hEllO wrld'), 2)
        self.assertEqual(count_vowel('hll wrld'), 0)

    def test_list_travel(self):
        ele='abc'
        l=['a','ab','abc','abcd','e']
        self.assertEqual(list_travel(ele,l), 2)
        self.assertEqual(list_travel('e',l), 4)   
        self.assertEqual(list_travel('apple', ['orange', 'apple', 'banana','apple','grapes','jackfruit','apple']), 6)     

    def test_fraction_simplify(self):
  
        (Fraction(4,-2)).simplify() == Fraction(-2,1)
    
    #def test_my_enumerate(self):
    #    l1=list(my_enumerate("hi!"))     
    #    l2=for offset, value in enumerate("hi!"):
    #    self.assertEqual(l1==l2)

    
def main():
    #part 1 input
    print("part 1 vowel search")
    s1=input("enter your string ")
    count_vowel(s1)

    #part 2 input
    print("part 2 list travel")
    ele= input("enter the element you want to be searched: ")
    list=input("enter the list with a comma between elements: ")
    list = list.split(",")
    list_travel(ele ,list)

    #part3 input
    print("part 3 fraction simplification")
    nr= int(input("enter numerator"))
    dn= int(input("enter denominator"))
    Fraction(nr,dn).simplify()       

    #part4 input
    print("part4 string enumerate")
    seq=input("enter the input string :  ")
    my_enumerate(seq)

    #part5 input
    print("part 5 finding target value by generating random numbers")
    min_value=int(input("enter min value: "))
    max_value=int(input("enter max value: "))
    target=int(input("enter target: "))
    max_attempts=int(input("enter max attempts: "))
    if min_value > max_value:
        raise ValueError("min value cannot be greater than max value")
    if (target > max_value) and (target < min_value):
        raise ValueError("target cannot be above max value")

    find_target(target, min_value, max_value, max_attempts)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
