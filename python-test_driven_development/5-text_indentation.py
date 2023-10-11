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
    
    for char in ".?:":
        text = text.replace(char, char + "|")
    
    sentences = text.split("|")

    for line in sentences:
        if line != "":
            print(line.strip() + "\n")
