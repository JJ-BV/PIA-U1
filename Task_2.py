# Problema 2. Frecuencia de palabras en un texto.
# Escribe un programa que pida al usuario ingresar una frase o párrafo. Luego, el
# programa debe contar cuántas veces aparece cada palabra en el texto y mostrar
# las palabras junto con su frecuencia. 

# Requisitos:
# 1. Eliminar los signos de puntuación y convertir todas las palabras a
# minúsculas para evitar diferencias.
# 2. Usar un diccionario donde la clave sea la palabra y el valor sea su
# frecuencia.
# 3. Mostrar las palabras y sus frecuencias de forma ordenada por la palabra. 

import unicodedata


phrase = input("Enter phrase:")

def word_frequency(phrase):
    wordCounter = {}
    # Normalize string
    phraseNormalized = unicodedata.normalize('NFKD', phrase).encode('ASCII', 'ignore').decode('ASCII')
    for word in phraseNormalized.split(' '):
        # go lower case
        word = word.lower()
        #words counter
        if word in wordCounter:
            wordCounter[word] += 1
        else:
            wordCounter[word] = 1
    #order by key alphabetically
    wordCounter = {clave: valor for clave, valor in sorted(wordCounter.items())}
    print(wordCounter)

word_frequency(phrase)