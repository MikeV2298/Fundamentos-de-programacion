### Nombre: Michael Alexander Chango Burgos
### Carrera: Sistema de Información
### Paralelo: SIN-S-MA-1-1 VAN20

# Proyecto de Fundamentos de la programación.

# ¿Qué es Python?🐍 
Es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. Trata de un lenguaje interpretado, es decir, que no es necesario compilarlo para ejecutar las aplicaciones escritas en Python, sino que se ejecutan directamente por el ordenador utilizando un programa denominado interpretador, por lo que no es necesario “traducirlo” a lenguaje máquina. 

Su filosofía hace hincapié en la legibilidad de su código, PYTHON es un lenguaje de programación multiparadigma, ya que soporta Programación Orientada a Objetos, Programación imperativa y en menor medida Programación Funcional. El creador de PYTHON es Guido Van Rossum.

Python ha ido ganando adeptos gracias a su sencillez y a sus amplias posibilidades, sobre todo en los últimos años, ya que facilita trabajar con inteligencia artificial, big data, machine learning y data science, entre muchos otros campos en auge.
![Uploading image.png…]()

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
Además de asignar variables también haremos uso de la función “print”, esta permite imprimir el dato por medio de consola, ya sea para imprimir la variable o imprimir algo directamente, por ejemplo:
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
print(“Hello World”)
[output] Hello World

print(“…”)
[output] …
```
Además de esto también podemos guardar un dato en una variable la cuál será ingresada por el usuario por medio del teclado y esta puede pedir números o palabras. Para esto es necesario de usar la función “input”, esta función permite obtener el texto escrito por el usuario, el cual se asignará a un espacio de memoria con el nombre que el programador vea conveniente. Y ya sea si se ingresa un número entero o decimal se hace uso del “int” o ”float”.
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
