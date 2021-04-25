import numpy as np
from abc import ABC, abstractmethod

#Entidades
##Mensaje
class Mensaje():
    def __init__(self, texto):
        self.texto = texto
        self.textoEncript = ''
        self.textoDesEncr = ''

    def setTexto(self, nuevoTexto:str):
        self.texto = nuevoTexto
        return print('Texto modificaco con exito!')
    def getTexto(self):
        return self.texto

    def setEncriptacion(self, textoEncript):
        self.textoEncript = textoEncript
    def getEncriptacion(self):
        return self.textoEncript

    def setDesencriptacion(self, textoDesEncr):
        self.textoDesEncr = textoDesEncr
    def getDesencriptacion(self):
        return self.textoDesEncr

    def __str__(self):
        cadena = ''
        cadena += 'Mensaje:\n\t{}\n'.format(self.texto)
        cadena += 'Mensaje encriptado:\n\t{}\n'.format(self.textoEncript)
        cadena += 'Mensaje desencriptado:\n\t{}\n'.format(self.textoDesEncr)
        return cadena

##Matriz
class Matriz():
    def __init__(self, matriz:list):
        matriz = np.array(matriz)
        try:
            tmpInvMatriz = np.linalg.inv(matriz)
        except np.linalg.LinAlgError:
            print('Introduzca una matriz inversible')
        else:
            self.Matriz = np.array(matriz)
            self.MatrizInv = np.array(tmpInvMatriz)

    def setMatriz(self, matriz:list):
        tmpMatriz = np.array(matriz)
        try:
            tmpInvMatriz = np.linalg.inv(tmpMatriz)
        except np.linalg.LinAlgError:
            print('Introduzca una matriz inversible')
        else:
            self.Matriz = np.array(tmpMatriz)
            self.MatrizInv = np.array(tmpInvMatriz)
    def getMatriz(self):
        return self.Matriz

    def getMatrizInv(self):
        return self.MatrizInv

    def __str__(self):
        cadena = ''
        cadena += 'Matriz:\t\n{}\n'.format(self.Matriz)
        cadena += 'Inversa:\t\n{}\n'.format(self.MatrizInv)

        return cadena

##Vector
class Vector():
    def __init__(self,vector:list):
        self.vector = vector
    
    def setVector(self, nuevoVector:list):
        self.vector = nuevoVector
    def getVector(self):
        return self.vector

    def __str__(self):
        cadena = ''
        cadena = 'Vector:\n'
        for i in self.vector:
            cadena += '\t{}\n'.format(i)
        return cadena

##Diccionario
class Diccionario():
    def __init__(self):
        self.dicc = {
            "a":1,
            "b":2,
            "c":3,
            "d":4,
            "e":5,
            "f":6,
            "g":7,
            "h":8,
            "i":9,
            "j":10,
            "k":11,
            "l":12,
            "m":13,
            "n":14,
            "ñ":15,
            "o":16,
            "p":17,
            "q":18,
            "r":19,
            "s":20,
            "t":21,
            "u":22,
            "v":23,
            "w":24,
            "x":25,
            "y":26,
            "z":27,
            ".":28,
            " ":0
        }

    def getDiccionario(self):
        return self.dicc


#Interfaces
##Encriptacion

class Encriptacion(ABC):
    
    @abstractmethod
    def cargarMensaje(self, mensaje:Mensaje) -> list:
        pass

    @abstractmethod
    def encriptar(self, lista:list, matriz:Matriz) -> str:
        pass

##Desencriptacion

class Desencriptacion(ABC):

    @abstractmethod
    def textoALista(self, texto:str) -> list:
        pass

    @abstractmethod
    def desencriptar(self, lista:list, matriz:Matriz) -> str:
        pass