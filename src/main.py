from utils import ler_palavras, mostra_jogo
import random

erros = 0
acertos = 0
letras_usadas = []
palavras = ler_palavras()
palavra_escolhida = random.choice(list(palavras)).lower()

while erros < 6 and acertos < len(palavra_escolhida):

    # Mostra o estado atual do jogo
    mostra_jogo(palavra_escolhida, letras_usadas, erros)

    # Pede uma letra ao jogador
    letra = input("Digite uma letra: ").lower()

    # Verifica se a letra já foi usada
    if letra in letras_usadas:
        print("Essa letra já foi usada!")
        continue

    # Adiciona a letra à lista de letras usadas
    letras_usadas.append(letra)

    # Verifica se a letra está na palavra
    if letra in palavra_escolhida:
        acertos += 1
        print("Acertou!")
    else:
        erros += 1
        print("Errou!")
