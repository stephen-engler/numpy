import numpy as np

arr = np.arange(0,11)
#indexing similar to lists
print(arr[4])
#same with slicing
print(arr[1:5])
print(arr[5:])

#broadcast
arr[0:5]=100
print(arr)

arr = np.arange(0,11)

#data isn't copied but reference
#if want copy
arr_copy = arr.copy()
arr_copy[:] = 100

print(arr)
print(arr_copy)

arr_2d = np.array([[5,10,15], [20,25,30], [35,40,45]])
print(arr_2d)

#array[row][column] or array[array,column]
print(arr_2d[0][0])
print(arr_2d[2,2])

#grab sub matrix
print(arr_2d[:2, 1:])