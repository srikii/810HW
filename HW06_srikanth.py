"""python program to perform some list comprehension operations
    autor : srikanth"""

import unittest

'''class Btree:
    def __init__(self,value):
        self.value=[None, value, None] 

    def find(self, value):
        if self.value[1] is not None:
            print("comparing",value,self.value[1])
            if value == self.value[1]:
                return True
            elif value<self.value[1]:
                return find(self.value[0])
            else:
                return find(self.value[2])'''


def remove_vowels(str):  # function to check password
    s = list(str)
    val = []
    for item in s:
        if item not in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            val.append(item)
    strng = ''
    for i in val:
        strng += i
    return strng


def check_pwd(pwd):  # function to check password
    s2 = list(pwd)
    upper = 0
    lower = 0
    digit = 0
    for item in s2:
        if item.islower() is True:
            lower += 1
        elif item.isupper() is True:
            upper += 1
        elif item.isdigit() is True:
            digit += 1
    if lower and upper and digit > 0:
        return "valid password"
    else:
        return "invalid password"


def insertion_sort(l):  # function for insertion sort
    sorted_list = []
    for i in l:
        for offset, c in enumerate(sorted_list):
            if c >= i:
                sorted_list.insert(offset, i)
                break
        else:
            sorted_list.append(i)
    return sorted_list


class listmanupulation(unittest.TestCase):

    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("hello world"), "hll wrld")

    def test_check_pwd(self):
        self.assertEqual(check_pwd("Hello W0rld"), "valid password")

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([1, 5, 3, 3]), [1, 3, 3, 5])


def main():
    str = input("enter file name: ")
    x1 = remove_vowels(str)
    print(x1)

    pwd = input("enter password: ")
    x2 = check_pwd(pwd)
    print(x2)

    print("enter the numbers to be sorted with space between numbers: ")
    l = [int(x) for x in input().split()]
    x3 = insertion_sort(l)
    print(x3)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    main()
