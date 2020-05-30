'''python script to convert singular to plurals
    author: srikanth'''

import unittest

def reverse(str1):


    print("Entered string is: ", str1)
    str = ""
    for i in str1:
        str = i + str
    print("reverse string is: ", str)
    return str


def rev_enumerate(seq):


    offset = len(seq)-1
    while offset > -1:
        yield offset, seq[offset]
        offset = offset-1


def find_second(s1, s2):


    first = s2.find(s1)
    second = s2.find(s1, first+1)
    if second == -1:
        return -1
    else:
        print("the offset of second accurance seq is: ", second)
        return second


def get_lines(path):


    try:
        fp=open(path,'r')
    except FileNotFoundError:
        print("file not found cant open", path)
    else:
        with fp:
            str1 = fp.read()
            str2 = " "
            i=0
            while i < len(str1):
                if str1[i] == "\\":
                    i+=2
                else:
                    str2 += str1[i]
                    i +=1
            
            line = str2.split("\n")

            for item in line:
                if item.startswith("#"):
                    line.remove(item)
                
            for item in line:
                if "#" not in item:
                    yield item
                else:
                    i=item.find("#")
                    yield(item[:i])


class GetLinemanupulation(unittest.TestCase):


    def test_reverse(self):


        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse(""), "")
        
    def test_rev_enumerate(self):


        expect = [(4, 'o'), (3, 'l'), (2, 'l'), (1, 'e'), (0, 'h')]
        result = list(rev_enumerate("hello"))
        self.assertEqual(result, expect)

        expect = [(9, 't'), (8, 'o'), (7, 'b'), (6, 'o'), (5, 'r'), (4, ' '),(3, 'm'), (2, 'a'), (1, ' '), (0, 'i')]
        result = list(rev_enumerate("i am robot"))
        self.assertEqual(result, expect)
        
    def test_find_second(self):


        self.assertEqual(find_second('iss', 'mississippi'), 4)
        self.assertEqual(find_second('mimi', 'hello mi mi mi mi'), -1)
        self.assertEqual(find_second('aba', 'ababa'), 2)


    def test_get_lines(self):


        file_name = 'D:/college/test1.txt'
        expect = ['<line0>', '<line1>', '<line2>', '< line3.1 line3.2 line3.3 >','<line4.1 line4.2>', '<line5>', '<line6>']
        result = list(get_lines(file_name))
        self.assertEqual(result, expect)

def main():


    str1 = input("enter the input string to reverse: ")
    reverse(str1)

    seq = input("enter seq to be reverse enumerated ")
    y = rev_enumerate(seq)
    for i in range(len(seq)):
        print(next(y))

    s1 = input("enter the ele to be searched: ")
    s2 = input("enter the string: ")
    find_second(s1, s2)

    f_name='test1.txt'
    for line in get_lines(f_name):
        print(line)


if __name__ == "__main__":
    
   # unittest.main(exit=False, verbosity=2)
    main()
