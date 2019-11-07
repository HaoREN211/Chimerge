# 作者：hao.ren3
# 时间：2019/11/7 20:08
# IDE：PyCharm
from numpy import array, shape

matrix_1 = array([[5, 0, 0], [4, 1, 1]])
matrix_2 = array([[45.0/11.0, 5.0/11, 5.0/11],
            [54.0/11, 6.0/11, 6.0/11]])

nb_row, nb_column = shape(matrix_1)

sum_c = 0.0
for i in range(nb_row):
    for j in range(nb_column):
        sum_c += (matrix_1[i, j] - matrix_2[i, j])*(matrix_1[i, j] - matrix_2[i, j])/matrix_2[i, j]
print(sum_c)