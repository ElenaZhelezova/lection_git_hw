"""
Task 5
Develop a function that takes a list of integers (by idea not in fact) as an
argument and returns list of top-three max integers. If passed list contains
not just integers collect them and print the following error message: You've
passed some extra elements that I can't parse: [<"elem1", "elem2" .... >].
If return value will have less than 3 elements for some reason it's ok and
shouldn't cause any problem, but some list should be returned in any case.
"""


import sys


def main(lst):
    nums = []
    not_nums = []
    for i in lst:
        i = i.strip('[]').split(',')
        for j in i:
            if not j:
                continue
            if j.isdigit():
                nums.append(int(j))
            else:
                not_nums.append(j)
    if not not_nums:
        nums = sorted(nums, reverse=True)
        print(nums[:3])
    else:
        print(f"you've passed some extra elements that I can't parse: {not_nums}")

    return


if __name__ == '__main__':
    main(sys.argv[1:])

