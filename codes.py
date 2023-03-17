from math import *
import os
from statistics import mode
from datetime import datetime


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

# 1. Imprime "Hola, mundo!" en la consola.
def greeting():
    clear()
    print("Hola, mundo! \n")
# 2. Calcula la suma de dos números ingresados por el usuario.
def sum_numbers():
    clear()
    print("Suma \n")
    x = float(input("Ingrese el primer numero: "))
    y = float(input("Ingrese el segundo numero: "))
    print(f"Resultado: {int(x)} + {int(y)} = {int(x+y)}")
# 3. Convierte grados Celsius a Fahrenheit.
def celsius_fahrenheit():
    clear()
    print("Celsius a Fahrenheit \n")
    x = int(input("Ingrese los grados celsius: "))
    result = x * 9/5 + 32
    print(f"Resultado: {str(x) + '°C' } = {str(result) + '°F'}")

# 4. Crea una función que calcule el área de un círculo.
def area_circle():
    clear()
    print("Area de un circulo \n")
    r = int(input("Ingrese el radio del circulo: "))
    area = pi * r**2
    print(f"Resultado: {r} = {str(area.__round__(2)) + ' cm^2'}")

# 5. Crea una lista de números y ordena la lista de mayor a menor.
def list_numbers():
    clear()
    print("Ordenar lista mayor a menor \n")
    num = [10, 25, 7, 30, 15, 4, 18, 9, 20, 13]
    print(f'Lista antes: {num}')
    num.sort(reverse=True)
    print(f'Lista despues: {num}')

# 6. Crea una función que determine si un número es par o impar.
def par_impar():
    clear()
    print("Par o Impar \n")
    x = int(input("Ingrese un numero: "))
    if x % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

# 7. Crea una función que calcule el factorial de un número.
def factorial_num():
    clear()
    print("Calcule el factorial \n")
    num = int(input("Ingrese un numero: "))
    if num == 0:
        return print(1)
    else:
        return print(num * factorial(num - 1))

# 8. Crea un programa que encuentre el máximo y mínimo de una lista de números.


def max_and_min():
    clear()
    print("Numero maximo y el minimo \n")
    lista = []
    num = int(input("Ingrese el tamaño de la lista: "))
    for i in range(1, num):
        addNum = int(input("Ingrese un numero: "))
        lista.append(addNum)
    print("El número máximo es:", max(lista))
    print("El número mínimo es:", min(lista))

# 9. Crea un programa que encuentre la longitud de una cadena de caracteres.


def len_characts():
    clear()
    print("Longitud de un caracter \n")
    x = input("Ingrese una palabra: ")
    print(f"Esta palabra tiene: {len(x)} caracteres")

# 10. Crea una función que determine si una cadena de caracteres es un palíndromo.


def palindrome():
    clear()
    print("Palindromos \n")
    x = input("Ingrese una oracion o palabra: ").lower().replace(" ", "")
    if x == x[::-1]:
        print("Es un palindromo")
    else:
        print("No es un palindromo")

# 11. Crea un programa que determine si un número es primo.


def num_primo():
    clear()
    print("Numeros primos \n")
    num = int(input("Ingresa un número entero positivo: "))
    primos = True
    if num < 2:
        primos = False
    else:
        for i in range(2, num):
            if num % i == 0:
                primos = False
                break
    if primos:
        print(num, "es un numero primo")
    else:
        print(num, "no es un numero primo")

# 12. Crea una función que determine si dos cadenas de caracteres son anagramas.


def anagram():
    clear()
    print("Anagramas \n")
    string1 = input("Ingrese una palabra: ").replace(" ", "").lower()
    string2 = input("Ingrese otra palabra: ").replace(" ", "").lower()
    if len(string1) != len(string2):
        print("La palabras deben ser del mismo tamaño!")
    else:
        list1 = list(string1)
        list2 = list(string2)
        list1.sort()
        list2.sort()
        if list1 == list2:
            print("Es un anagrama")
        else:
            print("No es un anagrama")

# 13. Crea un programa que calcule la suma de los dígitos de un número.


def sum_digit():
    clear()
    print("Suma de los digitos de un número \n")
    num = input("Ingrese un número o una sucecion de números: ")
    suma = 0
    for i in num:
        suma += int(i)
    print("La suma de los dígitos de", num, "=", suma)

