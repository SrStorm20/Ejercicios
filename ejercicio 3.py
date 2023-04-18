from modulos import mostrar_mensaje, verificar_entrada

def main ():
    numero1 = verificar_entrada("Ingrese el primer numero: ",0)
    numero2 = verificar_entrada ("Ingrese el segundo numero (debe ser mayor que el primero): ", numero1)
    multiplos = imprimir_multiplos (numero1, numero2)
    mensaje = generar_mensaje (multiplos)
    mostrar_mensaje (mensaje)





def imprimir_multiplos (numero1, numero2):
    multiplos = 0
    while numero1 <= numero2:
        if numero1 % 5 == 0 and numero1 % 2 == 0:
            print(f"{numero1} es múltiplo par de 5")
            multiplos += 1
        else: 
            print(f"{numero1} no es múltiplo par de 5")
        numero1 += 1
    return multiplos





def generar_mensaje(multiplos):
    mensaje = f"El total de multiplos pares de cinco en el intervalo es de {multiplos}"
    return mensaje

main()