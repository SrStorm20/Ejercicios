from modulos import  mostrar_mensaje, verificar_entrada

MINIMO = 0
def main ():
    numero1 = verificar_entrada("Ingrese el primer numero: ", MINIMO)
    numero2 = verificar_entrada ("Ingrese el segundo numero (debe ser mayor que el primero): ", numero1)
    multiplos = imprimir_multiplos (numero1, numero2)
    mensaje = generar_mensaje (multiplos)
    mostrar_mensaje (mensaje)



def imprimir_multiplos (numero1, numero2):
    multiplos = 0
    while numero1 <= numero2:
        if numero1 % 3 == 0 or numero1 == 1:
            print(f"{numero1} es multiplo de 3")
            multiplos +=1
        else: 
            print(f"{numero1} no es multiplo de 3")
        numero1 += 1
    return multiplos

def generar_mensaje(multiplos):
    mensaje = f"El total de multiplos de tres en el intervalo es de {multiplos}"
    return mensaje




main()