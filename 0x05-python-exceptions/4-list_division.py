#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = [None] * list_length
    for i in range(list_length):
        try:
            new_list[i] = my_list_1[i] / my_list_2[i]
        except TypeError:
            new_list[i] = 0
            print("wrong type")
        except ZeroDivisionError:
            new_list[i] = 0
            print("division by 0")
        except IndexError:
            new_list[i] = 0
            print("out of range")
        finally:
            continue
    return (new_list)
