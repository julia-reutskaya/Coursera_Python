from sys import stdin
from copy import deepcopy


class Matrix(object):
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)

    def __str__(self):
        str_rep = ""
        amount = 0
        for matrix in self.matrix:
            if amount != 0:
                str_rep += "\n"
            new_str = "\t".join(str(elem) for elem in matrix)
            str_rep += new_str
            amount += 1
        return str_rep

    def size(self):
        return len(self.matrix), len(self.matrix[0])


exec(stdin.read())