# 14. Crea una función que calcule la raíz cuadrada de un número.


def square_root():
    clear()
    print("Raíz cuadrada \n")
    num = int(input("Ingrese un numero positivo: "))
    if num < 0 or num == 0:
        print("El numero debe ser mayor a 0!")
    else:
        raiz = sqrt(num)
        print(f"Resultado: {num} = {raiz}")

# 15:  Crea un programa que calcule el área y perímetro de un rectángulo.


def area_perimeter():
    clear()
    print("Area y perimetro \n")
    x = int(input("Ingrese la longitud: "))
    y = int(input("Ingrese el ancho: "))
    area = x * y
    perimeter = (2*x) + (2*y)
    print("Resultados:")
    print(f"Area: {area}")
    print(f"Perimetro: {perimeter}")

# 16:  Crea una función que calcule el área de un triángulo.


def area_triangle():
    clear()
    print("Area de un triangulo \n")
    b = float(input("Ingrese la base del triangulo: "))
    h = float(input("Ingrese la altura del triangulo: "))
    area = (b * h) / 2
    print(f"Resultado: {int(area)}")

# 17:  Crea un programa que calcule la media, mediana y moda de una lista de números.


def med_median_moda():
    clear()
    print("Media, Mediana y Moda de una lista \n")
    lista = []
    count = int(input("Ingrese el tamaño de la lista: "))
    count += 1
    for a in range(1, count):
        add = int(input(f"Ingrese el numero {a}:"))
        lista.append(add)
    suma = 0
    for i in lista:
        suma += i
    lon = len(lista)
    lista.sort()
    mitad = int(lon / 2)
    if lon % 2 == 0:
        mediana = (lista[mitad - 1] + lista[mitad]) / 2
    else:
        mediana = lista[mitad]
    print(lista)
    print(f"Media: {suma / lon}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {mode(lista)}")

# 18:  Crea un programa que convierta una cadena de caracteres a mayúsculas.


def uppercase():
    clear()
    print("Mayusculas \n")
    caracter = input("Ingrese una palabra o oracion: ")
    caracter = caracter.upper()
    print(f"Resultado: {caracter}")

# 19:  Crea una función que determine si una cadena de caracteres es un palíndromo (versión sin espacios).


def duplicate_palindrome():
    clear()
    palindrome()

# 20:  Crea una función que calcule el número de veces que un carácter aparece en una cadena de caracteres.


def count_charact():
    clear()
    print("Caracteres en una texto \n")
    cadena = input("Ingrese una palabra o oracion: ")
    caracter = input("Ingrese un caracter de dicha palabra o oracion: ")
    count = 0
    for c in cadena:
        if c == caracter:
            count += 1
    print(f"Hay {count} '{caracter}' en el texto")

# 21:  Crea un programa que calcule la suma de una serie de números ingresados por el usuario.


def sum_list():
    clear()
    print("Suma de una serie de números \n")
    numbers = input("Ingresa una serie de números separados por comas: ")
    numberList = numbers.split(",")
    suma = 0
    for number in numberList:
        suma += float(number)
    print("La suma de los números es:", suma)

# 22:  Crea una función que convierta una cadena de caracteres a minúsculas.


def lowercase():
    clear()
    print("Minusculas \n")
    cadena = input("Ingrese una texto: ")
    print(f"Resultado: {cadena.lower()}")

# 23:  Crea un programa que calcule la suma de los primeros n números naturales.


def nat_num():
    clear()
    print("los primeros n números naturales \n")
    n = int(input("Ingresa un número entero positivo: "))
    suma = 0
    for i in range(1, n+1):
        if n < 10:
            suma += i
        else:
            print("Debe ser entre el rango de numeros naturales")
            exit()
    print("La suma de los primeros", n, "números naturales es:", suma)

# 24:  Crea una función que calcule la distancia entre dos puntos en un plano cartesiano.


def cartesian_point():
    clear()
    print("Distancia ente puntos cartesiano \n")
    x1 = int(input("Ingrese x del primer punto: "))
    y1 = int(input("Ingrese y del primer punto: "))
    x2 = int(input("Ingrese x del segundo punto: "))
    y2 = int(input("Ingrese y del segundo punto: "))
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print(f"Resultado: {distancia}")

