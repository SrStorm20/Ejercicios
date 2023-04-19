from modulos import  mostrar_mensaje, verificar_entrada

MINIMO = 0
MULTIPLO = 5

def main ():
    numero1 = verificar_entrada("Ingrese el primer numero: ", MINIMO)
    numero2 = verificar_entrada ("Ingrese el segundo numero (debe ser mayor que el primero): ", numero1)
    lista = imprimir_multiplos (numero1, numero2)
    mostrar_mensaje (lista)

def imprimir_multiplos (numero1, numero2):
    multiplos = 0
    lista = ""
    i = numero1
    while i <= numero2:
        if i % MULTIPLO == 0 and i % 2 ==0:
            lista += f"{i} es multiplo par de 5\n"
            multiplos +=1
        else: 
            lista += f"{i} no es multiplo par de 5\n"
        i += 1
    lista += f"El total de multiplos par de cinco en el intervalo es de {multiplos}"
    return lista

main()
