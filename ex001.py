import os
from time import sleep

clear = lambda: os.system('cls')

lista = ['lanche', 'almoço']
options = 99

while options != '0':
    while True:
        clear()
        options = input('[1] Inserir\n[2] Apagar\n[3] Ver itens\n[0] Encerrar\n')
        if options == '1' or options == '2' or options == '3' or options == '0':
            break
        else:
            print('Só é possível selecionar as opções 1, 2 ou 3.\nTente novamente!\n')

    if options == '1':
        voltar = 99
        while voltar != 0:
            clear()
            inserir = str(input('\nDigite o nome do item que quer inserir:\n'))
            lista.append(inserir)
            clear()
            print(f'\'{inserir}\' foi inserido em sua lista.\n')
            while True:
                voltar = input('[1] Inserir mais itens\n[0] Retornar ao menu\n')
                if voltar == '1':
                    break
                elif voltar == '0':
                    voltar = 0
                    break
                else:
                    clear()
                    print('Escolha um item do menu.\n')

    if options == '2':
        voltar = 99
        while voltar != 0:
            clear()
            for item in range(len(lista)):
                print(item + 1, lista[item])
            print('')
            if len(lista) == 0:
                print('Não há itens na lista.')
                sleep(3)
                voltar = 0
                break
            apagar = int(input('\nDigito o número do item você quer excluir:\n'))
            if apagar <= len(lista):
                clear()
                print('Seu item foi apagado.\n')
                lista.pop(apagar-1)
            else:
                clear()
                print('Você deve digitar exclusivamente um número relativo à um item da lista.\n')
            while True:
                    voltar = input('[1] Apagar mais itens\n[0] Retornar ao menu\n')
                    if voltar == '1' :
                        break
                    elif voltar == '0':
                        voltar = 0
                        break
                    else:
                        clear()
                        print('Escolha um item do menu.\n')

    if options == '3':
        voltar = 99
        while voltar != 0:
            clear()
            if len(lista) == 0:
                clear()
                print('\nA lista está vazia.\n')
            else:
                clear()
                for item in range(len(lista)):
                    print(item+1, lista[item])
                print('')
            while True:
                    voltar = input('[0] Retornar ao menu\n')
                    if voltar == '0':
                        voltar = 0
                        break
                    else:
                        clear()
                        print('Escolha um item do menu.\n')