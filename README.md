### Nombre: Michael Alexander Chango Burgos
### Carrera: Sistema de Información
### Paralelo: SIN-S-MA-1-1 VAN20

# Proyecto de Fundamentos de la programación.

# ¿Qué es Python? 🐍
Es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. Trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador utilizando un programa denominado interpretador, por lo que no es necesario “traducirlo” a lenguaje máquina. 

Su filosofía hace hincapié en la legibilidad de su código, PYTHON es un lenguaje de programación multiparadigma, ya que soporta Programación Orientada a Objetos, Programación imperativa y en menor medida Programación Funcional. El creador de PYTHON es Guido Van Rossum.

Python ha ido ganando adeptos gracias a su sencillez y a sus amplias posibilidades, sobre todo en los últimos años, ya que facilita trabajar con inteligencia artificial, big data, machine learning y data science, entre muchos otros campos en auge.

## ¿Qué es una variable?
En la variable se puede almacenar uno o varios caracteres (letras, números, etc.) que formen un tipo de dato con el cuál se pueda trabajar en el programa que vayamos a realizar, designándolo con un nombre (no se necesita que sea una palabra real específica) o una letra, pero esta no puede empezar con un carácter que no sea letra.

La variable se caracteriza por ser inestable, inconstante y mudable.

### Nombrando una variable
Como se mencionó anteriormente, la variable no se debe representar con caracteres que no sea una letra al principio, además esa variable no debe ser una palabra reservada de PYTHON, como, por ejemplo: False, None, if, elif, is, in, while, and, def, not, for, entre otras, usualmente se representa con una letra “(letra)” o usando letras con números “num1”.

### Asignando valores a una variable
A continuación, se presentará ejemplos de cómo nombrar una variable.
```Python
x = 2
num1 = 10
año = 2022
```
Ahora para que la variable contenga letras se hace uso de las comillas (“ ”)
```Python
Respuesta = “si”
resp = “no”
titulo3 = “Hello World”
```
Además de asignar variables también haremos uso de la función “print”, esta permite imprimir el dato por medio de consola, ya sea para imprimir la variable o imprimir algo directamente (esta forma usualmente se usa para hacer referencia a una variable que se vaya a representar), por ejemplo:
```Python
x = 100
print(x)
[output] 100

nombre = “Michael Chango”
print(nombre)
[output] Michael Chango
```
# Para imprimir directamente sin crear una variable.
```Python
print (“Hello World”)
[output] Hello World

print(“…”)
[output] …
```
Incluso también podemos guardar un dato en una variable la cuál será ingresada por el usuario por medio del teclado y esta puede pedir números o palabras. Para esto es necesario de usar la función “input”, esta función permite obtener el texto escrito por el usuario, el cual se asignará a un espacio de memoria con el nombre que el programador vea conveniente. Y ya sea si se ingresa un número entero o decimal se hace uso del “int” o ”float”.

Ejemplo:
```Python
x = int(input(“Ingrese dato: ”))
print(x)
[output] Ingrese dato: << y también saldrá el dato ingresado >>
```
Las maneras incorrectas de nombrar una variable son:
```Python
.numero= 10
1palabra = “Star”
nombre apellido = “Miguel Cevallos”
tik-tok = “seguidores”
```

## Operadores básicos
Los operadores básicos son Suma, Resta, Multiplicación, División, Potencia y Módulo, los cuales se representan con los siguientes símbolos:
```Python
Suma: +  
Resta: -  
Multiplicación: *  
División: /  
Potenciación: **
Módulo: %  
```
Con los símbolos mostrados se pueden realizar operaciones matemáticas, además también se puede usar paréntesis, corchetes, llaves, símbolos de desigualdad (>, <, <=, etc.) para establecer operaciones, funciones de forma más estructurada o recalcar ciertos puntos en la operación.

El proceso para realizar operaciones matemáticas y representar por medio de consola aplica para todos, lo único que cambia es su representación simbólica.

### Suma
Para realizar operaciones de suma creamos como mínimo una variable para poder sumar, y esta consiste en reunir varias cantidades para hacer el cálculo en una sola.
```Python
a = 16.5
b = 1.5
print(a + b)
[output] 18
# también se puede calcular creando una variable:
suma  = a + b
print(“El resultado es: “, suma)
[output] El resultado es: 18
```

