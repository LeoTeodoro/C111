# # COLECOES


# # TUPLAS
# nomes = ("Goku", "Vegeta", "Trunks", "Gohan")
# # SLICING DE DADOS
# print(nomes[0])
# print(nomes[:2])
# print(nomes[1:3])
# print(nomes[-2])

# # UPDATE
# nomes[0] = "Bulma" #ERRO


# # LISTAS
# nomes = ["Goku", "Vegeta", "Trunks", "Gohan"]
# # CREATE
# nomes.append("Bulma")
# # UPDATE
# nomes[0] = "Goten"
# # DELETE
# nomes.remove("Trunks")  # remocao por valor
# del nomes[2]  # remocao por indice
# print(nomes)


# # CONJUNTOS
# nomes = {"Goku", "Vegeta", "Trunks", "Gohan"}
# # CREATE
# nomes.add("Bulma")
# nomes.add("Goku")  # nao adiciona elementos repetidos

# # DELETE
# nomes.remove("Gohan")

# # UPDATE NAO FUNCIONA
# print(nomes)


# DICIONARIO
pessoa = {"nome": "Goku", "idade": 42}
# CREATE
pessoa["sexo"] = "M"
# UPDATE
pessoa["idade"] = 43
# DELETE
del pessoa["idade"]
print(pessoa)

pessoa2 = {"nome": "Bulma", "idade": 42}
# CREATE
pessoa2["sexo"] = "F"
# UPDATE
pessoa2["idade"] = 43
# DELETE
del pessoa2["idade"]
print(pessoa2)

# COLECOES ANINHADAS
nomes = [pessoa, pessoa2]
print(nomes[1]["nome"])
