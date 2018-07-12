import numpy as np

my_list = [1,2,3]

arr = np.array(my_list)

print(arr)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]

mat = np.array(my_mat)
print(mat)
#like range
print(np.arange(0,10, 2))

print(np.zeros((5,5)))
print(np.ones((2,2)))

#evenly disptribute 
linspace = np.linspace(0,5,10)

print(linspace)

#identity matrix
#linear algedra must be square

square = np.eye(4)
print(square)

#random


