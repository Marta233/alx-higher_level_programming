#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    numbers = my_list.copy()
    if idx < 0 and idx > (len(my_list) - 1):
        return (my_list.copy())
    else:
        numbers[idx] = element
        return (numbers)
