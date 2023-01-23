#!/usr/bin/python3
def safe_print_list(my_list=[], y=0):
    for j in range(y):
        try:
            print(my_list[j], end='')
        except IndexError:
            print()
            return j
    print()
    return y
