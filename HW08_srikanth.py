
"""python file to perform date arthemetic, field seperated file reader  and scanning directories and files
    author srikanth"""
import os
from prettytable import PrettyTable
from datetime import datetime
from datetime import timedelta


def days_date():
    d1 = datetime.strptime("Jan 1, 2017", '%b %d, %Y')
    d2 = datetime.strptime("Oct 31, 2017", '%b %d, %Y')
    d3 = datetime.strptime("Feb 27, 2000", '%b %d, %Y')
    d4 = datetime.strptime("Feb 27, 2017", '%b %d, %Y')
    print('number of days between {} and {} is {}'.format(d1, d2, (d2-d1).days))
    print('{} days after {} is {}'.format(3, d3, (d3+timedelta(days=3))))
    print('{} days after {} is {}'.format(3, d4, (d4+timedelta(days=3))))


def file_read(path, num_field, seperator=',', header=False):

    fp = open(path, 'r')
    for n, line in enumerate(fp):
        line = line.strip()
        ele = line.split(seperator)
        if len(ele) == num_field:
            if header == True:
                header = False
                continue
            yield tuple(ele)
        else:
            raise(Exception)


def pretty_table(p):
    pt = PrettyTable(field_names=['file', 'classes',
                                  'functions', 'lines', 'characters'])
    l = 0
    cha = 0
    fn = 0
    c = 0

    print("\nsummary for ", p)
    for f in os.listdir(p):
        if f.endswith('.py'):
            a = p+f
            fp = open(a, 'r')
            for line in fp:
                cha += len(line)
                l += 1
                line = (line.strip())
                if line.startswith('def '):
                    fn += 1
                if line.startswith('class '):
                    c += 1

            pt.add_row([a, c, fn, l, cha])
            c, fn, cha, l = 0, 0, 0, 0
    print(pt)


def main():
    days_date()

    #path="D:/college/test/p2.txt"
    try:
        path = input("enter the path for the file")
        for cwid, name, major, year in file_read(path, 4, seperator='|', header=True):
            print("name: {} cwid: {} major: {} year: {}".format(
                name, cwid, major, year))
    except FileNotFoundError:
        print("FILE NOT FOUND")

    try:
        #p = "D:/college/ssw 810/"
        p = input(
            "\nEnter absolute path of directory from which the pretty table should be derived: ")
        pretty_table(p)
    except FileNotFoundError:
        print("directory not found ")


if __name__ == '__main__':
    main()