# 25:  Crea un programa que determine si un número es positivo, negativo o cero.


def pos_neg_zer():
    clear()
    print("Positivo, negtivo o cero \n")
    numero = float(input("Introduce un número: "))
    if numero > 0:
        print("El número es positivo.")
    elif numero < 0:
        print("El número es negativo.")
    else:
        print("El número es cero.")

# 26:  Crea una función que calcule el área de un cuadrado.


def area_square():
    clear()
    print("Area de un cuadrado \n")
    lado = int(input("Ingrese uno de los lados: "))
    area = lado**2
    print(f"El area del cuadrado es: {area}")

# 27:  Crea un programa que determine el número de días en un mes.


def month():
    clear()
    print("Dias en un mes \n")
    mes = int(input("Introduce el número del mes (1-12): "))
    if mes == 2:
        print("El mes de febrero tiene 28 o 29 días, dependiendo si es año bisiesto o no.")
    elif mes == 4 | mes == 6 | mes == 9 | mes == 11:
        print("El mes tiene 30 días.")
    else:
        print("El mes tiene 31 días.")

# 28.  Crea una función que determine si una cadena de caracteres contiene sólo letras.


def is_letter():
    clear()
    print("Caracteres contiene sólo letras \n")
    cadena = input("Ingrese un texto: ")
    if all(caracter.isalpha() for caracter in cadena):
        print("Contiene sólo letras")
    else:
        print("No contiene sólo letras")

# 29:  Crea un programa que calcule el factorial de un número usando recursión.


def factorial_recursive():
    clear()
    print("Factorial recursivo \n")
    n = int(input("Ingrese un numero: "))
    if n == 0:
        print("Resultado: 1")
    else:
        n = n * factorial(n-1)
        print(n)

# 30:  Crea una función que calcule la potencia de un número


def exponent():
    clear()
    print("Potencia \n")
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"Resultado: {base ** exponente}")

# 31:  Crea un programa que calcule el producto de dos matrices.


def matrix():
    clear()
    matriz1 = [[1, 2], [3, 4], [5, 6]]
    matriz2 = [[7, 8, 9], [10, 11, 12]]
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    filas2 = len(matriz2)
    columnas2 = len(matriz2[0])
    if columnas1 != filas2:
        return None
    resultado = [[0 for j in range(columnas2)] for i in range(filas1)]
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(filas2):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    if resultado is not None:
        for fila in resultado:
            print(fila)
    else:
        print("Las matrices no son compatibles para multiplicarse.")

# 32:  Crea una función que determine si una cadena de caracteres es un número.


def number_in_char():
    clear()
    print("Caracter es un numeron \n")
    char = input("Ingrese un texto o palabra: ")
    if not all(chars.isalpha() for chars in char):
        print(f"{char}: contiene numeros")
    else:
        print(f"{char} no contiene numeros")

# 33:  Crea un programa que calcule el número de vocales en una cadena de caracteres.


def sum_numbers_char():
    clear()
    print("Suma de vocales \n")
    char = input("Ingrese un texto o palabra: ")
    count = 0
    for letter in char:
        if letter.lower() in "aeiou":
            count += 1
    print(f"En '{char}' hay {count} vocales")

# 34:  Crea una función que calcule la suma de los números pares entre 1 y n.


def sum_numbers_pair():
    clear()
    print("Suma numeros pares entre 1 y n \n")
    num = int(input("Ingrese el valor de n: "))
    count = 0
    number_list = []
    for i in range(1, num + 1):
        if i % 2 == 0:
            count = count + i
            number_list.append(i)
    number_list = str(number_list).replace(
        ", ", " + ").replace("[", "").replace("]", "")
    print(f"Resultado: \n{number_list} = {count}")

# 35:  Crea un programa que calcule el área y perímetro de un círculo.


def area_perimeter_circle():
    clear()
    print("Area y perimetro de un circulo: \n")
    radio = float(input("Ingrese el radio: "))
    area = pi * radio ** 2
    perimeter = 2 * pi * radio
    print(f"Area del circulo: {area} \nPerimetro del circulo: {perimeter}")

# 36: Crea una función que determine si una cadena de caracteres es un pangrama.


