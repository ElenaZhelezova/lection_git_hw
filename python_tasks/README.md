### Task 1
Self-study input() function. Write a script which accepts a sequence of
comma-separated numbers from user and generate a list and a tuple with those
numbers and prints these objects as-is (just print(list) without any formatting).

```
>>> python3 study_input.py 
enter comma-separated numbers: 55, 6,7, 99,100
[55, 6, 7, 99, 100]
(55, 6, 7, 99, 100)
```

### Task 2
Develop a procedure to print all even numbers from a numbers list which is given
as an argument. Keep the original order of numbers in list and stop printing if
a number 254 was met. Don't forget to add a check of the passed argument type.

```
>>> python3 print_nums.py 33, 66, 66, 77,254, 8
33
66
66
77

>>> python3 print_nums.py [33, 66, 66, 77,254, 8
33
66
66
77

>>> python3 print_nums.py [33, 66, 66, 77,254, 8]
33
66
66
77

>>> python3 print_nums.py [33,66,66,77,254,8]
33
66
66
77

>>> python3 print_nums.py 33,66,66,77,254,8
33
66
66
77
```


### Task 3
Something old in a new way :). Self-study positional arguments for Python scripts
(sys.argv). Write a script that takes a list of words (or even phrases)aScript
should ask a user to write something to stdin until user won't provide one of
argument phrases.
```
>>> python3 phrases_args.py stop it!
write word or phrase or 'stop it!' for exit: 
stop
write word or phrase or 'stop it!' for exit: 
stop it
write word or phrase or 'stop it!' for exit: 
stop it!
Bye
```


### Task 4
We took a little look on os module. Write a small script which will print a
string using all the types of string formatting which were considered during the
lecture with the following context: This script has the following PID:
<ACTUAL_PID_HERE>. It was ran by <ACTUAL_USERNAME_HERE> to work happily on
<ACTUAL_OS_NAME>-<ACTUAL_OS_RELEASE>.
```
>>> python3 actual_pid.py 
This script has the following PID: 455048. It was ran by elena to work happily on Linux - 5.4.0-70-generic
This script has the following PID: 455048. It was ran by elena to work happily on Linux - 5.4.0-70-generic
This script has the following PID: 455048. It was ran by elena to work happily on Linux - 5.4.0-70-generic
This script has the following PID: 455048. It was ran by elena to work happily on Linux - 5.4.0-70-generic
```


### Task 5
Develop a function that takes a list of integers (by idea not in fact) as an
argument and returns list of top-three max integers. If passed list contains
not just integers collect them and print the following error message: You've
passed some extra elements that I can't parse: [<"elem1", "elem2" .... >].
If return value will have less than 3 elements for some reason it's ok and
shouldn't cause any problem, but some list should be returned in any case.
```
>>> python3 top_three_max_int.py 55, 66, 77, 9, 11
[77, 66, 55]

>>> python3 top_three_max_int.py 55, 66, 77, 9, 11, fhfhfh, hh
you've passed some extra elements that I can't parse: ['fhfhfh', 'hh']

>>> python3 top_three_max_int.py 55, 66
[66, 55]

>>> python3 top_three_max_int.py '55' 66 77 9 11 fhfhfh hh]
you've passed some extra elements that I can't parse: ['fhfhfh', 'hh']

>>> python3 top_three_max_int.py [55, 66]
[66, 55]

>>> python3 top_three_max_int.py [55,66]
[66, 55]

>>> python3 top_three_max_int.py 55,66
[66, 55]
```

### Task 6
Create a function that will take a string as an argument and return a dictionary
where keys are symbols from the string and values are the count of inclusion of
that symbol.
```
>>> python3 symbols_dict.py lsakjvhjadkvkasvjadhhcvjkdsjvkdbvhj kasjkb skbfjhahcv asdasjk
{'l': 1, 's': 7, 'a': 8, 'k': 9, 'j': 9, 'v': 7, 'h': 6, 'd': 5, 'c': 2, 'b': 3, ' ': 3, 'f': 1}

>>> python3 symbols_dict.py abracadabra
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
```

### Task 7
Develop a procedure that will have a size argument and print a table where num
of columns and rows will be of this size. Cells of table should contain numbers
from 1 to n ** 2 placed in a spiral fashion. Spiral should start from top left
cell and has a clockwise direction.
```
>>> python3 square_table.py 10
1 2 3 4 5 6 7 8 9 10 
36 37 38 39 40 41 42 43 44 11 
35 64 65 66 67 68 69 70 45 12 
34 63 84 85 86 87 88 71 46 13 
33 62 83 96 97 98 89 72 47 14 
32 61 82 95 100 99 90 73 48 15 
31 60 81 94 93 92 91 74 49 16 
30 59 80 79 78 77 76 75 50 17 
29 58 57 56 55 54 53 52 51 18 
28 27 26 25 24 23 22 21 20 19 

>>> python3 square_table.py a
argument is not a number

>>> python3 square_table.py 5
1 2 3 4 5 
16 17 18 19 6 
15 24 25 20 7 
14 23 22 21 8 
13 12 11 10 9 
```

### Task 8*
You have had AWK homework (3-4), please find a document in a homework Slack
thread. Do all the same AWK tasks using Python.

#####* What is the most frequent browser (user agent)?
#####* Show number of requests per month for ip 95.108.129.196 
#####* Show total amount of data which server has provided for each unique ip
```
>>> python3 awk_puzzles.py --log_file access.log --ip 193.106.31.130
...
your report in ../access.log-2021-04-06 15:09:01.617561-report.txt file

>>> cat access.log-2021-04-06\ 15\:09\:01.617561-report.txt | head -n10 
most frequent user agent: "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)" - used 34387 times 

number of requests for 193.106.31.130:
Dec/2020  -  10291 requests
Jan/2021  -  24096 requests

total amount of data:
32653 bytes for 13.66.139.0
450 bytes for 157.48.153.185
22017 bytes for 216.244.66.230


```