### Resta
```Python
# Creamos dos variables para poder realizar el cálculo.
x = 24  
y = 18 
# Creamos otra variable donde almacenaremos nuestra operación  
# Presentamos las dos variables (x e y) acompañadas del operador de resta  
vrbl = x - y 
# Presentamos un print para demostrar que nuestra operación sea correcta 
print(“El resultado es: “, vrbl)
[output] El resultado es: 6
```

### Multiplicación
```Python
# Creamos dos variables para poder realizar el cálculo.
a = 15
e = 3 
# Creamos otra variable donde almacenaremos nuestra operación  
# Presentamos las dos variables (a y e) acompañadas del operador de multiplicación  
vrbl = a * e  
# Presentamos un print para demostrar que nuestra operación sea correcta 
print(“El resultado es: “, vrbl)
[output] El resultado es: 45
```

### División
```Python
# Creamos dos variables para poder realizar el cálculo.
a = 15
b = 3 
# Creamos otra variable donde almacenaremos nuestra operación  
# Presentamos las dos variables (a y b) acompañadas del operador de división  
vrbl = (a / b)  
# Presentamos un print para demostrar que nuestra operación sea correcta 
print(“El resultado es: “, vrbl)
[output] El resultado es: 5
```

### Módulo
Se usa el símbolo “%” este operador la utilizamos para hallar el resto "cuando el primer operando se divide por el segundo".
```Python
# Creamos dos variables para poder realizar el cálculo.
a = 51
b = 6
# Creamos otra variable donde almacenaremos nuestra operación  
# Presentamos las dos variables (a y b) acompañadas del operador de módulo  
vrbl = (a % e)  
# Presentamos un print para demostrar que nuestra operación sea correcta 
print (“El resultado es: “, vrbl)
[output] El resultado es: 3
```
### Potencia
En este tipo de operación se hace uso del símbolo de multiplicación pero usándolo dos veces de forma seguida “ **  “.
```Python
# Creamos dos variables para poder realizar el cálculo.
x = 4
y = 2 
# Creamos otra variable donde almacenaremos nuestra operación  
# Presentamos las dos variables (x e y) acompañadas del operador de potencia  
vrbl = (x ** y)  
# Presentamos un print para demostrar que nuestra operación sea correcta 
print(“El resultado es: “, vrbl)
[output] El resultado es: 16
```

## Tipos de datos en Python
En Python están definidos los datos por conjuntos, estos tienen características y propiedades determinadas como lo son los Booleanos, los numéricos (enteros, punto flotante y complejos) y las cadenas de caracteres (string).

### Integer
Los números enteros son aquellos que no llevan decimales y estos pueden ser positivos y negativos, el cero también va incluido, este tipo de dato consta de una serie sin comillas de sólo dígitos.

Ejemplo:
```Python
año = 2022
print (type(año))
[output] <class 'int'>
```

### Float
En este tipo de dato permite insertar números con decimales ya sean positivos o negativos, los valores son almacenados de una forma muy particular.

Ejemplo:
```Python
fx = -5.34
print (type(fx))
[output] <class 'float'>
# Números expresados en notación científica también acepta float
x = 30e2  
print(type(x))
[output] <class 'float'>
```

### String
Las cadenas (o strings) son un tipo de datos conformados por secuencias de caracteres que representan texto (letras, números y otro tipo de caracteres). Se delimitan mediante el uso de comillas simples o dobles.

Ejemplo:
```Python
texto = "khdbh/#3"  
print(type(texto))
[output] <class 'str'>
```

## Casting en Python
Hacer un cast o casting significa convertir un tipo de dato a otro. Anteriormente hemos visto tipos como los int, string o float. Pues bien, es posible convertir de un tipo a otro.
Existen 2 tipos de casting y son:

Casting implícito: Es realizada automáticamente por Python. Sucede cuando realizamos ciertas operaciones con dos tipos distintos.
```Python
x = 4      # <class 'int'>  
y = 2.3   # <class 'float'>  
z = x + y  

print(z) 
[output] 6.3 # <class 'float'>        

print(type(a)) 
[output] <class 'float'>
```
Casting explícito: Es tipo de casting es realizado por nosotros, tenemos la potestad de cambiar nuestro dato al que queremos.
```Python
a = 3.5  
print(type(a)) 
[output] <class 'float'>  

b = str(a)  
print(type(b)) 
[output] <class 'str'>
```

