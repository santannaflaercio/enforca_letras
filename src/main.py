from utils import ler_palavras, mostra_jogo
import random

erros = 0
letras_usadas = []
palavras = ler_palavras()
palavra_escolhida = random.choice(list(palavras)).lower()

while erros < 6 and len(set(palavra_escolhida) - set(letras_usadas)) > 0:
    # Mostra o estado atual do jogo
    mostra_jogo(palavra_escolhida, letras_usadas, erros)

    # Pede uma letra ao jogador
    letra = input("Digite uma letra: ").lower()

    # Verifica se a entrada é válida
    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, digite apenas uma única letra.")
        continue

    # Verifica se a letra já foi usada
    if letra in letras_usadas:
        print("Essa letra já foi usada!")
        continue

    # Adiciona a letra à lista de letras usadas
    letras_usadas.append(letra)

    # Verifica se a letra está na palavra
    if letra in palavra_escolhida:
        print("Acertou!")
    else:
        erros += 1
        print("Errou!")

# Verifica se o usuário ganhou ou perdeu
if erros >= 6:
    print(f"Você perdeu! A palavra era '{palavra_escolhida}'.")
else:
    print("Parabéns, você ganhou!")
