# -*- coding: utf-8 -*-
"""Practica 3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13rCz5IdTSeIfGqSHx8xZ8C6YyGO8bo2P
"""

#Nicolas Sayago Victor Gabrie
#Solano Vargas Manuel Abraham de Jesus
#El objetivo de esta practica es la creacion y uso de tries de codificacion. Para ello generaremos un alfabet, con este haremos una asignacion de cadenas binarias

#Montar nuestro Drive en Phyton
from google.colab import files
from google.colab import drive
drive.mount("/content/drive")

#Importar las librerias que usaremos
import pandas as pd
#1  Leer el archivo de Excel desde Drive
df = pd.read_excel("/content/drive/MyDrive/Practica 3/BinaryAlfabet.xlsx")
class Codificador:
    def __init__(self, ruta_archivo):
        self.df = pd.read_excel(ruta_archivo)
        self.diccionario = dict(zip(self.df['Letras'], self.df['Valor binario']))

    def codificacion(self, cadena):
        binario = ''
        for caracter in cadena:
            if caracter in self.diccionario:
                binario += str(self.diccionario[caracter])
            else:
                print(f"El caracter '{caracter}' no se encuentra en el DataFrame.")
        return int(binario, 2) if binario else None

# Crear una instancia de la clase Codificador
codificador = Codificador("/content/drive/MyDrive/Practica 3/BinaryAlfabet.xlsx")

# Codificar una cadena
cadena = "ABRACADABRA"
binario = codificador.codificacion(cadena)
print(f"La codificación de '{cadena}' es {binario}")

import pandas as pd

class Decodificador:
    def __init__(self, ruta_archivo):
        self.df = pd.read_excel(ruta_archivo)
        self.diccionario = dict(zip(self.df['Letras'], self.df['Valor binario']))

    def codificacion(self, cadena):
        binario = ''
        for caracter in cadena:
            if caracter in self.diccionario:
                binario += str(self.diccionario[caracter])  # Convertir a cadena antes de concatenar
            else:
                binario += '0000'  # Asume que los caracteres desconocidos se codifican como '0000'
        return binario

# Primero, crea una instancia de la clase Decodificador con la ruta al archivo de Excel
decodificador = Decodificador('/content/drive/MyDrive/Practica 3/BinaryAlfabet.xlsx')

# Luego, puedes usar el método de codificación para codificar una cadena
cadena = 'Hola'
binario = decodificador.codificacion(cadena)

print(f'La cadena "{cadena}" se codifica en binario como: {binario}')