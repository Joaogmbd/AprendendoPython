#primeiro Programa em Python
import os
import time
import random

clear = lambda: os.system('cls')

clear()
nome = input('Digite aqui o seu nome: ')
y = int(input('Olá, '+ nome.capitalize() + ' ! Digite aqui a sua Idade: '))

def menu():
    clear()
    print('=========================')
    print('Escolha uma opção de programa: \n\n')
    print('0: sair do programa!')
    print('1: saiba quantos dias você já viveu!')
    print('2: saiba se você já pode beber!')
    print('3: veja um foguete decolar!')
    print('4: Veja se o seu IMC está dentro do padrão saudável!')
    print('5: Gere um número aleatório!')
    print('6: Jogue Roleta Russa!')
    print('=========================')
    while(1):
        opcao = input()
        if opcao == '0':
            return 0
        if opcao == '1':
            diasvividos()
            break
        elif opcao == '2':
            maiordeidade()
            break
        elif opcao == '3':
            foguete()
            break
        elif opcao == '4':
            calculadoradeIMC()
            break
        elif opcao == '5':
            numeroAleatorio()
            break
        elif opcao == '6':
            russa()
            break
        else:
            print('Você não digitou uma opção correta!')
def diasvividos():
    clear()
    dias = y * 365
    print('Como você tem '+ str(y) + ' anos, você já viveu aproximadamente '+ str(dias) + ' dias!')
    time.sleep(5)
    menu()
def maiordeidade():
    clear()
    print('Agora, vamos ver se você pode beber \U0001F51E')
    confirma = input('Você está mentindo sobre a sua idade? (Digite "sim" ou "nao"): ')
    if confirma == 'sim':
        print('Agradeço pela honestidade!\n Da próxima vez use a sua idade de verdade!')
        time.sleep(5)
        clear()
        return 0
    elif confirma == 'nao':
        if y >= 18:
            print('Você pode beber! \U0001F608 \U0001F974')
            time.sleep(5)
            clear()
            menu()
        else:
            print('Pela lei, você não pode beber! \U0001F476')
            time.sleep(5)
            clear()
            menu()
def foguete():
    clear()
    print('\U00002601' * 4)
    print('\n'*4)
    print('\t\U0001F680')
    time.sleep(0.5)
    clear()
    print('\U00002601' * 4)
    print('\n'*3)
    print('\t\U0001F680')
    time.sleep(0.5)
    clear()
    print('\U00002601' * 4)
    print('\n'*2)
    print('\t\U0001F680')
    time.sleep(0.5)
    clear()
    print('\U00002601' * 4)
    print('\n')
    print('\t\U0001F680')
    time.sleep(0.5)
    clear()
    print('\U00002601' * 4)
    print('\t\U0001F680')
    time.sleep(0.5)
    clear()
    print('\n')
    time.sleep(0.5)
    clear()
    menu()
def calculadoradeIMC():
    clear()
    print('vamos calcular o seu IMC, ' + nome.capitalize() + '!')

    peso = float(input('Digite aqui o seu peso em kg: '))
    altura = float(input('Digite aqui a sua altura em metros: '))

    imc = peso / (altura**2)

    while(1):
        if imc < 18.5:
            print(nome + ', o seu imc é: '+ str(imc) + '.')
            print('Isso indica que você está classificado como MAGREZA.')
            break
        elif imc >= 18.5 and imc <= 24.9:
            print(nome + ', o seu imc é: '+ str(imc) + '.')
            print('Isso indica que você está classificado como NORMAL.')
            break
        elif imc >= 25 and imc <= 29.9:
            print(nome + ', o seu imc é: '+ str(imc) + '.')
            print('Isso indica que você está classificado como SOBREPESO.')
            print('Fique esperto, pois está classifacado também como OBESIDADE GRAU I.')
            break
        elif imc >= 30 and imc <= 39.9:
            print(nome + ', o seu imc é: '+ str(imc) + '.')
            print('Isso indica que você está classificado como OBESIDADE.')
            print('Fique esperto, pois está classifacado também como OBESIDADE GRAU II.')
            break
        elif imc >= 40:
            print(nome + ', o seu imc é: '+ str(imc) + '.')
            print('Isso indica que você está classificado como OBESIDADE GRAVE.')
            print('Fique esperto, pois está classifacado também como OBESIDADE GRAU III.')
            break
    time.sleep(5)
    menu()
def numeroAleatorio():
    clear()
    min = int(input('Digite o valor minímo: '))
    max = int(input('Digite o valor máximo: '))

    def gerar(min,max):
        numero = random.randint(min,max)
        return numero

    print('O número escolhido foi: '+ str(gerar(min,max)) + '!')
    print('Gostaria de gerar um novo número?')
    print('Digite 1 para gerar um novo número dentro dos valores escolhidos.')
    print('Digite 2 para gerar um novo número dentro de novos valores.')
    print('Digite 0 para voltar ao menu.')
    escolha = input()

    while (1):
        while escolha == '1':
            print('O novo número gerado foi: '+ str(gerar(min,max)))
            print('Digite 1 para gerar novamente.')
            escolha = input()
        if escolha == '2':
            numeroAleatorio()
        elif escolha == '0':
            menu()
        else:
            print('Há algo de errado com a entrada, digite novamente!')
            escolha = input()
def russa():
    from random import choice
    from time import sleep
    
    #codigo copiado do stackoverflow: https://pt.stackoverflow.com/a/462181
    print('=' * 30)
    print(f'\033[34m{f"Roleta Russa":^30}\033[m')
    print('=' * 30)

    valores = ['Falhou', 'Falhou', 'Falhou', 'Falhou', 'Falhou', 'Morreu']

    cont = 0
    for c in range(1, 7):
        print('Girando!')
        for i in range(30):
            sleep(0.1)
            print(f'{chr(46)}', end='')
        print()
        x = choice(valores)
        cont += 1
        if x != valores[-1]:
            print(f'\033[32m{cont}º disparo {x}!\033[m')
            if cont == 6:
                print(f'\033[34mVocê é muito Sortudo! Continua Vivo!\033[m')
        else:
            print(f'\033[31m{x}! No {cont}º disparo!\033[m')
            break

menu()
