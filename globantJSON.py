#Desarrollar una función que interprete un texto en formato JSON y lo convierta 
#en un diccionario de claves, concatenando las anidadas usando ".". 
#Por ejemplo, ante el siguiente JSON: { "a": true, "b": { "b1": "hello", "b2": 3.5 }, "c": 3 } 
#Debería devolver: a = true b.b1 = hello b.b2 = 3.5 c = 3 

import json

def diccionarioConcatenado(diccionarioPadre, clavePadre=''):
    nuevoDiccionario = {}
    for clave in diccionarioPadre:
        valor = diccionarioPadre[clave]
        if clavePadre:
            nuevaClave = clavePadre + '.' + str(valor)
        else:
            nuevaClave = clave
        if isinstance(valor, dict):
            nuevoDiccionario.update(diccionarioConcatenado(valor, nuevaClave))
        else:
            nuevoDiccionario[nuevaClave] = valor
    
    return nuevoDiccionario

# JSON source
source = '{ "a": true, "b": { "b1": "hello", "b2": 3.5 }, "c": 3 }'

# JSON loads method converts a String to a dictionary
data = json.loads(source)
newDictionary = diccionarioConcatenado(data)

print(newDictionary) 