def pangram():
    clear()
    print("Pangrama \n")
    cadena = input("Ingrese una palabra: ").lower()
    letras = set()
    for c in cadena:
        if c.isalpha():
            letras.add(c)
    if len(letras) == 26:
        print("Es un pangrama")
    else:
        print("No es un pangrama")

# 37:  Crea un programa que determine el día de la semana dado un número del 1 al 7.


def day_in_week():
    clear()
    print("Días de la semana \n")
    day = int(input("Ingrese un numero del 1-7: "))
    days = {
        1: "Domingo",
        2: "Lunes",
        3: "Martes",
        4: "Miercoles",
        5: "Jueves",
        6: "Viernes",
        7: "Sabado",
    }
    if 7 >= day <= 1:
        if list(days.values())[day-1]:
            print(f"\n{list(days.values())[day-1]}")
    else:
        print("Opcion invalida, debe elejir un numero entre 1 y 7")

# 38:  Crea una función que calcule el número de días entre dos fechas.


def date_into_date():
    clear()
    print("Dias entre fechas \n")
    print("dd/mm/aaaa \n")
    formate = "%d/%m/%Y"
    date_one = input("Ingrese la primera fecha: ")
    date_two = input("Ingrese la segunda fecha: ")
    date_one_obj = datetime.strptime(date_one, formate)
    date_two_obj = datetime.strptime(date_two, formate)
    days_math = (date_one_obj - date_two_obj).days
    year = int(days_math / 365)
    mount = int((days_math % 365) / 30)
    day = int((days_math % 365) % 30)
    print(f"{year} años, {mount} meses, {day} dias")
    print(f"{abs(days_math)} dias")

# 39:  Crea un programa que calcule la suma de los dígitos de un número usando recursión.


def sum_recusive_number():
    clear()
    print("Suma de los dígitos de un número usando recursión \n")
    number = int(input("Ingrese un numero: "))
    number_tmp = number
    suma = 0
    while number > 0:
        suma += number % 10
        number //= 10
    print(f"La suma del digitos {number_tmp} es: {suma}")

# 40:  Crea una función que determine si un número es perfecto


def perfect_number():
    clear()
    print("El número es perfecto \n")
    number = int(input("Ingrese un numero: "))
    suma = 0
    for i in range(1, number):
        if number % i == 0:
            suma += i
    if suma == number:
        print("El", number, "es un número perfecto")
    else:
        print("El", number, "no es un número perfecto")

# 41: Pedirle al usuario que introduzca su nombre y después imprimir un mensaje de bienvenida personalizado.


def greeting_custom():
    clear()
    print("bienvenida personalizada \n")
    nombre = input("Ingresa tu nombre: ")
    mensaje = "Hola, {0}! ¡Bienvenido a mi programa de Python!".format(nombre)
    print(mensaje)

# 42:  Convertir una temperatura en grados Celsius a Fahrenheit.


def duplicate_celsius_fahrenheit():
    clear()
    celsius_fahrenheit()

# 43:  Calcular el área de un círculo a partir del radio introducido por el usuario.


def duplicate_area_circle():
    clear()
    area_circle()

# 44:  Pedirle al usuario que introduzca un número y determinar si es par o impar.


def duplicate_par_impar():
    clear()
    par_impar()

# 45:  Pedirle al usuario que introduzca dos números y calcular su suma, resta, multiplicación y división.


def math_machine():
    clear()
    print("Calculadora \n")
    number_one = float(input("Ingrese un numero: "))
    number_two = float(input("Ingrese otro numero: "))
    suma = number_one + number_two
    resta = number_one - number_two
    mult = number_one * number_two
    div = number_one / number_two
    print("\nResultados: \n")
    print(
        f"Suma: {suma} \nResta: {resta} \nMultiplicacion: {mult} \nDivicion: {div}")

# 46:  Calcular el promedio de una lista de números introducida por el usuario.


def promedius_in_list():
    clear()
    print("Calcular el promedio de una lista \n")
    nums = []
    while True:
        try:
            num = float(
                input("Ingresa un número (o cualquier letra para finalizar): "))
            nums.append(num)
        except:
            break
    result = sum(nums) / len(nums)
    print("El promedio de los números ingresados es:", result)

# 47: Pedirle al usuario que introduzca una cadena de texto y después imprimir la cadena al revés.


