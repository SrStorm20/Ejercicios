from modulos import ingresar_entero

def main():
    numero1 = ingresar_entero("Ingrese el primer numero: ")
    numero2 = ingresar_entero("Ingrese el segundo numero (debe ser mayor que el primero): ")
    numero2 = mayor_que_uno(numero1, numero2)
    primos = encontrar_primos(numero1, numero2)
    mensaje = generar_mensaje(primos)
    mostrar_mensaje(mensaje)

def mayor_que_uno(numero1, numero2):
    while numero1 >= numero2:
        numero2 = ingresar_entero("\nIngrese el segundo numero (debe ser mayor que el primero): ")
    return numero2

def encontrar_primos(numero1, numero2):
    primos = 0
    while numero1 <= numero2:
        primo = True
        rango1 = 2
        rango2 = numero1 ** 0.5
        while rango1 <= rango2:
            if numero1 % rango1 == 0:
                primo = False
                break
            rango1 += 1
        if primo == True and not numero1 == 1:
            print(f"El numero {numero1} es primo")
            primos += 1
        else:
            print(f"El numero {numero1} no es primo")
        numero1 += 1
    return primos

def generar_mensaje(primos):
    mensaje = f"El total de numeros primos en el intervalo es de {primos}"
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)

main()
