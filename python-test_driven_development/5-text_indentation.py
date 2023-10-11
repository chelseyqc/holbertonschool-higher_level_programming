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

    for i in range(len(text)):
        if text[i] in ".?:" and i != len(text) - 1:
            print(text[i], end="\n\n")
        else:
            print(text[i], end="")
