#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")

    sentences = text.replace(".", ".\n\n")
    sentences = sentences.replace("?", "?\n\n")
    sentences = sentences.replace(":", ":\n\n")

    new_text = sentences.splitlines(True)
    list1 = []
    for c in new_text:
        if c == "\n":
            list1.append("\n")
        else:
            list1.append(c.lstrip())
    print("".join(list1), end="")
