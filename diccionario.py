#Entidades
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

    def traducir(self, llave):
        return(self.dicc[llave])

    def numsALetras(self,valor:int):
        return list(self.dicc.keys())[list(self.dicc.values()).index(valor)]

