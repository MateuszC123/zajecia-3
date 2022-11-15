zwiezeta = []

x = 0
while x < 4:
    y= input("wprowadz imiona zwierzat: ")
    zwiezeta.append(y)
    x += 1
print(zwiezeta)
b = sorted(zwiezeta)
print(b)
print(zwiezeta[0], zwiezeta[-3:])
print(zwiezeta.sort())
print(len(zwiezeta))