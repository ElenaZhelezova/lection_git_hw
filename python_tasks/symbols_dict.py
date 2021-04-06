"""
Task 6
Create a function that will take a string as an argument and return a dictionary
where keys are symbols from the string and values are the count of inclusion of
that symbol.
"""


import sys
from collections import defaultdict as ddict


def main(str):
    dict_str = ddict(int)
    for k in str:
        dict_str[k] += 1

    return dict(dict_str)


if __name__ == '__main__':
    input_str = ' '.join(sys.argv[1:])
    print(main(input_str))

