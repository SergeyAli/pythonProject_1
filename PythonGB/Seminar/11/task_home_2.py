'''
📌 Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц
'''

class Matrix:

    def __init__(self, a_matrix: list[list[int, float]]):
        self._rows = len(a_matrix)
        self._cols = len(a_matrix[0])
        self._a_matrix = a_matrix

    def __add__(self, other):
        new_matrix = [[0 for _ in range(self._cols)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._cols):
                new_matrix[j][i] = self._a_matrix[j][i] + other._a_matrix[j][i]
        return Matrix(new_matrix)


    def __eq__(self, other) :
        for j in range(self._rows):
            for i in range(self._cols):
                if self._a_matrix[j][i] != other._a_matrix[j][i]:
                    return False
        return True


    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self._a_matrix]) + '\n'



if __name__ == '__main__':
    matr_a = Matrix([[5, 3], [1, 2], [6,  1]])
    # matr_b = Matrix([[3, 6], [4, 1], [5,  9]])
    matr_b = Matrix([[10, 6], [7, 5], [3, 1]])
    matr_c = Matrix([[10, 6], [7, 5], [3, 1]])

    print(matr_a)
    print(matr_b)
    print(matr_c)

    print(f'{matr_a == matr_b = }')
    print(f'{matr_a == matr_b = }')
    print(f'{matr_b == matr_c = }')
    print(matr_a + matr_b)
    print(matr_a + matr_c)
