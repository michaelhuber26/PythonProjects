import numpy as np
import sys


arr = np.array([1, 2, 3, 4, 5, 6, 7, 0, 8])  # for TESTING
arr = np.reshape(arr, (-1, 3))

print(arr)

arr = np.reshape(arr, (-1))

print(arr)

pos = np.where(arr == 0)
arr = np.delete(arr, pos)

print(arr)

arr = np.insert(arr, 5, 0)

sArr = ""
for i in arr:
    sArr += str(i)

print(sArr)

for i in range(9):
    sys.stdout.write(sArr[i]+ " ")

    if (i+1)%3 == 0:
        sys.stdout.write('\n')

print("")



sArr = sArr[:3] + '\n' + sArr[3:]
sArr = sArr[:6+1] + '\n' + sArr[6+1:]

print(sArr)

print('.', end='', flush=True)
