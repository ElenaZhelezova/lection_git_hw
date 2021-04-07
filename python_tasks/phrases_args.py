"""
Task 3
Something old in a new way :). Self-study positional arguments for Python scripts
(sys.argv). Write a script that takes a list of words (or even phrases) Script
should ask a user to write something to stdin until user won't provide one of
argument phrases.
"""


import sys


def main(st_ph):
    for line in sys.stdin:
        if st_ph == line.rstrip():
            break
        print(f"write word or phrase or '{st_ph}' for exit: ")
    print("Bye")


if __name__ == '__main__':
    stop_phrase = ' '.join(sys.argv[1:])
    print(f"write word or phrase or '{stop_phrase}' for exit: ")
    main(stop_phrase)