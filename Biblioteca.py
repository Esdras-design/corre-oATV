produtos = {
    "Notebook": 3500,
    "Teclado": 150,
    "mouse": 80
}
print(produtos["Teclado"])


#------------------------------------------------------------------

produtos["Monitor"] = 1200
produtos["Notebook"] = 4000
print(produtos)

#------------------------------------------------------------------

del produtos["mouse"]
print(produtos)

#------------------------------------------------------------------

for chave, valor in produtos.items():
    print(f"produtos: {chave}, Preço: R${valor}")

#------------------------------------------------------------------

lista_de_tuplas = list(produtos.items())
print(lista_de_tuplas)