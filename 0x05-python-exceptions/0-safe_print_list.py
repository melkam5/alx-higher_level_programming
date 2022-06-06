#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elem = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            num_elem += 1
    except IndexError:
        print(end='')
    finally:
        print()
    return num_elem
