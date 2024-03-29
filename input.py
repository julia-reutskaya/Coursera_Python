from sys import stdin
from copy import deepcopy


class Matrix:
    def __init__(self, lists):
        self.lists = deepcopy(lists)

    def __str__(self):
        strRep = ""
        amount = 0
        for lists in self.lists:
            if amount != 0:
                strRep += "\n"
            new_str = "\t".join(str(elem) for elem in lists)
            strRep += new_str
            amount += 1
        return strRep

    def size(self):
        return len(self.lists), len(self.lists[0])

    def __add__(self, other):
            result = []
            numbers = []
            for i in range(len(self.lists)):
                for j in range(len(self.lists[0])):
                    summa = other.lists[i][j] + self.lists[i][j]
                    numbers.append(summa)
                    if len(numbers) == len(self.lists[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)

    def __mul__(self, alpha):
        if isinstance(alpha, int) or isinstance(alpha, float):
            result = []
            numbers = []
            for i in range(len(self.lists)):
                for j in range(len(self.lists[0])):
                    summa = self.lists[i][j] * alpha
                    numbers.append(summa)
                    if len(numbers) == len(self.lists[0]):
                        result.append(numbers)
                        numbers = []
            return Matrix(result)

    def transpose(self):
        t_matrix = list(zip(*self.lists))
        self.lists = t_matrix
        return Matrix(t_matrix)

    def transposed(self):
        t_matrix = list(zip(*self.lists))
        return Matrix(t_matrix)

    __rmul__ = __mul__


exec(stdin.read())