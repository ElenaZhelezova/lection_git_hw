"""
Task 2
Develop a procedure to print all even numbers from a numbers list which is given
as an argument. Keep the original order of numbers in list and stop printing if
a number 254 was met. Don't forget to add a check of the passed argument type.
"""


import sys


def main(lst):
    for i in lst:
        i = i.strip('[]').split(',')
        for j in i:
            if j.isdigit() and int(j) != 254:
                print(int(j))
            elif j.isdigit() and int(j) == 254:
                return
    return


if __name__ == '__main__':
    main(sys.argv[1:])

