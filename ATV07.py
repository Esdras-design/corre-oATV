tupla = ("Alice", "Bruno", "Carlos", "Daniela")
lista_temp = list(tupla)
lista_temp[2]= "Clara"
tupla = tuple(lista_temp)
print(tupla)