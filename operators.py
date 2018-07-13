import numpy as np

arr = np.arange(0,11)
#can use math operators on arrays
arr + arr
arr - arr
arr * arr
print(arr * 100)
#sometimes numpy won't give error for 1/0 just a warning

#universal array functions
print(np.sqrt(arr))
print(np.sin(arr))
print(arr)