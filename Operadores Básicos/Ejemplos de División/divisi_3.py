
a = float(input("Ingrese un Valor: "))
b = float(input("Ingrese un Valor: "))
c = float(input("Ingrese un Valor: "))

v = a + b*c
w = a * c

div1 = v / b
div2 = (w * v) / (a + c + b)

print("Resultado de la primera operación:")
print(v,"/",b,'=',div1)
print("Resultado de la primera operación:")
print('(',w,'x',v,')','/','(',a,'+',c,'+',b,')','=',div2)
