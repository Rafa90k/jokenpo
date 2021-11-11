from random import randint
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']

computador = randint(0, 2)

print('''Suas opções são:
[0]Pedra
[1]Papel
[2]Tesoura
''')

jogador = int(input('Digite a sua opção: '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO!!')

print('-=' *12)

print('O computador jogou {}' .format(itens[computador]))
print('O jogador jogou {} ' .format(itens[jogador]))

print('-=' *12)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('JOGADOR GANHOU!!')

    elif jogador == 2:
        print('COMPUTADOR GANHOU!!')

    else:
        print('JOGADA INVALIDA!!')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU!!!')

    elif jogador == 1:
        print('EMPATE!!!')

    elif jogador == 2:
        print('JOGADOR GAMHOU!!')

    else:
        print('JOGADA INVALIDA!!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU!!')
    
    elif jogador == 1:
        print('COMPUTADOR GANHOU!!')

    elif jogador == 2:
        print('EMPATE!!')
    
    else:
        print('JOGADA INVALIDA!!')
