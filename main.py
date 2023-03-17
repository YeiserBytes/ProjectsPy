from codes import *
from time import sleep

main_menu = {
    1: greeting,
    2: sum_numbers,
    3: celsius_fahrenheit,
    4: area_circle,
    5: list_numbers,
    6: par_impar,
    7: factorial_num,
    8: max_and_min,
    9: len_characts,
    10: palindrome,
    11: num_primo,
    12: anagram,
    13: sum_digit,
    14: square_root,
    15: area_perimeter,
    16: area_triangle,
    17: med_median_moda,
    18: uppercase,
    19: duplicate_palindrome,
    20: count_charact,
    21: sum_list,
    22: lowercase,
    23: nat_num,
    24: cartesian_point,
    25: pos_neg_zer,
    26: area_square,
    27: month,
    28: is_letter,
    29: factorial_recursive,
    30: exponent,
    31: matrix,
    32: number_in_char,
    33: sum_numbers_char,
    34: sum_numbers_pair,
    35: area_perimeter_circle,
    36: pangram,
    37: day_in_week,
    38: date_into_date,
    39: sum_recusive_number,
    40: perfect_number,
    41: greeting_custom,
    42: duplicate_celsius_fahrenheit,
    43: duplicate_area_circle,
    44: duplicate_par_impar,
    45: math_machine,
    46: promedius_in_list,
    47: reverse_text,
    48: list_num_insert,
    49: pair_in_hundre,
    50: impair_in_hundre,
    51: primos,
    52: duplicate_factorial,
    53: table_mutiplication,
    54: max_min_nums,
    55: text_cand,
    56: cand_word,
    57: duplicate_med_median_moda,
    58: fib_do_num,
    59: two_numbers,
    60: duplicate_palindrome_two,
    61: duplicate_par_impar,
    62: char_letter_symbols,
    63: num_pair,
    64: num_impair,
    65: sum_impair_pair,
    66: isduplicate_list,
    67: invert_list,
    68: reverse_pair_list,
    69: reverse_list,
    70: max_ten_list,
    71: sum_pos_neg,
    72: mult_int,
    73: cocient,
    74: reciduct,
    75: sum_real,
    76: mult_real,
    77: concat,
    78: duplicate_len_charact,
    79: firth_character,
    80: final_character,
    81: five_firth_characters,
    82: five_final_characters,
    83: num_letters_in_characters,
    84: num_word_in_text,
    85: and_logic,
    86: or_logic,
    87: not_logic,
    88: sum_array,
    89: promd_array,
    90: max_and_min_list,
    91: array_asd_int,
    92: array_des_int,
    93: array_int_pair,
    94: array_int_impair,
    95: concat_array,
    96: search_in_array,
    97: search_in_array_init,
    98: search_in_array_end,
    99: convert_string_array
}

