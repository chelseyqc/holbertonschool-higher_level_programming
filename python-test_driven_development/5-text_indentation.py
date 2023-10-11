#!/usr/bin/python3
"""prints a text"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after ., ?, and :

    Args:
        text (str): the text to be indented
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text_copy = str(text)
    last_char = False

    for char in text_copy:
        if last_char:
            if char == " ":
                continue
            last_char = False
        if char in ['.', '?', ':']:
            print(char)
            print("")
            last_char = True
        else:
            print(char, end="")
