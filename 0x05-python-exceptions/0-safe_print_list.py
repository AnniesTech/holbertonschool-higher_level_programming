#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        new_list = my_list[:x]
        cont = 0
        print(*new_list, sep='')
        for i in new_list:
            cont = cont + 1
        return(cont)
    except IndexError:
        return(cont)
