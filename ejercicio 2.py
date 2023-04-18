from modulos import ingresar_entero

def main ():
    numero1 = ingresar_entero("Ingrese el primer numero: ")
    numero2 = ingresar_entero ("Ingrese el segundo numero (debe ser mayor que el primero): ")
    numero2 = mayor_que_uno(numero1, numero2)
    multiplos = imprimir_numeros (numero1, numero2)
    mensaje = generar_mensaje (multiplos)
    mostrar_mensaje (mensaje)




def mayor_que_uno(numero1, numero2):
    while numero1 >= numero2:
        numero2 = ingresar_entero ("\nIngrese el segundo numero (debe ser mayor que el primero): ")
    return numero2


def imprimir_numeros (numero1, numero2):
    multiplos = 0
    while numero1 <= numero2:
        numero1_str = str(numero1)
        suma = 0
        suma_digitos = ""
        for digito in numero1_str:
            digito_int = int(digito)
            suma += digito_int
            suma_digitos += f"{digito_int} + "

        if numero1 % 3 == 0:
            print(f"{suma_digitos}\b\b = {suma} es múltiplo de 3")
            multiplos += 1
        else: 
            print(f"{suma_digitos}\b\b = {suma} no es múltiplo de 3")
        numero1 += 1
    return multiplos


def generar_mensaje(multiplos):
    mensaje = f"El total de multiplos de tres en el intervalo es de {multiplos}"
    return mensaje

def mostrar_mensaje(mensaje):
    print(mensaje)


main()