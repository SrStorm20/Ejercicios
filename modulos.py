

"""
Reciclaje
Yo
"""
def ingresar_real (numero):
    valor = None
    while valor == None:
        try: 
            valor = float(input(numero))
        except: 
            print("Error. \nEl valor no corresponde a la categoria real")
    return valor

def ingresar_string (letra):
    valor = None
    while valor == None:
        try: 
            valor = str(input(letra))
        except: 
            print("Error. \nEl valor no corresponde a la categoria texto")
    return valor

def ingresar_entero (numero):
    valor = None
    while valor == None:
        try: 
            valor = int(input(numero))
        except: 
            print("Error. \nEl valor no corresponde a la categoria entero")
    return valor

def verificar_validez(numero, nota_minima, nota_maxima): # NOTAS
    rango = True
    while rango:        
        valor = ingresar_real(numero)
        if valor > nota_maxima or valor < nota_minima:
            print (f"El numero debe estar entre {nota_minima} y {nota_maxima}")
        else:
            rango = False
    return valor

def verificar_entrada(numero, numero2): # Un limite
    centinela = True
    while centinela:
        valor = ingresar_entero(numero) 
        if valor <= numero2:
            mostrar_mensaje(f"Ingrese un valor mayor a {valor}.")
        else:
            centinela = False
    return valor

def verificar_limite(numero, rango_minimo, rango_maximo): # dos limites
    centinela = True
    while centinela:
        valor = ingresar_entero(numero)
        if valor < rango_minimo or valor > rango_maximo:
            print(f"Ingrese un numero entre {rango_minimo} y {rango_maximo}")
        
        else:
            centinela = False
    return valor


def mostrar_mensaje(mensaje):
    print(mensaje)

