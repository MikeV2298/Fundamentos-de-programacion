# Ejemplo 1
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)
    
# Ejemplo 2
for i in range(0, 4):
    for j in range(0, 4):
        break
        #Nunca se realiza más de una iteración
    # El break no afecta a este for
    print(i, j)
    
# Ejemplo 3
for num in range(-10, 9):
    print(num)

    if num >= 6:
        break
