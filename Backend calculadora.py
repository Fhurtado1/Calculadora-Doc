# Aplicación de calculadora en Python

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("Error: División por cero")
        return
    return a / b

opcion = 0
while opcion != 5:
    print("\nAplicación de Calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = int(input("Seleccione una opción (1-5): "))

    if opcion == 1:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = suma(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = resta(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 3:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = multiplicacion(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == 4:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = division(num1, num2)
        if resultado != None:
            print("El resultado de la división es:", resultado)
    elif opcion == 5:
        print("Gracias por utilizar la aplicación de Calculadora.")
    else:
        print("Opción inválida, por favor seleccione una opción válida (1-5).")
