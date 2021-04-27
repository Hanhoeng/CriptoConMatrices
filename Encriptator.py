from os import listxattr
import numpy as np
from abc import ABC, abstractmethod
from diccionario import Diccionario

#Entidades
##Mensaje
class Mensaje():
    def __init__(self, texto):
        self.texto = texto
        self.textoEncript = []
        self.textoDesEncr = []

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



class Desencriptar():
    
    def desencriptar(self, mensaje:Mensaje, matriz:list):
        lista = mensaje.getEncriptacion()
        matriz = np.array(matriz)
        llave = np.linalg.inv(matriz)

        def split_list(lst:list):
            n=3
            while len(lst)%3!=0:
                lst.append(' ')
                pass
            for i in range(0,len(lst),n):
                yield lst[i:i + n]
            '''
            
            if len(list(lst))%3==0:
                for i in range(0, len(lst), n): 
                    yield lst[i:i + n]
            else:
                lst.append(" ")
            return split_list(lst)
            '''

        listaVectores = list(split_list(lista))
        listaVectoresResultantes = []
        
        for i in listaVectores:
            i = np.array(i)
            res = np.dot(i,llave)
            listaVectoresResultantes.append(res)
        final = []
        for i in range(len(listaVectoresResultantes)):
            for j in listaVectoresResultantes[i]:
                final.append(int(round(j,0)))
        mensaje.setDesencriptacion(final)



class Encriptador():

    def encriptar(self, mensaje:Mensaje, matriz:list):
        texto = mensaje.getTexto()
        texto = texto.lower()
        listaTexto = list(texto)
        listaNumeros = []
        #Convierte letras a numeros para poder ser encriptable
        for i in listaTexto:
            listaNumeros.append(Diccionario().traducir(i))
        #Comprueba si la longitud del mensaje es modular de 3, si no es le agrega espacios
        #hasta que sea modular de 3
        def split_list(lst:list):
            n=3
            while len(lst)%n != 0:
                lst.append(0)
            for i in range(0,len(lst),n):
                yield lst[i:i + n]
            '''
            if len(lst) != 0:
                while len(lst)%3!=0:
                    lst.append(' ')
            else:
            '''
                
            
            '''
            
            if len(list(lst))%3==0:
                for i in range(0, len(lst), n): 
                    yield lst[i:i + n]
            else:
                lst.append(" ")
            return split_list(lst)
            '''
        listaVectores = list(split_list(listaNumeros))
        listaVectoresResultantes = []
        matriz = np.array(matriz)
        for i in listaVectores:
            i = np.array(i)
            res = np.dot(i,matriz)
            listaVectoresResultantes.append(res)
        final = []
        for i in range(0,len(listaVectoresResultantes)):
            for j in listaVectoresResultantes[i]:
                final.append(j)
        mensaje.setEncriptacion(final)
        return print("Se encripto con exito!!")