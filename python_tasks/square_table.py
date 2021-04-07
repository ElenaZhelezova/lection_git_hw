"""
Task 7
Develop a procedure that will have a size argument and print a table where num
of columns and rows will be of this size. Cells of table should contain numbers
from 1 to n ** 2 placed in a spiral fashion. Spiral should start from top left
cell and has a clockwise direction.
"""


import sys


def main(n):
    output_matrix = [[0 for j in range(n)] for i in range(n)]
    k = n * n
    m = 1
    d = 0

    while m <= k:
        for j in range(d, n - d):
            output_matrix[d][j] = m
            j += 1
            m += 1

        for i in range(1 + d, n - d):
            output_matrix[i][n - 1 - d] = m
            i += 1
            m += 1

        b = [0 for j in range(n)]
        for j in range(1 + d, n - d):
            b[j] = m
            j += 1
            m += 1
        b.reverse()

        for j in range(d, n - 1 - d):
            output_matrix[n - 1 - d][j] = int(b[j])

        c = [0 for i in range(n)]
        for i in range(1 + d, n - 1 - d):
            c[i] = m
            i += 1
            m += 1
        c.reverse()

        for i in range(1 + d, n - 1 - d):
            output_matrix[i][d] = int(c[i])
        d += 1

    return output_matrix


if __name__ == '__main__':
    try:
        num = int(sys.argv[1])
        matrix = main(int(num))
        for i in matrix:
            for j in i:
                print(j, end=' ')
            print()

    except ValueError:
        print("argument is not a number")