def reverse_text():
    clear()
    print("Palabras al revez \n")
    text = input("Ingrese una o varias palabras: ")
    print("Resultado:", text[::-1])

# 48:  Pedirle al usuario que introduzca una lista de números y después imprimir la lista ordenada de menor a mayor.


def list_num_insert():
    clear()
    print("Lista ordenada 2.0v \n")
    number = input("Ingrese una lista de numeros separados: ")
    nums = [int(num) for num in number.split(",")]
    result = sorted(nums)
    print(f"Lista antes: {number} \nLista despues: {result}")

# 49:  Imprimir todos los números pares del 0 al 100.


def pair_in_hundre():
    clear()
    print("Pares entre 1 y 100 \n")
    for i in range(0, 101, 2):
        print(i)

# 50:  Imprimir todos los números impares del 0 al 100


def impair_in_hundre():
    clear()
    print("Impares entre 1 y 100 \n")
    for i in range(1, 101, 2):
        print(i)

# 51:  Imprimir todos los números primos del 0 al 100.


def primos():
    clear()
    print("Numeros Primos \n")
    for i in range(2, 101):
        isPrimo = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                isPrimo = False
                break
        if isPrimo:
            print(i)

# 52:  Calcular el factorial de un número introducido por el usuario.


def duplicate_factorial():
    clear()
    factorial()

# 53:  Imprimir la tabla de multiplicar de un número introducido por el usuario.


def table_mutiplication():
    clear()
    print("Tabla de multiplicacion \n")
    num = int(input("Ingrese un numero: "))
    print("Tabla de multiplicacion: \n")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")

# 54:  Pedirle al usuario que introduzca una lista de números y después encontrar el número más grande y el número más pequeño.


def max_min_nums():
    clear()
    print("Lista de numeros \n")
    numeros = input("Ingrese una lista de números separados por espacios: ")
    numeros = [int(num) for num in numeros.split()]
    maximo = numeros[0]
    minimo = numeros[0]
    for num in numeros:
        if num > maximo:
            maximo = num
        elif num < minimo:
            minimo = num
    print("El número más grande es:", maximo)
    print("El número más pequeño es:", minimo)

# 55: Pedirle al usuario que introduzca una cadena de texto y después imprimir la cantidad de veces que aparece cada letra en la cadena.


def text_cand():
    clean()
    print("Cantidad de veces que aparece una letra \n")
    text = input("Ingrese una cadena de texto: ")
    count = {}
    for letter in text:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter, counter in count.items():
        print(letter, counter)

# 56: Pedirle al usuario que introduzca una cadena de texto y después imprimir cuántas palabras hay en la cadena.


def cand_word():
    clear()
    print("Cantidad de palabras \n")
    text = input("Ingrese una cadena de texto: ")
    words = text.split()
    num_words = len(words)
    print(f"Hay {num_words} palabras de la cadena.")

# 57:  Pedirle al usuario que introduzca una lista de números y después imprimir la media, mediana y moda.


def duplicate_med_median_moda():
    clear()
    med_median_moda()

# 58:  Imprimir la serie de Fibonacci hasta el número introducido por el usuario.


def fib_do_num():
    clear()
    print("Sucesion de fibonacci \n")
    num = int(input("Ingrese un numero: "))
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    print(f"Serie de Fibonacci hasta {num}:")
    for num in fib:
        print(num, end=' ')

# 59:  Pedirle al usuario que introduzca dos números y después intercambiar sus valores sin usar una variable temporal.


def two_numbers():
    clear()
    print("Intercambio de variables \n")
    number_one = int(input("ingrese un numeros: "))
    number_two = int(input("Ingrese otro numero: "))
    print(f"a: {number_one} \nb: {number_two}")
    number_one,
    number_two = number_two, number_one
    print(f"a: {number_one} \nb: {number_two}")

# 60:  Pedirle al usuario que introduzca una cadena de texto y después imprimir si es un palíndromo o no.


def duplicate_palindrome_two():
    clear()
    palindrome()

# 61:  Pedirle al usuario que introduzca una lista de números y después imprimir cuántos son pares y cuántos son impares.


def duplicate_par_impar():
    clear()
    par_impar()

# 62:  Pedirle al usuario que introduzca una cadena de texto y después imprimir cuántos dígitos, letras y caracteres especiales contiene.


