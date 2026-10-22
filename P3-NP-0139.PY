# Array indexing in NumPy
#Alexander Salazar NC = 0139
import numpy as np
n0139 = np.array([10, 20, 30, 40, 50])
print(n0139)
print(n0139[0])
print(n0139[3])
print(n0139[-1])
print(n0139[-2])
print("----------------------------------------")
n0139 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(n0139)
print(n0139[0, 0])
print(n0139[1, 2])
print(n0139[-1, -1])
print(n0139[-2, -2])
print("----------------------------------------")
# 3D array 2x(2x3)
n0139 = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])

print(n0139)
print(n0139[0, 0, 0])
print(n0139[1, 1, 0])
print(n0139[-1, -1, -2])
print("Alexander salazar NC= 0139")