"""
Task 1
Self-study input() function. Write a script which accepts a sequence of
comma-separated numbers from user and generate a list and a tuple with those
numbers and prints these objects as-is (just print(list) without any formatting).
"""


def main(seq):
    seq = seq.split(',')
    seq_list = []
    for i in seq:
        try:
            i = int(i)
            seq_list.append(int(i))
        except:
            continue
    seq_tuple = tuple(seq_list)
    print(seq_list)
    print(seq_tuple)
    return


if __name__ == '__main__':
    sequence = input("enter comma-separated numbers: ")
    main(sequence)
