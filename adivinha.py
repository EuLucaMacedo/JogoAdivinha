import random

def bem_vindo():
    print('🎯 Bem-vindo ao jogo: Adivinhe o Número!')
    print('🤖 Pensei em um número. Consegue adivinhar?')

def escolher_dificuldade():

    print('\n🎮 Escolha a dificuldade:')
    print('[ 1 ] Fácil (1 a 30)')
    print('[ 2 ] Médio (1 a 60)')
    print('[ 3 ] Difícil (1 a 100)')

    while True:
        escolha = input('Escolha o Nível do Jogo: ')
        if escolha == '1':
            return 30
        elif escolha == '2':
            return 60
        elif escolha == '3':
            return 100
        else:
            print('❌Escolha Inválida. Tente novamente.')

def obter_palpite():
    while True:
        try:
            return int (input('Digite o seu Palpite: '))
        except ValueError:
            print('❌ Entrada inválida. Digite um número.')


def jogo_adivinhacao():
    limite = escolher_dificuldade()
    numero_sorteado = random.randint(1, limite)
    tentativas = 0



    nivel = 'Fácil' if limite == 30 else ('Médio' if limite == 60 else 'Difícil')
    print(f'Você escolheu o Nível {nivel} de Dificuldade!')

    print(f'\n🔢 O número está entre 1 e {limite}.\n')

    while True:
        chute = obter_palpite()
        tentativas += 1
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
    bem_vindo()
    jogo_adivinhacao()