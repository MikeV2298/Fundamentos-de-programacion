#EJEMPLO 1
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

#EJEMPLO 2
j = 0
for i in range(10):
    j += 2
    print('i:', i, 'j:', j)
    if j >= 2 and j <= 18:
        continue
    print('el valor de j:', j)

#EJEMPLO 3
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)
