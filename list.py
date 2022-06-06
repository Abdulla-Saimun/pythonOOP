>>> my_list = [3, 4, 5, 2, 7, 8, 1]
>>> my = [item for item in my_list if item>4]
>>> my
[5, 7, 8]
>>> ls = [x for x in my_list if x<7]
>>> ls
[3, 4, 5, 2, 1]
>>> ls = [x+1 for x in my_list if x<7]
>>> ls
[4, 5, 6, 3, 2]
>>>
>>> my_list = [5, 2, 90, 24, 10, 2, 95, 36]
>>>
>>> print([i**2 for i in my_list])
[25, 4, 8100, 576, 100, 4, 9025, 1296]
>>>
>>> list_of_lists = [[1, 2],
...                  [3, 4],
...                  [5, 6],
...                  [7, 8]]
>>>
>>> # using list comprehension
>>> my_list = [item for List in list_of_lists for item in List]
>>> print(my_list)
[1, 2, 3, 4, 5, 6, 7, 8]
>>>
