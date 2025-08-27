

# Questões

## **Questão 1 - Abertura e Criação de Arquivo**
O código tenta abrir o arquivo `dados/notas.txt`. Caso o arquivo não exista, ele é criado automaticamente com o texto "Arquivo criado." Após isso, o conteúdo do arquivo é lido e exibido no terminal.

## **Questão 2 - Contagem de Linhas Não Vazias**
O código tenta abrir o arquivo `dados/frases.txt`. Se o arquivo não for encontrado, ele é criado automaticamente com algumas frases de exemplo. Em seguida, o código conta quantas linhas do arquivo não estão vazias e exibe o total.

## **Questão 3 - Limpeza de Comentários**
Este script abre o arquivo `dados/comentarios.txt` e, caso ele não exista, cria um arquivo com um texto de exemplo. O conteúdo é então processado: espaços extras são removidos e as reticências (`...`) são substituídas por pontos (`.`). O resultado é salvo no arquivo `saidas/comentarios_limpos.txt`.

## **Questão 4 - Processamento de Jogadores e Times**
O código lê o arquivo `dados/jogadores_times.txt`, que contém nomes de jogadores e seus respectivos times. Caso o arquivo não exista, ele é criado com alguns dados de exemplo. O script divide as linhas em um dicionário de jogadores e times. Linhas mal formatadas são registradas em `logs/linhas_invalidas.log`.

## **Questão 5 - Unificação e Ordenação de Listas**
O código tenta abrir os arquivos `dados/lista_a.txt` e `dados/lista_b.txt`. Se algum dos arquivos não for encontrado, ele será criado com uma lista padrão de frutas. O script junta as listas, remove duplicatas e salva o resultado no arquivo `saidas/lista_uniq.txt`.

## **Questão 6 - Contagem de Palavras Distintas**
O código lê o arquivo `dados/texto.txt`, converte todas as palavras para minúsculas e remove a pontuação. Em seguida, ele conta quantas palavras únicas existem no arquivo. Se o arquivo não for encontrado, uma mensagem de erro é exibida.

## **Questão 7 - Unificação e Ordenação de Duas Listas de Frutas**
Semelhante à Questão 5, o código lê os arquivos `dados/lista_a.txt` e `dados/lista_b.txt` com listas de frutas. Ele combina as listas, remove duplicatas, ordena as frutas e grava o resultado no arquivo `saidas/lista_unica.txt`. Se algum dos arquivos não for encontrado, o código processa apenas o arquivo que estiver disponível.
