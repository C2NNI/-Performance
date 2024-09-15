import numpy as np

task_array = []
np.array(task_array)

print("Введите длину массива:")
n = int(input())
print("Введите длину обхода:")
m = int(input())

for i in range (1, n+1):
    task_array.append(i)
print(task_array)

index = 0
new_array = []
np.array(new_array)

while True:
    if index > n - 1:
        break
    new_array.append(task_array[index])
    index = (index + m - 1) % len(task_array)
    if new_array[len(new_array)-1] == 1 and len(new_array) > 1:
        break
print(new_array[:len(new_array)-1])