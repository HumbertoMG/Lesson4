# Defino la tupla
tupla = (1,"X",2.35,"hola",2)
# Impresión de tupla
print ("Tupla de 5 elementos: ", tupla)
# Convierto la tupla en lista utilizando función list
lista = list(tupla)
# Imprimo la lista
print("Lista de la tupla de 5 elementos: ", lista)
# Defino diccionario con los elementos de la lista
diccionario = {1:lista[0], 2: lista[1], 3: lista[2], 4: lista[3], 5: lista[4]}
# Imprimo el diccionario
print ("Diccionario de la lista de 5 elementos: ", diccionario)
