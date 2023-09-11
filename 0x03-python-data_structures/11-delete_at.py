#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        for x in range(idx, (len(my_List) - 1)):
            my_list[x] = my_list[x + 1]
        my_list = my_list[:-1]
    return (my_list)
