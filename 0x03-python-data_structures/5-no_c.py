#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for idx in range(0, len(my_string)):
        if my_string[idx] == 'c' or my_string[idx] == 'C':
            new_string = new_string + ""
        else:
            new_string = new_string + my_string[idx]
    print(new_string)