### List
Las listas son un tipo de estructuras de datos muy flexible que guardan de forma ordenada un conjunto de datos que no tienen por qué ser del mismo tipo (‘int’, ‘float’, ‘chr’, ‘str’, ‘bool’, ‘object’).
```Python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums)
[output] [1, 2, 3, 4, 5, 6, 7, 8]

lista = [ 69, "Hello World", 17.25, [8, 16, 24]]
print(lista)
[output] [ 69, 'Hello World', 17.25, [8, 16, 24]]
```

### Tuple
Las tuplas se utilizan para almacenar varios elementos en una sola variable, es una colección ordenada e inmutable ya que no cambian una vez inicializadas.

Ejemplo:
```Python
tupl = (1,2,3)
print(tupl)
[output] = (1,2,3)
```

### Dictionary
Es utilizado para almacenar valores de datos en pares” clave:valor”, sirve para coleccionar información tal como un diccionario normal y corriente de manera ordenada. Además no admite datos duplicados. En este caso se hará uso de las llaves “{}”.

Ejemplo:
```Python
info= {
  "Nombre ": "Michael",
  "Edad": 18, 
  "Documento": 2334857,
  "Ciudad en la que reside": "Palestina",
}
print(info)
[output] {'Nombre ': 'Michael', 'Edad': 18, 'Documento': 2334857, 'Ciudad en la que reside': 'Palestina'}

## Tomando decisiones
Aquí entraremos al tema de los ciclos, loop y sentencias (if, for, break, continue, while).

### Sentencia if
En Python podemos insertar diferentes condiciones lógicas como:

Igual a: x == y

Diferente de: x != y

Mayor que: x > y

Menor que: x < y

Mayor o igual que: x >= y

Menor o igual que: x <= y

Estas condiciones se pueden usar de varias maneras, más comúnmente en "sentencias if" y “bucles”.

La "sentencia if" se escribe utilizando la palabra clave “if”, esta es una palabra reservada de Python.

La palabra clave “elif” es la forma de Python de decir "si la condición anterior no fue cierta, intente con esta condición".

Además, para cerrar la “sentencia if” tenemos la instrucción “else”, que en los últimos de los casos si las condiciones anteriores no se cumplieron esta da por hecha la respuesta correcta.

Al momento de ejecutarse el programa con la “sentencia if”, sólo se ejecutará si es verdadera la condición.

Ejemplo:
```Python
x= 14
y= 11

if x > y:
    print ('El mayor es: ', x)
    if x%2 == 0:
        print (x, "es un numero par")

    else:
        print (x, "es un numero impar")
 
else: 
    print ('El mayor es', y)
    if y%2 == 0:
        print (y, "es un numero par")

    else:
        print (y, "es un numero impar")
```

### Ciclo For
Un bucle For se usa para iterar sobre una secuencia (es decir, una lista, una tupla, un diccionario, un conjunto o una cadena), dependiendo de los elementos que haya o el rango que se establezca serán la cantidad de veces que se repita, el elemento puede estar compuesto por cualquier dato, no importa si son str, int o float lo único que tomará en cuenta será la cantidad de elementos que haya.

Ejemplo:
```Python
lista = [1,2,3,'holeup']
for i in lista:
    print('elemento:',i)
[output]
elemento: 1
elemento: 2
elemento: 3
elemento: holeup
```

### Ciclo While
Con el bucle while podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera.

Ejemplo:
```Python
a = 2  
while a < 6:  
  print(a)  
  a += 1
[output]
2
3
4
5
```
### Break
“Break” es una palabra reservada y sirve para romper un ciclo.

Ejemplo:
```Python
contador = 0
for i in range(10):
        contador +=1
        print('i: ', i)
        if contador > 5:
            break
print('Contador: ', contador)
[output]
i:  0
i:  1
i:  2
i:  3
i:  4
i:  5
Contador:  6
```
### Continue
La sentencia “continue” es una palabra reservada, nos permite modificar el comportamiento de los ciclos. Continue se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar. No romperá el ciclo solo saltará el código pendiente.

Ejemplo:
```Python
k = 0
for i in range(10):
    k += 2
    if 2 <= k <=6:
        continue
    print('i: ', i, '|', 'El valor de k: ', k)
[output]
i:  3 | El valor de j:  8
i:  4 | El valor de j:  10
i:  5 | El valor de j:  12
i:  6 | El valor de j:  14
i:  7 | El valor de j:  16
i:  8 | El valor de j:  18
i:  9 | El valor de j:  20
```
