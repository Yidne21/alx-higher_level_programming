#!/usr/bin/python3
def safe_print_division(a, b):
    questiont = 0
    try:
        questiont = a / b
    except ZeroDivisionError:
        questiont = None
    finally:
        print('Inside result: {}'.format(questiont))
        return questiont
