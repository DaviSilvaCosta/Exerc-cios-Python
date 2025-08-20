#Exercicio 1
'''
def gerar_tabuada():
    try:
        tabuada9 = "tabuada_9.txt"

        with open(tabuada9,"w")as arquivo:
            for i in range(1,11):
                linha = f"9 x {i} = {9*i}\n"
                arquivo.write(linha)

        print(f"Tabuada o 9 salva com sucesso no arquivo{tabuada9}")
    
    except Exception as e:
        print("Ocorreu um erro ao tentar salvar a tabuada")
        print(e)

gerar_tabuada()
'''
#Exercicio 2
'''
from datetime import datetime
try:
    Nome = input("Nome: ")
    RG = input("RG: ")
    CPF = input("CPF: ")
    Nascimento = int(input("Ano de Nascimento: "))
    Idade = datetime.now().year - Nascimento

    with open("texto.txt","w") as f:
        f.write(f"{Nome},{RG},{CPF},{Nascimento},{Idade}anos")

    print("Dados salvos com sucesso!")
except:
    print("Erro ao salvar")
'''
#exercicios 3
'''
try:
    with open("texto.txt", "r") as f:
        linhas = [linha.strip() for linha in f]
        
    print("Conteúdo do arquivo em forma de lista:")
    print(linhas)

except Exception as e:
    print("Erro ao ler o arquivo")
    print(e)

'''
#exercicio 4
'''
def registrar_status_aluno():
    try:
        # Solicita os dados do aluno
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        
        # Calcula a média
        media = (nota1 + nota2) / 2
        
        # Determina o status do aluno
        status = "Aprovado" if media >= 6 else "Reprovado"
        
        # Abre o arquivo em modo de anexação
        with open("status_alunos.txt", "a") as arquivo:
            # Escreve os dados no arquivo
            arquivo.write(f"{nome} - Média: {media:.2f} - Status: {status}\n")
        
        print("Dados registrados com sucesso!")
    
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos para as notas.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chama a função para registrar o status do aluno
registrar_status_aluno()
'''

#Exercicios 5
'''
def calculadora_e_armazenar():
    try:
        # Solicita os dois números inteiros
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        # Realiza as operações
        soma = num1 + num2
        subtracao = num1 - num2
        multiplicacao = num1 * num2
        divisao = num1 / num2 if num2 != 0 else 'Erro: Divisão por zero'
        
        # Armazena os resultados em um arquivo de texto
        with open("resultados_calculadora.txt", "a") as arquivo:
            arquivo.write(f"{num1} + {num2} = {soma}\n")
            arquivo.write(f"{num1} - {num2} = {subtracao}\n")
            arquivo.write(f"{num1} * {num2} = {multiplicacao}\n")
            arquivo.write(f"{num1} / {num2} = {divisao}\n")
            arquivo.write("-" * 30 + "\n")
        
    except ValueError:
        print("Erro: Por favor, insira valores inteiros válidos.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chama a função para executar a calculadora
calculadora_e_armazenar()

'''

#questa 6
'''
def ler_nome():
    try:
        nome = input("Digite o seu nome: ")
        
        if not nome.isalpha():
            raise ValueError("Nome inválido. Deve conter apenas letras.")
        
        print(f"Nome válido: {nome}")
    
    except ValueError as e:
        print(e)

ler_nome()
'''

#Exercicio 7
'''
def dividir_numeros():
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    
    except ValueError:
        print("Erro: Digite apenas números inteiros.")

dividir_numeros()
'''
#exercicio 8
'''
import math

def calcular_fatorial(lista):
    for num in lista:
        try:
            if type(num) != int:
                raise ValueError(f"'{num}' não é um número inteiro.")
            if num < 0:
                raise ValueError(f"O número {num} é negativo. Fatorial não existe.")
            
            print(f"O fatorial de {num} é {math.factorial(num)}")
        
        except ValueError as e:
            print(f"Erro: {e}")

lista_numeros = [5, 3, -2, "a", 7]

calcular_fatorial(lista_numeros)
'''
#questao 9
'''
import os

def contar_palavras_linhas(arquivo):
    if not os.path.exists(arquivo):
        print(f"Erro: O arquivo '{arquivo}' não existe.")
        return
    
    total_linhas = 0
    total_palavras = 0
    
    with open(arquivo, 'r') as f:
        for linha in f:
            total_linhas += 1
            total_palavras += len(linha.split())
    
    print(f"O arquivo '{arquivo}' tem {total_linhas} linhas e {total_palavras} palavras.")

arquivo = "texto.txt"
contar_palavras_linhas(arquivo)

'''

#quest 10
'''
import os

def salvar_nome(arquivo):
    try:

        nome = input("Digite o seu nome completo: ").strip()

        if not nome or not all(c.isalpha() or c.isspace() for c in nome):
            raise ValueError("Nome inválido. O nome deve conter apenas letras e espaços.")
        
        nome_formatado = nome.title()

        if not os.path.exists(arquivo):
            raise FileNotFoundError(f"O arquivo '{arquivo}' não foi encontrado no diretório.")
        
        with open(arquivo, 'a') as f:
            f.write(nome_formatado + '\n')
        
        print(f"Nome '{nome_formatado}' armazenado com sucesso no arquivo '{arquivo}'.")

    except ValueError as e:
        print(f"Erro: {e}")
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

arquivo = "texto.txt"
salvar_nome(arquivo)
'''

