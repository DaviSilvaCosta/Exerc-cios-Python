
#Questao 1
'''
nome = "joao"

with open("texto.txt","w") as arquivo:
    arquivo.write("joao")

with open("texto.txt","r") as arquivo:    
    nome = arquivo.read()

nome_invest = nome[::-1]

print(nome_invest)
'''
#questao 2
'''
with open("texto.txt", "w") as arquivo:
    arquivo.write("joao pedro da costa souza")

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(len(conteudo.split()))

'''
#questao 3
'''
with open("texto.txt", "w") as arquivo:
    arquivo.write("joao pedro da costa souza")

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()

print(conteudo.replace(" ","_"))
'''

#questao 4
'''
with open("texto.txt", "w") as arquivo:
    arquivo.write("computador bola jogo carteira jogo")

with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()

palavras_unicas = list(set(conteudo.lower().split()))
print(palavras_unicas)
'''
