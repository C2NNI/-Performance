with open ("C:/Users/Артём/Desktop/НТ Performance/circle.txt", "r") as file:
    list_cen = file.readline().split()
    list_rad = file.readline()
    x, y = list_cen
    rad = list_rad
    #print(x, y, rad)

dot = []
with open ("C:/Users/Артём/Desktop/НТ Performance/dot.txt", "r") as file:
    for line in file:
        point = line.split()
        x_dot, y_dot = point
        dot.append((x_dot, y_dot))
    dot = [tuple(map(float, i)) for i in dot]
    #print(dot)

import math 
for x_dot, y_dot in dot:
    len_dot = math.sqrt(((x_dot - float(x))**2 + (y_dot - float(y))**2))
    if len_dot < float(rad):
        print(1)
    elif  len_dot > float(rad):
        print(2)
    else: print(0)