def char_letter_symbols():
    clear()
    print("Dígitos, letras y caracteres especiales \n")
    text = input("ingrese un texto: ")
    num_char = 0
    num_letter = 0
    num_symbol = 0
    for i in text:
        if i.isdigit():
            num_char += 1
        elif i.isalpha():
            num_letter += 1
        else:
            num_symbol += 1
    print("\nLa cadena de texto tiene:")
    print(f"- {num_char} digitos \n- {num_letter} letras \n- {num_symbol} caracteres especiales")

# 63:  Pedirle al usuario que introduzca una lista de números y después imprimir sólo los números pares.


def num_pair():
    clear()
    print("Lista de números pares \n")
    entrada = input("Introduce una lista de números separados por comas: ")
    numeros = [float(num) for num in entrada.split(",")]
    numeros_pares = [num for num in numeros if num % 2 == 0]
    print("Los números pares de la lista son:", numeros_pares)

# 64:  Pedirle al usuario que introduzca una lista de números y después imprimir sólo los números impares.


def num_impair():
    clear()
    print("Lista de números impares \n")
    entrada = input("Introduce una lista de números separados por comas: ")
    numeros = [float(num) for num in entrada.split(",")]
    numeros_impares = [num for num in numeros if num % 2 != 0]
    print("Los números impares de la lista son:", numeros_pares)

# 65:  Pedirle al usuario que introduzca una lista de números y después imprimir la suma de los números pares y la suma de los números impares.


def sum_impair_pair():
    clear()
    print("Suma de numeros pares e impares \n")
    num = input("Ingrese una lista de numeros separados por coma: ")
    nums = [float(i) for i in num.split(",")]
    count_pair = 0
    count_impair = 0
    for i in nums:
        if i % 2 == 0:
            count_pair += i
        elif i % 2 != 0:
            count_impair += i
    print(
        f"La suma de numeros pares es: {count_pair} \nLa suma de numeros impares es: {count_impair}")

# 66:  Pedirle al usuario que introduzca una lista de números y después imprimir la lista sin duplicados.


def isduplicate_list():
    clear()
    print("Lista sin duplicados \n")
    num = input("Ingrese una lista de numeros separados por coma: ")
    nums = [int(i) for i in num.split(",")]
    result = list(set(nums))
    print(f"La lista sin duplicados es: {result}")

# 67:  Pedirle al usuario que introduzca una lista de números y después imprimir la lista invertida.


def invert_list():
    clear()
    print("Listas invertida \n")
    nums = input("Ingrese una lista de numeros separados por coma: ")
    list_num = [float(i) for i in nums.split(",")]
    list_num.reverse()
    print(f"Resultado: {list_num}")

# 68:  Pedirle al usuario que introduzca una lista de números y después imprimir la lista al revés pero manteniendo el orden de los elementos pares e impares.


def reverse_pair_list():
    clear()
    print("Lista invertida de pares e impares \n")
    entrada = input("Introduce una lista de números separados por comas: ")
    numeros = [float(num) for num in entrada.split(",")]
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    impares = list(filter(lambda x: x % 2 != 0, numeros))
    pares.reverse()
    impares.reverse()
    numeros_invertidos = []
    numeros_invertidos.extend(impares)
    numeros_invertidos.extend(pares)
    print("La lista invertida pero manteniendo el orden de los elementos pares e impares es:", numeros_invertidos)

# 69:  Pedirle al usuario que introduzca una lista de números y después imprimir la lista ordenada de mayor a menor.


def reverse_list():
    clear()
    print("Listas revertida \n")
    entrada = input("Introduce una lista de números separados por comas: ")
    numeros = [float(num) for num in entrada.split(",")]
    numeros.sort(reverse=True)
    print(f"La lista ordenada de mayor a menor es: \n{numeros}")

# 70:  Pedirle al usuario que introduzca una lista de números y después imprimir sólo los números mayores que 10.

def max_ten_list():
    clear()
    print("Lista de numeros mayores a 10 \n")
    entrada = input("Introduce una lista de números separados por comas: ")
    numeros = [float(num) for num in entrada.split(",")]
    max_ten = [ num for num in numeros if num > 10 ]
    print(f'Los números mayores que 10 son: \n{max_ten}')

# 71:  Realizar la suma de dos números enteros uno negativo y uno positivo.


