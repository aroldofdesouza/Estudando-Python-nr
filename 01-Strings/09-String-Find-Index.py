nome="Aroldo Fernando de Souza"
print(nome)
print("Find -> Retorna posição de String", nome.find("o"))
print("Find -> Retorna posição de String, entre a posição 2 em diante:", nome.find("o", 2))
print("Find -> Retorna posição de String, entre a posição 3 e 7:", nome.find("o", 3,7))
print("Finde -> se não encontrar, ele retorna -1", nome.find("x"))
print()
print("Index -> É o mais indicado, ele retorna a primeira ocorrencia.:", nome.index("o"))
print("E dá uma mensagem de erro, se não encontrar!")
print("Index -> É o mais indicado, ele retorna a primeira ocorrencia.:", nome.index("x"))

