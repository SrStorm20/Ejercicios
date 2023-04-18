from modulos import verificar_validez_entero

VALOR_MINIMO = -5
VALOR_MAXIMO = 5

def main():
    mostrar_mensaje( f"Los numeros deben estar en un rango de {VALOR_MINIMO} a {VALOR_MAXIMO}")
    numero1 = verificar_validez_entero ("Ingrese el primer numero: ", VALOR_MINIMO, VALOR_MAXIMO)
    numero2 = verificar_validez_entero ("Ingrese el segundo numero: ", VALOR_MINIMO, VALOR_MAXIMO)
    suma1 = funcion_sin_nombre(numero1, numero2)
    suma2 = funcion_sin_nombre(numero2, numero1)
    mostrar_mensaje(suma1)
    mostrar_mensaje(suma2)


def funcion_sin_nombre(num1, num2):
    resultado = ""
    num2_positivo = abs(num2) # valor absoluto
    if num2 < 0:
        resultado += " - "
    resultado += str(num1)
    contadorProMAx = 1
    while contadorProMAx < num2_positivo:
        if num1 and num2 < 0:
            resultado += " - " + str(num1)
        else:
            resultado += " + " + str(num1)
        contadorProMAx += 1
    resultado += f" = {num1*num2} "
    return resultado


def mostrar_mensaje(mensaje):
    print("Hola mundo")

main()