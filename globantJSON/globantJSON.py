#Desarrollar una función que interprete un texto en formato JSON y lo convierta 
#en un diccionario de claves, concatenando las anidadas usando ".". 
#Por ejemplo, ante el siguiente JSON: { "a": true, "b": { "b1": "hello", "b2": 3.5 }, "c": 3 } 
#Debería devolver: a = true b.b1 = hello b.b2 = 3.5 c = 3 

import json

def diccionarioConcatenado(diccionarioPadre, clavePadre):
    nuevoDiccionario = {}
    
    #Iterate through the parentDictionary
    for clave in diccionarioPadre:
        # Get the value of the 1st key
        valor = diccionarioPadre[clave] 
        # If the value in the dictionary is a dictionary the function calls itself with a newly assigned parentKey
       
        if isinstance(valor, dict):
            nuevoDiccionario.update(diccionarioConcatenado(valor, clave + "."))
        else:
            nuevoDiccionario[clavePadre + clave] = valor
    
    return nuevoDiccionario

# JSON source
source = '{ "a": true, "b": { "b1": "hello", "b2": 3.5 }, "c": 3 }'

# JSON loads method converts a String to a dictionary
data = json.loads(source)
newDictionary = diccionarioConcatenado(data, "") # Method to make the new concatenated dictionary

print(newDictionary) 