def sum_pos_neg():
    clear()
    print("Suma de un numero negativo y un positivo \n")
    a = -5
    b = 10
    print(f"La suma de {a} y {b} dan como resultado {a+b}")

# 72:  Mostrar el resultado de la multiplicación de dos números enteros.


def mult_int():
    clear()
    print("Multiplicacion de dos numeros enteros \n")
    a = 5
    b = 10
    print(f"Al multiplicar el numero {a} y {b} da como resultado {a*b}")

# 73:  Mostrar el cociente de dos números enteros.


def cocient():
    clear()
    print("Concinte de dos numeros entero \n")
    a = 25
    b = 4
    cociente = a // b
    print(f"El cociente de {a} entre {b} es: {cociente}")

# 74:  Mostrar el residuo de dos números enteros.


def reciduct():
    clear()
    print("Reciduo de dos numeros entero \n")
    a = 25
    b = 4
    cociente = a % b
    print(f"El reciduo de {a} entre {b} es: {cociente}")

# 75:  Realizar la suma de dos números reales.


def sum_real():
    clear()
    print("Suma de numeros reales \n")
    a = 3.14
    b = 2.71
    suma = a + b
    print("La suma de", a, "y", b, "es:", suma)

# 76:  Mostrar el resultado de la multiplicación de dos números reales.


def mult_real():
    clear()
    print("Multiplicacion de numeros reales \n")
    a = 3.14
    b = 2.71
    producto = a * b
    print("El producto de", a, "y", b, "es:", producto)

# 76:  Mostrar el resultado de la multiplicación de dos números reales.


def concat():
    clear()
    print("Concatenar \n")
    cadena1 = "Hola "
    cadena2 = "mundo!"
    saludo = cadena1 + cadena2
    print(saludo)

# 78:  Mostrar la longitud de una cadena.


def duplicate_len_charact():
    clear()
    print("Longituda de una cadena \n")
    print(f'La cadena "Hola mundo!" tiene: {len("Hola mundo!")} de longitud.')

# 79:  Mostrar el primer carácter de una cadena.


def firth_character():
    clear()
    print("Primera letra \n")
    print("Hola mundo!")
    print("Hola mundo"[0])

# 80:  Mostrar el último carácter de una cadena.


def final_character():
    clear()
    print("Ultima letra \n")
    print("Hola mundo!")
    print("Hola mundo"[-1])

# 81:  Mostrar los primeros 5 caracteres de una cadena.


def five_firth_characters():
    clear()
    print("Primeras 5 letras \n")
    print("Hola mundo!")
    print("Hola mundo"[:5])

# 82:  Mostrar los últimos 5 caracteres de una cadena.


def five_final_characters():
    clear()
    print("Ultimas 5 letras \n")
    print("Hola mundo!")
    print("Hola mundo"[-5:])

# 83:  Mostrar el número de veces que aparece una letra en una cadena.


def num_letters_in_characters():
    clear()
    print("Contador de letra en una cadena \n")
    cadena = "Hola mundo!"
    letra = "o"
    num_ocurrencias = cadena.count(letra)
    print("El número de veces que la letra", letra, "aparece en la cadena es:", num_ocurrencias)

# 84:  Mostrar el número de veces que aparece una palabra en una cadena.


def num_word_in_text():
    clear()
    print("Contador de palabras en una cadena \n")
    cadena = "Hola mundo! Hola a todos en el mundo!"
    palabra = "Hola"
    num_ocurrencias = cadena.count(palabra)
    print("El número de veces que la palabra", palabra, "aparece en la cadena es:", num_ocurrencias)

# 85:  Mostrar el resultado de la operación lógica "AND" de dos variables booleanas.


def and_logic():
    clear()
    print("AND \n")
    a = True
    b = False
    resultado = a and b
    print(resultado)

# 86:  Mostrar el resultado de la operación lógica "OR" de dos variables booleanas.


def or_logic():
    clear()
    print("OR \n")
    a = True
    b = False
    resultado = a or b
    print(resultado)

# 87:  Mostrar el resultado de la operación lógica "NOT" de una variable booleana.


def not_logic():
    clear()
    print("NOT \n")
    a = True
    resultado = not a
    print(resultado)

# 88:  Realizar la suma de todos los elementos de un arreglo de números enteros.


