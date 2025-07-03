import random

def jogo_adivinhacao():
    numero_sorteado = random.randint(0, 10)
    tentativas = 0

    print('🎯 Bem-vindo ao jogo: Adivinhe o Número!')
    print('🤖 Pensei em um número de 0 a 10. Consegue adivinhar?')

    while True:
        try:
            chute = int(input('Digite seu palpite: '))
            tentativas += 1

        except ValueError:
            print('❌ Entrada inválida. Digite um número inteiro entre 0 e 10.')
            continue

        if chute < numero_sorteado:
            print('🔻 Muito baixo.')
        elif chute > numero_sorteado:
            print("🔺 Muito alto.")
        if chute != numero_sorteado:
            print(f'Você escolheu {chute}, ERROUUU! 😅 Tente novamente...\n')
        else:
            break

    print(f'🎯 Acertou! O número era {numero_sorteado}.')
    print(f'Você precisou de {tentativas} tentativa(s).')
    print('🏁 Fim do Jogo!')


if __name__ == "__main__":
    jogo_adivinhacao()