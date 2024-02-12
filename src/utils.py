def ler_palavras():
    try:
        with open("data/palavras.txt", "r") as arquivo:
            palavras = set(arquivo.readlines())
    except FileNotFoundError:
        print("Erro: Arquivo 'palavras.txt' não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo 'palavras.txt': {e}")
    return palavras


def mostra_jogo(palavra_escolhida, letras_usadas, erros):

    # Mostra a palavra com as letras acertadas
    palavra_com_acertos = ""
    for letra in palavra_escolhida:
        if letra in letras_usadas:
            palavra_com_acertos += letra
        else:
            palavra_com_acertos += "_"

    print("--------------------")

    # Mostra o número de erros
    print(f"Erros: {erros}")

    # Mostra a palavra com as letras acertadas
    print(f"Palavra: {palavra_com_acertos}")

    # Mostra as letras usadas
    print(f"Letras usadas: {letras_usadas}")
