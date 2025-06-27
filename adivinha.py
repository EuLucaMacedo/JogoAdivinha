import random

def jogo_adivinhacao():
    numero_sorteado = random.randint(0, 10)
    tentativas = 0

    print('🤖 Pensei em um número de 0 a 10. Consegue adivinhar?')

    while True:
        try:
            chute = int(input('Digite seu palpite: '))
        except ValueError:
            print('❌ Entrada inválida. Digite um número inteiro entre 0 e 10.')
            continue

        tentativas += 1

        if chute != numero_sorteado:
            print(f'Você escolheu {chute}, ERROUUU! 😅 Tente novamente...\n')
        else:
            print(f'🎯 Acertou! O número era {numero_sorteado}.')
            print(f'Você precisou de {tentativas} tentativa(s).')
            break

    print('🏁 Fim do Jogo!')


