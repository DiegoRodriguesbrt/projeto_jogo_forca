# importando biblioteca para utilizar função random, que será utilizada para sorteio da palavra.
# importando biblioteca do RegEx para utilizar na formatação do input do usuário.
# importando biblioteca pygame para fazer os efeitos sonoros do jogo.
# importando biblioteca os para limpar tela do console/terminal, não funciona na IDE.
# importando biblioteca time para não deixar o usuário dar spam no input.
import re
from random import randrange
import pygame
import os
import time

# Método que limpa a tela do console/terminal.
def limpa_tela():
    os.system('cls')


# Método de abertura ou cabeçalho do jogo.
def mensagem_abertura():
    print(20 * ">" + 11 * " " + "UNIESP" + 11 * " " + 20 * "<" + "\n"
                                                                 "#" + 21 * " " + "INTRODUÇÃO A PROGRAMAÇÃO" + 21 * " " + "#\n"
                                                                                                                          "#" + 66 * " " + "#")
    print("#" + 28 * " " + "CATEGORIA" + 29 * " " + "#")
    print("#" + 66 * " " + "#")
    print("#" + 7 * " " + "1 - FRUTA" + 50 * " " + "#")
    print("#" + 7 * " " + "2 - CARRO" + 50 * " " + "#")
    print("#" + 7 * " " + "0 - SAIR" + 51 * " " + "#")
    print("#" + 66 * " " + "#")
    print("#  Grupo:" + 58 * " " + "#")
    print("#  Diego Rodrigues de Brito - 2022111510080@iesp.edu.br            #")
    print("#  Gabriel Viana - 2022111510007@iesp.edu.br                       #")
    print("#  Mateus Lemos - 2022111510023@iesp.edu.br                        #")
    print("#  Maria Susete de Lima - 2022111510009@iesp.edu.br                #")
    print("#  Bruno Falcão Feitosa Massa Filho - 2022110220019@iesp.edu.br    #")
    print("#  Maria de Fátima Souza Moreira - 2022111510049@iesp.edu.br       #")
    print("#" + 66 * " " + "#")
    print(68 * "#" + "\n")


# Função responsável por abrir e sortear a palavra dentro do arquivo.txt que será utilizada no jogo;
# Função responsável pelo menu inicial do jogo;
def sorteio_palavra():
    palavras = []
    categoria = input("Escolha uma das categorias: ").strip()
    print()

    if categoria == "1":
        arquivo = open("frutas.txt", "r")

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

    elif categoria == "2":
        arquivo = open("carros.txt", "r")

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

        arquivo.close()

    elif categoria == "0":
        return exit()

    else:
        return -1

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    informa_categoria = categoria
    limpa_tela()
    if informa_categoria == "1":
        print("Você selecionou a Categoria FRUTAS!\n")
    elif informa_categoria == "2":
        print("Você selecionou a Categoria CARROS!\n")
    return palavra_secreta


# Essa função formata o input dos chutes para não receber caractere especial, mais de 1 carectere ou números;
def formata_chute_input():
    chute = input("\nQual letra? ").strip().upper()
    if len(chute) != 1 or not re.match("[a-zA-ZçÇãÃêÊ]", chute):
        return 0
    else:
        return chute


# Essa função imprime na tela a quantidade de caracteres da palavra a ser adivinhada pelo jogador;
# O tamanho dessa palavra está representado pelos traços, por exemplo: Kiwi -> ['_', '_', '_', '_'];
def inicializa_letras(palavra):
    return ['_' for letra in palavra]


# Esta função é responsável por percorrer toda a palavra e verificar se as letras chutadas pelo jogador pertencem a palavra secreta;
# Se essa letra realmente pertencer a palavra, então ela não estará mais oculta para o jogador;
# já aparecendo na posição correta da palavra. Por exemplo:
# chute: a   ->    ['_', 'a', '_', 'a']
def chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1


# Esta função tem como objetivo imprimir na tela gradativamente o desenho da forca conforme o jogador for dando chutes errados;
def desenha_forca(tentativas):
    print("  _______     ")
    print(" |/      |    ")

    if tentativas == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if tentativas == 2:
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |       |    ")
        print(" |            ")

    if tentativas == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |       |    ")
        print(" |            ")

    if tentativas == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if tentativas == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if tentativas == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")


# Método responsável por imprimir na tela uma mensagem de vitória;
def imprime_mensagem_vencedor():
    pygame.mixer.music.load("som_ganhou.mp3")
    pygame.mixer.music.play()
    print("Você ganhou, parabéns :D")


