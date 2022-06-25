#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for column in range(len(row)):
            print(
                    "{:d}".format(row[column]),
                    end="" if column == len(row) - 1 else " ")
        print("")
