def ler_palavras():
    # Inicializa um conjunto vazio para armazenar as palavras
    palavras = set()
    try:
        # Abre o arquivo de palavras no modo de leitura
        with open("data/palavras.txt", "r") as arquivo:
            # Usa uma compreensão de conjunto para ler as palavras do arquivo
            # e remover espaços em branco extras com o método strip()
            palavras = {palavra.strip() for palavra in arquivo}
    except FileNotFoundError:
        # Imprime uma mensagem de erro se o arquivo não for encontrado
        print("Erro: Arquivo 'palavras.txt' não encontrado.")
        raise
    except Exception as e:
        # Imprime uma mensagem de erro se ocorrer qualquer outra exceção ao ler o arquivo
        print(f"Erro ao ler o arquivo 'palavras.txt': {e}")
        raise
    finally:
        # Retorna o conjunto de palavras, mesmo que uma exceção tenha ocorrido
        return palavras


def mostra_jogo(palavra_escolhida, letras_usadas, erros):
    # Mostra a palavra com as letras acertadas
    palavra_com_acertos = "".join(letra if letra in letras_usadas else "_" for letra in palavra_escolhida)

    print("--------------------")
    # Mostra o número de erros
    print(f"Erros: {erros}")
    # Mostra a palavra com as letras acertadas
    print(f"Palavra: {palavra_com_acertos}")
    # Mostra as letras usadas
    print(f"Letras usadas: {' '.join(sorted(letras_usadas))}")
