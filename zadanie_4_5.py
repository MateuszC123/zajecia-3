import random

punkty = [round(random.uniform(0, 50), 2) for i in range(15)]
print(punkty)
print(min(punkty), max(punkty))
g = float(input("prosze podac liczbe punktow: "))

if (g == punkty):
    print(punkty.index(g))
else:
    print("niema takiego numeru rzeczywistego w liscie")

b = sum(punkty) / len(punkty)
b = round(b, 2)
print("srednia: ", b)

list1 = []
for i in punkty:
    if i < b:
        list1.append(i)
print(len(list1))
print(list1)

list2 = [i for i in punkty if i > b]
print(len(list2))
print(list2)





