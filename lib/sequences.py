#!/usr/bin/env python3


def print_fibonacci(length):
    i = 1
    my_list = []
    if length > 0:
        my_list.append(0)
        if length > 1:
            my_list.append(1)
            if length > 2:
                while len(my_list) < length:
                    my_list.append(my_list[i]+my_list[i-1])
                    i +=1
                print(my_list)
                return
    print(my_list)
    return