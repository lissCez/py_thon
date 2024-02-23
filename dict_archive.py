# arquivo = open("./exemplo.txt")
# #texto = arquivo.read()
# #texto = arquivo.readlines()
# #texto = arquivo.readline()
# for line in arquivo.readline():

# print(line)
# #print(texto)

# with open("arquivo_escrita.txt", "w") as f:
#     raise ValueError
#     f.write("oi ;b")

# with open("arquivo_escrita.txt", "r+") as f:
#     raise ValueError
#     f.write("oi ;b")

from pprint import pprint

conta_letras = {}
conta_palavras = {}

for linha in conta_palavras:
    palavras = linha.split()

    for palavra in palavras:
        conta_palavras[palavra] = conta_palavras.get(palavra, 0) + 1

        for letra in palavra:
            conta_letras[letra] = conta_letras.get(letra, 0) + 1

# pprint(conta_letras)
# pprint(conta_palavras)

max_palavra = [None, 0]
for palavra, count in conta_palavras.items():
    if max_palavra[1] < count:
        max_palavra = [palavra, count]

pprint(max_palavra)

max_char = [None, 0]
for char, count in conta_letras.items():
    if max_char[1] < count:
        max_char = [letra, count]

with open("result_ado.txt", "w") as f:
    f.write(f"Palavra mais frequente: {max_palavra[0]}\n")
    f.write(f"Frequência: {max_palavra[1]}\n")
    f.write("\n" + "=" * 50 + "\n")
    f.write(f"Cactére mais frequente: {max_palavra[0]}\n")
    f.write(f"Frequência: {max_palavra[1]}\n")
