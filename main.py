from Encriptator import *
from diccionario import Diccionario as traductor

print('Bienvenido!')
texto = input('Introduzca el mensaje que desee encriptar:\n')
mensaje = Mensaje(texto)

llave = [[2,3,6],[1,8,10],[3,2,1]]
print('Usando la matriz: {}'.format(llave))

encriptar = Encriptador()
desencriptar = Desencriptar()
encriptar.encriptar(mensaje,llave)
print('Mensaje encriptado: {}'.format(mensaje.getEncriptacion()))
eleccion0 = input('Desea desencriptarlo?(y/n) ')
eleccion0 = eleccion0.lower()

if eleccion0 == 'y':
    desencriptar.desencriptar(mensaje,llave)
    listaNumeros = mensaje.getDesencriptacion()
    print(listaNumeros)
    eleccion1=input('Desea traducir el mensaje?(y/n) ')
    eleccion1.lower()
    if eleccion1=='y':
        cadena=''
        for i in listaNumeros:
            letras = traductor().numsALetras(i)
            cadena += letras
        print(cadena)
    else:
        print('Hasta luego!')
else:
    print('{}\n'.format(mensaje))
    print('Hasta luego!')

print('Control de mensaje:\n')
print(mensaje)