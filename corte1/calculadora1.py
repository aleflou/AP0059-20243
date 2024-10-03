# Definir las funciones para las operaciones
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: División por cero"

# Función principal para ejecutar la calculadora
def calculadora():
    while True:
        # Solicitar al usuario los números
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        # Solicitar la operación al usuario
        print("¿Qué operación desea realizar?")
        print("Presione: \n S para sumar \n R para restar \n M para multiplicar \n D para dividir")
        operacion = input().upper()  # Convertimos la entrada a mayúscula para facilitar la comparación

        # Ejecutar la operación seleccionada
        if operacion == 'S':
            print("El resultado de la suma es:", suma(num1, num2))
        elif operacion == 'R':
            print("El resultado de la resta es:", resta(num1, num2))
        elif operacion == 'M':
            print("El resultado de la multiplicación es:", mult(num1, num2))
        elif operacion == 'D':
            print("El resultado de la división es:", div(num1, num2))
        else:
            print("Operación no válida")

        # Preguntar si desea continuar
        continuar = input("¿Desea realizar otra operación? (S/N): ").upper()
        if continuar != 'S':
            print("Gracias por usar la calculadora.")
            break

# Ejecutar la calculadora
calculadora()
