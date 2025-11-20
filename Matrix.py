class Matrix:

    def __init__(self, height, wight, matrix) -> None:
        self.width = wight
        self.height = height
        self.value = []
        self.cols = []
        self.rows = [1]
        # Реализация хранения матрицы в разряженно-строчном виде
        new_row = [1]
        for i in range(self.height):
            for j in range(self.width):
                if matrix[i][j] != 0:
                    self.value.append(matrix[i][j])
                    self.cols.append(j + 1)
            self.rows.append(len(self.value) + 1)

    def __str__(self):                      # Просто возвращение матрицы
        matrix_str = ""
        for i in range(self.height):
            row_str = ""
            for j in range(self.width):
                row_str += str(self.get_elem(i + 1, j + 1)) + " "
            matrix_str += row_str + "\n"
        return matrix_str
    
    def get_trace(self):                                # Поиск следа матрицы
        if self.height == self.width:
            trace = 0
            for i in range(self.height):
                trace += self.get_elem(i + 1, i + 1)
            return trace
        else:
            raise MatrixError( "Error: size of rows and cols must be equal!")

    def get_elem(self, row, col):    # Поиск элемента матрицы по индексу и столбцу
        row, col = row, col
        
        coll = self.value[self.rows[row - 1] - 1:self.rows[row] - 1]
        slice_cols = self.cols[self.rows[row - 1] - 1:self.rows[row] - 1]

        if col in slice_cols:
            return coll[slice_cols.index(col)]
        
        elif (col < 1 or col > self.width) or (row < 1 or row > self.height): 
            raise MatrixError ("Invailed row or col size, try again!")
        
        else: return 0

    def __add__ (self, matrix2): 
        if self.width != matrix2.width or self.height != matrix2.height:
            raise MatrixError("Sizes of matrix must be equal")
        
        new_matrix = []
        for i in range(self.height):
            for j in range(self.width):
                new_matrix.append(self.get_elem(i + 1, j + 1) + matrix2.get_elem(i + 1, j + 1))

        return Matrix(self.height, self.width, new_matrix)

    def __mul__ (self, number):

        new_matrix = []
        if type(number) is int:
            for i in range(self.height):
                for j in range(self.width):
                    new_matrix.append(self.get_elem(i + 1, j + 1) * number)
        
        elif type(number) is Matrix:
            if self.width != number.height:
                raise MatrixError("The size of the rows should be equal to the size of the columns.")

            for i in range(self.height):
                row = [] 
                for j in range(number.width):
                    element_ij = 0
                    for k in range(self.width):
                        element_ij += self.get_elem(i + 1, k + 1) * number.get_elem(k + 1, j + 1)
                    row.append(element_ij) 
                new_matrix.append(row) # 

            return Matrix(self.height, number.width, new_matrix)  

    def get_determine(self):
        if self.width != self.height:
            raise MatrixError("Matrix must be square to calculate determinant.")

        # Create a deep copy! Crucial for correct determinant calculation
        matrix_copy = [[self.get_elem(i + 1, j + 1) for j in range(self.width)] for i in range(self.height)]

        if self.width == 1:
            return matrix_copy[0][0]  # Base case for 1x1 matrix
        elif self.width == 2:
            return matrix_copy[0][0] * matrix_copy[1][1] - matrix_copy[0][1] * matrix_copy[1][0]  # Base case for 2x2 matrix

        determinant = 0
        for i in range(self.width):
            minor = [row[:i] + row[i+1:] for row in matrix_copy[1:]] # Correct minor calculation
            determinant += ((-1)**i) * matrix_copy[0][i] * Matrix(len(minor), len(minor[0]), minor).get_determine()

        return determinant


class MatrixError(Exception):
    def __init__(self, message):
        super().__init__(message)

# rows1, cols1 = map(int, input("Введите кол-во строк и столбцов 1 матрицы: ").split())
# matrix_1 = [list(map(int, input().split())) for _ in range(rows1)]

# rows2, cols2 = map(int, input("Введите кол-во строк и столбцов 2 матрицы: ").split())
# matrix_2 = [list(map(int, input().split())) for i in range(rows2)]

# num = int(input("Введите скаляр: "))

# print(matrix_1 + matrix_2)
# print(matrix_1 * matrix_2)
# print(matrix_1 * num)
# print(matrix_1.get_determine())

matrix1 =   Matrix(3, 3, [[1, -2, 3], 
                          [0, 7, 4], 
                          [5, 3, -3]])

matrix2 =  Matrix(3, 3, [[1, 0, 0], 
                         [0, 9, 0], 
                         [1, 0, 0]])

matrix3 =  Matrix(4, 5, [[1, 4, 0, 8, 7], 
                         [0, 9, 0, 9, 3], 
                         [1, 0, 0, 1, 4],
                         [1, 0, 0, 4, 1]])

matrix4 =  Matrix(5, 5, [[1, 4, 0, 8, 7], 
                         [0, 93, 0, 0, 34], 
                         [2, 0, 1, 1, 7],
                         [3, 1, 9, 90, 3], 
                         [90, 3, 0, 4, 1]])

matrix5 =  Matrix(5, 5, [[19, 3, 0, 8, 7], 
                         [0, 53, 56, 7, 34], 
                         [2, 0, 1, 11, 5],
                         [0, 1, 4, 1, 0],
                         [0, 3, 0, 43, 1]])
# print(matrix1 * 4)
# print(matrix1 * matrix2)
# print(matrix1.get_determine())
