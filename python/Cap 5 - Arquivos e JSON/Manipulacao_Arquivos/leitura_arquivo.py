with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
print("Tipo de dado da variável", type(conteudo))  
print("\nConteúdo do arquivo:\n", conteudo)