def sum_array():
    clear()
    print("Suma de un arreglo de enteros \n")
    arreglo = [2, 4, 6, 8, 10]
    suma = 0
    for elemento in arreglo:
        suma += elemento
    print("La suma de los elementos es:", suma)

# 89:  Mostrar el promedio de un arreglo de números enteros.


def promd_array():
    clear()
    print("Promedio de un arreglo de enteros \n")
    arreglo = [2, 4, 6, 8, 10]
    suma = 0
    for i in arreglo:
        suma += i
    promd = suma / len(arreglo)
    print(f"El promedio es: {promd}")

# 90:  Mostrar el número más grande y el más pequeño de un arreglo de números enteros.


def max_and_min_list():
    clear()
    print("Número más grande y el más pequeño de un arreglo \n")
    numeros = [2, 4, 6, 8, 10]
    print(numeros, '\n')
    maximo = numeros[0]
    minimo = numeros[0]
    for num in numeros:
        if num > maximo:
            maximo = num
        elif num < minimo:
            minimo = num
    print("El número más grande es:", maximo)
    print("El número más pequeño es:", minimo)

# 91:  Ordenar un arreglo de números enteros de forma ascendente.


def array_asd_int():
    clear()
    print("Arreglo de números enteros de forma ascendente \n")
    arreglo = [9, 5, 7, 2, 1, 8, 4, 6, 3]
    print("El arreglo desornado es:", arreglo)
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    print("El arreglo ordenado es:", arreglo)

# 92:  Ordenar un arreglo de números enteros de forma descendente.


def array_des_int():
    clear()
    print("Arreglo de números enteros de forma descendente \n")
    arreglo = [9, 5, 7, 2, 1, 8, 4, 6, 3]
    print("El arreglo desornado es:", arreglo)
    n = len(arreglo)
    for i in range(n):
        for j in range(0, n-i-1):
            if arreglo[j] < arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    print("El arreglo ordenado es:", arreglo)

# 93:  Mostrar los elementos de un arreglo de números enteros que son pares.


def array_int_pair():
    clear()
    print("Enteros pares de un arreglo: \n")
    arreglo = [9, 5, 7, 2, 1, 8, 4, 6, 3]
    for i in arreglo:
        if i % 2 == 0:
            print(i)

# 94:  Mostrar los elementos de un arreglo de números enteros que son impares.


def array_int_impair():
    clear()
    print("Enteros impares de un arreglo: \n")
    arreglo = [9, 5, 7, 2, 1, 8, 4, 6, 3]
    for i in arreglo:
        if i % 2 != 0:
            print(i)

# 95:  Concatenar dos arreglos de cadenas.


def concat_array():
    clear()
    print("Concatenar dos arreglos de cadenas \n")
    arr1 = ["Hola"]
    arr2 = ["Mundo!"]
    print(arr1[0] + " " + arr2[0])

# 96:  Mostrar los elementos de un arreglo de cadenas que contienen una letra específica.


def search_in_array():
    clear()
    print("Arreglos que contienen una letra específica \n")
    arreglo = ["hola", "adios", "casa", "perro", "gato", "manzana"]
    letra = "a"
    for cadena in arreglo:
        if letra in cadena:
            print(cadena)

# 97:  Mostrar los elementos de un arreglo de cadenas que comienzan con una letra específica.


def search_in_array_init():
    clear()
    print("Arreglo de cadenas que comienzan con una letra específica \n")
    arreglo = ["hola", "adios", "casa", "perro", "gato", "amigo"]
    letra = "a"
    for cadena in arreglo:
        if cadena[0] == letra:
            print(cadena)

# 98:  Mostrar los elementos de un arreglo de cadenas que terminan con una letra específica.


def search_in_array_end():
    clear()
    print("Arreglo de cadenas que termina con una letra específica \n")
    arreglo = ["hola", "adios", "casa", "perro", "gato", "amigo"]
    letra = "a"
    for cadena in arreglo:
        if cadena[-1] == letra:
            print(cadena)

# 99:  Convertir una cadena en un arreglo de caracteres.


def convert_string_array():
    clear()
    print("Covertir una cadena en un arreglo \n")
    cadena = "Hola mundo"
    arreglo = []
    for caracter in cadena:
        arreglo.append(caracter)
    print(arreglo)