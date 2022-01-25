#!/usr/bin/python3
""" This is 5-text_indentation.py that replaces   by 2 new lines"""


def text_indentation(text):
    """Returns the text replacing the "." "?" ":" by 2 new lines "
        Return:
            Final text with the new lines
    """
    sep = "\n"
    if type(text) is not str:
        raise TypeError("text must be a string")
    x = text.replace(".", ".\n\n").replace("?", "?\n\n").replace(":", ":\n\n")
    new_list = [line.strip() for line in x.split("\n")]
    for i in range(len(new_list)):
        if i == len(new_list) - 1:
            sep = ""
        print(new_list[i], end=sep)
