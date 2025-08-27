import os
import string

# Questão 1
def questao1():
    caminho = "dados/notas.txt"
    os.makedirs("dados", exist_ok=True)
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("Arquivo criado.")
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()
    print("Conteúdo de 'notas.txt':")
    print(conteudo)

# Questão 2
def questao2():
    caminho = "dados/frases.txt"
    os.makedirs("dados", exist_ok=True)
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print("Arquivo 'frases.txt' não encontrado. Criando automaticamente...")
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("Esta é uma frase de exemplo.\n\nOutra linha válida.\n\n\n")
        with open(caminho, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    except PermissionError:
        print("Erro: Sem permissão para acessar o arquivo.")
        return

    nao_vazias = [linha for linha in linhas if linha.strip()]
    print(f"Total de linhas não vazias: {len(nao_vazias)}")

# Questão 3
def questao3():
    entrada = "dados/comentarios.txt"
    saida = "saidas/comentarios_limpos.txt"
    os.makedirs("dados", exist_ok=True)
    os.makedirs("saidas", exist_ok=True)

    if not os.path.exists(entrada): 
        with open(entrada, "w", encoding="utf-8") as f:
            f.write("Muito bom... gostei  muito  do trabalho... parabéns...")
    try:
        try:
            with open(entrada, "r", encoding="utf-8") as f:
                conteudo = f.read()
        except UnicodeDecodeError:
            with open(entrada, "r", encoding="latin-1") as f:
                conteudo = f.read()

        conteudo = conteudo.replace("...", ".")
        conteudo = ' '.join(conteudo.split())

        with open(saida, "w", encoding="utf-8") as f:
            f.write(conteudo)
        print("Arquivo 'comentarios_limpos.txt' criado.")
    except Exception as e:
        print("Erro ao processar comentarios.txt:", e)

# Questão 4
def questao4():
    entrada = "dados/jogadores_times.txt"
    log = "logs/linhas_invalidas.log"
    os.makedirs("dados", exist_ok=True)
    os.makedirs("logs", exist_ok=True)
    jogadores = {}

    if not os.path.exists(entrada):
        with open(entrada, "w", encoding="utf-8") as f:
            f.write("João,Palmeiras\nMaria,Corinthians\nLinha inválida\nCarlos,Santos")

    try:
        with open(entrada, "r", encoding="utf-8") as f:
            linhas = f.readlines()

        for linha in linhas:
            try:
                if ',' in linha:
                    nome, time = linha.strip().split(",", 1)
                    jogadores[nome.strip()] = time.strip()
                else:
                    raise ValueError("Linha sem vírgula")
            except Exception:
                try:
                    with open(log, "a", encoding="utf-8") as log_file:
                        log_file.write(linha)
                except Exception:
                    print("Erro ao escrever no log.")
        print("Dicionário de jogadores e times:")
        print(jogadores)
    except FileNotFoundError:
        print("Arquivo 'jogadores_times.txt' não encontrado.")

# Questão 5
def questao5():
    arquivos = ["dados/lista_a.txt", "dados/lista_b.txt"]
    saida = "saidas/lista_uniq.txt"
    os.makedirs("dados", exist_ok=True)
    os.makedirs("saidas", exist_ok=True)
    itens = set()

    for arq in arquivos:
        if not os.path.exists(arq):
            with open(arq, "w", encoding="utf-8") as f:
                if "a" in arq:
                    f.write("banana\nlaranja\nmaçã\n")
                else:
                    f.write("maçã\nuva\nkiwi\n")

        try:
            with open(arq, "r", encoding="utf-8") as f:
                for linha in f:
                    itens.add(linha.strip())
        except FileNotFoundError:
            print(f"Aviso: Arquivo '{arq}' não encontrado.")

    with open(saida, "w", encoding="utf-8") as f:
        for item in sorted(itens):
            f.write(item + "\n")
    print("Arquivo 'lista_uniq.txt' criado.")

# Questão 6
def questao6():
    caminho = "dados/texto.txt"
    os.makedirs("dados", exist_ok=True)

    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("Este é um texto de exemplo. Ele contém várias palavras, inclusive repetidas!")

    try:
        with open(caminho, "r", encoding="utf-8") as f:
            texto = f.read()

        texto = texto.lower()
        for p in string.punctuation:
            texto = texto.replace(p, " ")
        palavras = set(texto.split())
        print(f"Quantidade de palavras únicas: {len(palavras)}")
    except FileNotFoundError:
        print("Arquivo texto.txt não encontrado.")

# Questão 7
def questao7():
    arquivos = ["dados/lista_a.txt", "dados/lista_b.txt"]
    saida = "saidas/lista_unica.txt"
    os.makedirs("dados", exist_ok=True)
    os.makedirs("saidas", exist_ok=True)
    itens = set()

    for arq in arquivos:
        try:
            with open(arq, "r", encoding="utf-8") as f:
                itens.update([linha.strip() for linha in f])
        except FileNotFoundError:
            print(f"Aviso: Arquivo '{arq}' não encontrado.")

    with open(saida, "w", encoding="utf-8") as f:
        for item in sorted(itens):
            f.write(item + "\n")
    print("Arquivo 'lista_unica.txt' criado.")

# Execução principal
def main():
    print("Executando todas as questões...")
    questao1()
    print("-" * 40)
    questao2()
    print("-" * 40)
    questao3()
    print("-" * 45)
    questao4()
    print("-" * 40)
    questao5()
    print("-" * 40)
    questao6()
    print("-" * 40)
    questao7()
    print("Todas as questões executadas.")

if __name__ == "__main__":
    main()
