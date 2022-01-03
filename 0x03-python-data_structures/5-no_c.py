#!/usr/bin/python3
def no_c(my_string):
    new = list(my_string)
    for i in new[0:]:
        if i == 'C' or i == 'c':
            new.remove(i)
    return("".join(new))