# Método que imprime na tela uma mensagem caso o jogador não vença o jogo;
def imprime_mensagem_perdedor(palavra_secreta):
    pygame.mixer.music.load("som_perdeu.mp3")
    pygame.mixer.music.play()
    print("Infelizmente você perdeu :(")
    print("A palavra era {}".format(palavra_secreta))


# Método que oferece a opção de iniciar o jogo novamente, sempre após o fim de uma partida (caso o jogador queira);
def mensagem_jogar_novamente():
    jogar_novamente = (input("Você gostaria de jogar novamente? [S/N] ").strip().upper())

    if jogar_novamente == "S" or jogar_novamente == "SIM":
        limpa_tela()
        if __name__ == "__main__":
            jogar()

    elif jogar_novamente == "N" or jogar_novamente == "NÃO" or jogar_novamente == "NAO":
        print("Obrigado por jogar!!")

    else:
        print('Opção inválida! Digite "S" para jogar novamente ou "N" para encerrar o jogo.')
        mensagem_jogar_novamente()


# Método que efetivamente da início ao jogo, em que as funções acima serão utilizadas e implementadas;
def jogar():
    pygame.init()
    pygame.mixer.music.pause()  # método para pausar música quando o jogador clica em jogar novamente rapidamente;
    mensagem_abertura()
    palavra_secreta = sorteio_palavra()

    while palavra_secreta == -1:
        pygame.mixer.music.load("som_letra_repetida.mp3")
        pygame.mixer.music.play()
        print("Opção inválida!!\n")
        time.sleep(1)
        palavra_secreta = sorteio_palavra()

    letras_sorteio = inicializa_letras(palavra_secreta)
    print(letras_sorteio)

    enforcou = False
    acertou = False
    tentativas = 0
    letras_certas = []  # Lista que armazena as letras certas adivinhadas pelo jogador;
    letras_erradas = []  # Lista que armazena as letras erradas chutadas pelo jogador;

    while not enforcou and not acertou:

        chute = formata_chute_input()

        # Condição que verifica os caracteres de entrada do chute feito pelo usuário;
        while chute == 0:
            pygame.mixer.music.load("som_letra_repetida.mp3")
            pygame.mixer.music.play()
            print("Digite uma letra válida!!\n")
            time.sleep(1)
            chute = formata_chute_input()

        # Condição que verifica se a letra digitada pelo jogador é repetida;
        while chute in letras_certas or chute in letras_erradas:
            pygame.mixer.music.load("som_letra_repetida.mp3")
            pygame.mixer.music.play()
            print("Letra repetida! Digite outra.\n")
            time.sleep(1)
            chute = input("Qual letra? ").strip().upper()

        # Condição que verifica se tem a letra digitada na palavra;
        if chute in palavra_secreta:
            chute_correto(chute, letras_sorteio, palavra_secreta)
            letras_certas.append(chute)
            pygame.mixer.music.load("som_acertou.mp3")
            pygame.mixer.music.play()

        # Condição referente a quando a letra digitada não está na palavra;
        else:
            pygame.mixer.music.load("som_errou.mp3")
            pygame.mixer.music.play()
            tentativas += 1
            desenha_forca(tentativas)
            letras_erradas.append(chute)

        # O jogador será enforcado depois de 6 tentativas;
        enforcou = tentativas == 6
        acertou = "_" not in letras_sorteio

        print()
        print(letras_sorteio)
        print()

        # Parte e laço que informam letras erradas e acertadas ao usuário;
        print("Letras informadas:")
        print("Corretas: ", end=" ")

        for i in range(0, len(letras_certas)):
            if i == len(letras_certas) - 1:
                print("{}".format(letras_certas[i]), end=".")
            else:
                print("{}".format(letras_certas[i]), end=", ")

        print()
        print("Erradas: ", end=" ")

        for i in range(0, len(letras_erradas)):
            if i == len(letras_erradas) - 1:
                print("{}".format(letras_erradas[i]), end=".")
            else:
                print("{}".format(letras_erradas[i]), end=", ")

        print("\n")
        print(68 * "-")

    # Executa método para imprimir mensagem quando o jogador vence;
    if acertou:
        imprime_mensagem_vencedor()

    # Executa método para imprimir mensagem quando o jogador perde;
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    mensagem_jogar_novamente()


# Condição para método jogar como main e iniciar
if __name__ == "__main__":
    jogar()
