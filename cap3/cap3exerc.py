# 1
# a
times = [
    "Flamengo",
    "Manchester City",
    "Real Madrid",
    "Bayern de Munique",
    "Barcelona",
]
print(times[:3])
# b
print(times[3:])
# c
print(sorted(times))
# d
print(times.index("Barcelona"))


# 2
loja1 = {
    "Galaxy s24",
    "Galaxy s23",
    "Galaxy s23 fe 5g",
    "Galaxy s22",
    "Galaxy a71",
    "Galaxy a54",
}
loja2 = {
    "Iphone 15 pro",
    "Iphone 15 pro max",
    "Iphone 14 pro",
    "Iphone 14",
    "Iphone 13",
}
total = [loja1, loja2]
print("\nTodos os modelos:")
print(total)
print("Modelos separados por loja:")
print("loja 1:")
print(loja1)
print("loja 2:")
print(loja2)

# 3
nome = input("\nDigite seu nome: ")
media = float(input("Digite sua media: "))
portal = {"nome": nome, "media": media}
if portal["media"] >= 60:
    print(f"{portal['nome']} AP")
    portal["situacao"] = "AP"
else:
    print(f"{portal['nome']} RP")
    portal["situacao"] = "RP"
print(portal)
