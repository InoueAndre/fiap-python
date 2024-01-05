with open("primeiro_arquivo.txt", "w") as arquivo: # w = write | r = read | a = append | x = exclusive | t = text
    arquivo.write("\nCriando meu primeiro arquivo.")

# Colocando o mesmo comando, ele irá sobrescrever a linha anterior
#with open("primeiro_arquivo.txt", "w") as arquivo:
#    arquivo.write("\nSobrescrevendo meu arquivo.")

with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)