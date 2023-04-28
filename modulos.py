

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

def generar_mensaje_tabla_multiplicacion(numero_tabla, valor_minimo, valor_maximo):
   mensaje = f"\nTabla de multiplicación del {numero_tabla}\n\n"
   i = valor_minimo
   while i <= valor_maximo:
       producto = numero_tabla * i
       mensaje += f"{numero_tabla:2d} x {i:2d} = {producto:3d}\n"
       i = i + 1
   return mensaje

def verificar_es_vocal (letra):
    es_vocal = letra.lower() in "aeiou" #True or False
    return es_vocal

def identificar_consonantes(respuesta):
    vocal=respuesta.lower() not in "aeiou"
    return vocal
