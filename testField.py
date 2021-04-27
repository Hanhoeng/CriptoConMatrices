import numpy as np
from Encriptator import *
from diccionario import Diccionario

#Prueba array de numpy
'''
x = np.array([[0,0,0],[0,0,0],[0,0,0]])
print(x)
'''

#Prueba metodo cargarMensaje(mensaje)
'''
texto = 'TexTo De pRuEba'
mensaje = Mensaje(texto)
print(mensaje)
encriptado = Encriptador().cargarMensaje(mensaje)
print(encriptado)
'''

#prueba de matriz
'''
##Matriz con inversa
###Pasando una lista de python
arr = [[1,2,1],[0,-1,3],[2,1,0]]
matriz1 = Matriz(arr)
print(matriz1)
###Pasando un array de numpy
arrnp = np.array(arr)
matriz2 = Matriz(arrnp)
print(matriz2)
###Ambos funcionan :D
##Matriz sin inversa, debe sacar error
arr2 = [[0,0,0],[0,0,0],[0,0,0]]
matriz3 = Matriz(arr2)
print(matriz3)
##funciona
##Iniciar con matriz inversa y cambiar a matriz inversible, debe sacar error
matriz4 = Matriz(arr)
print(matriz4)
matriz4.setMatriz(arr2)
##funciona
'''

#prueba de vectores
'''
x1x2x3 = [1,1,1]
x1x2x3b = [2,3,3]
vector1 = Vector(x1x2x3)
print(vector1)
vector1.setVector(x1x2x3b)
print(vector1)
##funciona
'''
'''
texto = 'texto de prueba'
mensaje = Mensaje(texto)
traductor = Diccionario()
texto2 = list(texto)
traducido = []
for i in texto2:
    traducido.append(traductor.traducir(i))
print(traducido)



print(mensaje)
encriptacion = Encriptador()
desencriptacion = Desencriptar()
arr = [[1,2,1],[0,-1,3],[2,1,0]]
print(encriptacion.encriptar(mensaje,arr))
print(mensaje)
print(desencriptacion.desencriptar(mensaje,arr))
print(mensaje)
'''
'''
x = 20.999999999999996
print(round(x,0))
'''
a = [0,0,0,0]
while len(a)%3 != 0:
    a.append(0)

print(a)