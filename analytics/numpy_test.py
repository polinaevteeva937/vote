import numpy as np

my_list = [1, 2, 3, 4, 5, 6]
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array1 = np.array(my_list)
array2 = np.array(my_matrix)

array3 = np.arange(0, 10, 2)
array4 = np.zeros((5, 5), dtype = "int64")
array5 = np.ones((5, 5), dtype = "int64")
array6 = np.linspace(0, 1, 5, dtype = "float64")
array7 = np.eye(4, dtype = "int64")
array8 = np.random.rand(3, 3)
array9 = np.random.randint(1, 20, 6)
print('\n', array9)

max = array9.max()
min = array9.min()
sum = array9.sum()
mean = array9.mean()

slice = array9[0:3]
shape1 = array9.reshape(3, 2)
shape2 = array9.reshape(2, 3)

array9 *= 2
array9[0] /= 2
print('\n', array9)


# print('Новый массив \n', array9)