# Main menu
while True:
    clear()
    print("======= Menu pricipal ======= \n")
    print("1. Ejercicios del 1 - 10")
    print("2. Ejercicios del 11 - 20")
    print("3. Ejercicios del 21 - 30")
    print("4. Ejercicios del 31 - 40")
    print("5. Ejercicios del 41 - 50")
    print("6. Ejercicios del 51 - 60")
    print("7. Ejercicios del 61 - 70")
    print("8. Ejercicios del 71 - 80")
    print("9. Ejercicios del 81 - 90")
    print("10. Ejercicios del 91 - 99")
    print("0. Salir")
    opc = input("Ingrese una opcion: ")
    if opc == "1": 
        clear()
        print("Ejercicios del 1 - 9 \n")
        print("1: Hola mundo \n2: Suma dos numeros \n3: Celsius a Fahrenheit \n4: Area de un Circulo \n5: Ordena lista \n6: Par o impar \n7: Factorial \n8: max y min de una lista \n9: Longitud cadena \n10. Palíndromo \n")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[1]()
            sleep(1)
        elif opca == "2":
            main_menu[2]()
            sleep(1)
        elif opca == "3":
            main_menu[3]()
            sleep(1)
        elif opca == "4":
            main_menu[4]()
            sleep(1)
        elif opca == "5":
            main_menu[5]()
            sleep(1)
        elif opca == "6":
            main_menu[6]()
            sleep(1)
        elif opca == "7":
            main_menu[7]()
            sleep(1)
        elif opca == "8":
            main_menu[8]()
            sleep(1)
        elif opca == "9":
            main_menu[9]()
            sleep(1)
        elif opca == "10":
            main_menu[10]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "2":
        clear()
        print("Ejercicios del 11 - 20 \n")
        print("1: Número primo \n2: Anagramas \n3: Suma de dígitos \n4: Raíz cuadrada \n5: Área y perímetro de rectángulo \n6: Área de triángulo \n7: Media, mediana y moda \n8: Mayúsculas \n9: Palíndromo sin espacios \n10: Contar caracteres \n")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[11]()
            sleep(1)
        elif opca == "2":
            main_menu[12]()
            sleep(1)
        elif opca == "3":
            main_menu[13]()
            sleep(1)
        elif opca == "4":
            main_menu[14]()
            sleep(1)
        elif opca == "5":
            main_menu[15]()
            sleep(1)
        elif opca == "6":
            main_menu[16]()
            sleep(1)
        elif opca == "7":
            main_menu[17]()
            sleep(1)
        elif opca == "8":
            main_menu[18]()
            sleep(1)
        elif opca == "9":
            main_menu[19]()
            sleep(1)
        elif opca == "10":
            main_menu[20]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "3":
        clear()
        print("Ejercicios del 21 - 30 \n")
        print("1: Suma de números \n2: Minúsculas \n3: Suma de n números \n4: Distancia entre puntos \n5: Positivo, negativo o cero \n6: Área de cuadrado \n7: Número de días en mes \n8: Solo letras \n9: Factorial con recursión \n10: Potencia \n")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[21]()
            sleep(1)
        elif opca == "2":
            main_menu[22]()
            sleep(1)
        elif opca == "3":
            main_menu[23]()
            sleep(1)
        elif opca == "4":
            main_menu[24]()
            sleep(1)
        elif opca == "5":
            main_menu[25]()
            sleep(1)
        elif opca == "6":
            main_menu[26]()
            sleep(1)
        elif opca == "7":
            main_menu[17]()
            sleep(1)
        elif opca == "8":
            main_menu[18]()
            sleep(1)
        elif opca == "9":
            main_menu[19]()
            sleep(1)
        elif opca == "10":
            main_menu[20]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "4":
        clear()
        print("Ejercicios del 31 - 40 \n")
        print("1: Producto de matrices")
        print("2: Es un número")
        print("3: Número de vocales")
        print("4: Suma de números pares")
        print("5: Área y perímetro de círculo")
        print("6: Pangrama")
        print("7: Día de la semana")
        print("8: Días entre fechas")
        print("9: Suma de dígitos con recursión")
        print("10: Número perfecto")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[31]()
            sleep(1)
        elif opca == "2":
            main_menu[32]()
            sleep(1)
        elif opca == "3":
            main_menu[33]()
            sleep(1)
        elif opca == "4":
            main_menu[34]()
            sleep(1)
        elif opca == "5":
            main_menu[35]()
            sleep(1)
        elif opca == "6":
            main_menu[36]()
            sleep(1)
        elif opca == "7":
            main_menu[37]()
            sleep(1)
        elif opca == "8":
            main_menu[38]()
            sleep(1)
        elif opca == "9":
            main_menu[39]()
            sleep(1)
        elif opca == "10":
            main_menu[40]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "5":
        clear()
        print("Ejercicios del 41 - 50 \n")
        print("1: bienvenida personalizada")
        print("2: Cersius a Fahrenheit")
        print("3: Area de un circulo")
        print("4: Números pares e impares")
        print("5: Calculadora")
        print("6: Calcular el promedio de una lista")
        print("7: Palabras al revez")
        print("8: Lista ordenada 2.0v")
        print("9: Pares entre 1 y 100")
        print("10: Impares entre 1 y 100")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[41]()
            sleep(1)
        elif opca == "2":
            main_menu[42]()
            sleep(1)
        elif opca == "3":
            main_menu[43]()
            sleep(1)
        elif opca == "4":
            main_menu[44]()
            sleep(1)
        elif opca == "5":
            main_menu[45]()
            sleep(1)
        elif opca == "6":
            main_menu[46]()
            sleep(1)
        elif opca == "7":
            main_menu[47]()
            sleep(1)
        elif opca == "8":
            main_menu[48]()
            sleep(1)
        elif opca == "9":
            main_menu[49]()
            sleep(1)
        elif opca == "10":
            main_menu[50]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "6":
        clear()
        print("Ejercicios del 51 - 60 \n")
        print("1: Numeros Primos")
        print("2: Factorial")
        print("3: Tabla de multiplicacion")
        print("4: Lista de numeros ")
        print("5: Cantidad de veces que aparece una letra")
        print("6: Cantidad de palabras")
        print("7: Media, Madiana y Moda")
        print("8: Sucesion de fibonacci")
        print("9: Intercambio de variables")
        print("10: Palindromos")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[51]()
            sleep(1)
        elif opca == "2":
            main_menu[52]()
            sleep(1)
        elif opca == "3":
            main_menu[53]()
            sleep(1)
        elif opca == "4":
            main_menu[54]()
            sleep(1)
        elif opca == "5":
            main_menu[55]()
            sleep(1)
        elif opca == "6":
            main_menu[56]()
            sleep(1)
        elif opca == "7":
            main_menu[57]()
            sleep(1)
        elif opca == "8":
            main_menu[58]()
            sleep(1)
        elif opca == "9":
            main_menu[59]()
            sleep(1)
        elif opca == "10":
            main_menu[60]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "7":
        clear()
        print("Ejercicios del 61 - 70 \n")
        print("1: Par e impar")
        print("2: Dígitos, letras y caracteres especiales")
        print("3: Lista de números pares")
        print("4: Lista de números impares ")
        print("5: Suma de numeros pares e impares")
        print("6: Lista sin duplicados")
        print("7: Listas invertida")
        print("8: Lista invertida de pares e impares")
        print("9: Listas revertida")
        print("10: Lista de numeros mayores a 10")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[61]()
            sleep(1)
        elif opca == "2":
            main_menu[62]()
            sleep(1)
        elif opca == "3":
            main_menu[63]()
            sleep(1)
        elif opca == "4":
            main_menu[64]()
            sleep(1)
        elif opca == "5":
            main_menu[65]()
            sleep(1)
        elif opca == "6":
            main_menu[66]()
            sleep(1)
        elif opca == "7":
            main_menu[67]()
            sleep(1)
        elif opca == "8":
            main_menu[68]()
            sleep(1)
        elif opca == "9":
            main_menu[69]()
            sleep(1)
        elif opca == "10":
            main_menu[70]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "8":
        clear()
        print("Ejercicios del 71 - 80 \n")
        print("1: Suma de un numero negativo y un positivo")
        print("2: Multiplicacion")
        print("3: Concinte de dos numeros")
        print("4: Reciduo de dos numeros")
        print("5: Suma de numeros reales")
        print("6: Multiplicacion de numeros reales")
        print("7: Concatenar")
        print("8: Longituda de una cadena")
        print("9: Primera letra")
        print("10: Ultima letra")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[71]()
            sleep(1)
        elif opca == "2":
            main_menu[72]()
            sleep(1)
        elif opca == "3":
            main_menu[73]()
            sleep(1)
        elif opca == "4":
            main_menu[74]()
            sleep(1)
        elif opca == "5":
            main_menu[75]()
            sleep(1)
        elif opca == "6":
            main_menu[76]()
            sleep(1)
        elif opca == "7":
            main_menu[77]()
            sleep(1)
        elif opca == "8":
            main_menu[78]()
            sleep(1)
        elif opca == "9":
            main_menu[79]()
            sleep(1)
        elif opca == "10":
            main_menu[80]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "9":
        clear()
        print("Ejercicios del 81 - 90 \n")
        print("1: Primeras 5 letras")
        print("2: Ultimas 5 letras")
        print("3: Contador de letra en una cadena")
        print("4: Contador de palabras en una cadena")
        print("5: AND")
        print("6: OR")
        print("7: NOT")
        print("8: Suma de un arreglo de enteros")
        print("9: Promedio de un arreglo de enteros")
        print("10: Número más grande y el más pequeño de un arreglo")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[81]()
            sleep(1)
        elif opca == "2":
            main_menu[82]()
            sleep(1)
        elif opca == "3":
            main_menu[83]()
            sleep(1)
        elif opca == "4":
            main_menu[84]()
            sleep(1)
        elif opca == "5":
            main_menu[85]()
            sleep(1)
        elif opca == "6":
            main_menu[86]()
            sleep(1)
        elif opca == "7":
            main_menu[87]()
            sleep(1)
        elif opca == "8":
            main_menu[88]()
            sleep(1)
        elif opca == "9":
            main_menu[89]()
            sleep(1)
        elif opca == "10":
            main_menu[90]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "10":
        clear()
        print("Ejercicios del 91 - 99 \n")
        print("1: Arreglo de números enteros de forma ascendente")
        print("2: Arreglo de números enteros de forma descendente")
        print("3: Enteros pares de un arreglo")
        print("4: Enteros impares de un arreglo")
        print("5: Concatenar dos arreglos de cadenas")
        print("6: Arreglos que contienen una letra específica")
        print("7: Arreglo de cadenas que comienzan con una letra específica")
        print("8: Arreglo de cadenas que termina con una letra específica")
        print("9: Covertir una cadena en un arreglo ")
        opca = input("Ingrese una opcion: ")
        if opca == "1":
            main_menu[91]()
            sleep(1)
        elif opca == "2":
            main_menu[92]()
            sleep(1)
        elif opca == "3":
            main_menu[93]()
            sleep(1)
        elif opca == "4":
            main_menu[94]()
            sleep(1)
        elif opca == "5":
            main_menu[95]()
            sleep(1)
        elif opca == "6":
            main_menu[96]()
            sleep(1)
        elif opca == "7":
            main_menu[97]()
            sleep(1)
        elif opca == "8":
            main_menu[98]()
            sleep(1)
        elif opca == "9":
            main_menu[99]()
            sleep(1)
        else:
            print("Su opcion es invalida!")
            sleep(1)
    elif opc == "0":
        exit()
    else:
        print("Opcion invalida!")
