import os, random

# Função que verifica se o player quer jogar novamente
def verificador():
    opcao = input('Deseja jogar novamente? s = Sim | n = Não ').upper()
    if opcao == 'SIM':
        run()
    elif opcao == 'NÃO':
        return
    else:
        os.system('cls')
        print('\n\nDigite uma opção válida!\n\n')
        verificador()

# Funão com toda lógica do game
def main(pontos):

    arq_palavras = open('lista_palavras.txt', 'r')

    lista_palavras = []

    for p in arq_palavras:
        lista_palavras.append(p)

    palavra = list((random.choice(lista_palavras)).upper())
    palavra.remove('\n')
    tamanho = len(palavra)

    palavra_escondida = []
    usadas = []

    for l in palavra:
        if l == '-':
            palavra_escondida.append('-')
        else:
            palavra_escondida.append('_')

    # Lógica principal do jogo
    while pontos != 0:

        os.system('cls')

        display = '  '.join(palavra_escondida)
        usadas_f = '  '.join(usadas)
        palavra_revelada = ' '.join(palavra)

        print(
            f'\n\n\n Tenativas Restantes: {pontos}',
            f'\n\n\n Letras Usadas:\n\n {usadas_f}',
            '\n\n\n', display
        )

        letra = input('\n\nLetra: ').upper()

        if len(letra) == 1 and letra != ' ':
            if letra in palavra:
                for x in range(tamanho):
                    if letra == palavra[x]:
                        palavra_escondida.pop(x)
                        palavra_escondida.insert(x, letra)
                if letra not in usadas:
                    usadas.append(letra)
            else:
                if letra not in usadas:
                    pontos -= 1
                    usadas.append(letra)
        else:
            print('Digite uma letra')

        if palavra_escondida == palavra:
            os.system('cls')
            print('\n\n\nParabéns! Você acertou a palavra!\n\n')
            print(f'A palavra é: {palavra_revelada} \n\n\n')
            verificador()
            return

    os.system('cls')
    print('\n\nQue pena! Você não acertou...\n\n')
    print(f'A palavra era: {palavra_revelada} \n\n\n')
    verificador()
    return

# Função com apresentação pré e pós-game e execução do próprio game
def run():

    os.system('cls')

    print('\n\n..::  J O G O   D A   F O R C A   A N I M A I S  ::..\n')

    pontos = int(input('\nNúmero de Chances: '))

    # Chama a função main()
    main(pontos)

    os.system('cls')
    print('\n\n\n..::  Obrigado por jogar!  ::..')
    print('\n\n\nby dnotrever\n\n\n')

# Executa o jogo
run()