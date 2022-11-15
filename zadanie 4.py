
import random
punkty = []
for i in range(0, 15):
    a = random.uniform(0, 50)
    a = round(a,2)
    punkty.append(a)
print(punkty)
punkty.sort()
print(punkty)
print(punkty[0], punkty[-1])
""" powinno sie robic funkjca """
print("najwieksza : ", min(punkty)," i najmiejsza liczba", max(punkty))



