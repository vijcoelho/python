import random

tabela = [1,2,3,4,5,6,7,8,9]
sequencias = [{1,2,3}, {4,5,6}, {7,8,9},{1,4,7}, {2,5,8}, {3,6,9},{1,5,9}, {3,5,7}]

def menu():
    print('{}=============================={}'.format('\033[34m', '\033[m'))
    print('{}|Bem-Vindo Ao Jogo Da Velhota|{}'.format('\033[31m', '\033[m'))
    print('{}=============================={}'.format('\033[34m', '\033[m'))
    print(input('{}\n\nPRESSIONE ENTER PARA JOGAR{}'.format('\33[33m','\033[m')))

def exibir_tabuleiro(tabela):
    print("\t┌───┬───┬───┐")
    print(f"\t│ {tabela[0]} │ {tabela[1]} │ {tabela[2]} │")
    print("\t├───┼───┼───┤")
    print(f"\t│ {tabela[3]} │ {tabela[4]} │ {tabela[5]} │")
    print("\t├───┼───┼───┤")
    print(f"\t│ {tabela[6]} │ {tabela[7]} │ {tabela[8]} │")
    print("\t└───┴───┴───┘")

def jogar_aleatorio(random):    
    jr = random.randint(1,2)
    if jr == 1:
        print('Começa com X')
        return 'X'
    else:
        print ('Começa com O')
        return 'O'
       
def jogando_jogo():
    jogador = jogar_aleatorio(random)
    
    rodadas = 0
    while rodadas < 9:
        rodadas += 1
        print(f'Vez do {jogador}')
        pegarnumero = int(input('Deseja colocar em que lugar: '))
        if pegarnumero not in range(1,10):
            print("Tem que ser um número de 1 a 9")
            pegarnumero = int(input('Coloque corretamente agora: '))
        elif tabela[pegarnumero - 1] == 'X' or tabela[pegarnumero - 1] == 'O':
            print("Este quadrado já foi preenchido")
        else:
            tabela[pegarnumero - 1] = jogador
            exibir_tabuleiro(tabela)
            vencedor = verificar_vencedor(sequencias, jogador)
            if vencedor:
                print(f'O jogador {jogador} ganhou!')
                return
            if rodadas == 9:
                print("Deu empate!")
                return
            if jogador == 'X':
                jogador = 'O'
            else:
                jogador = 'X'

def verificar_vencedor(sequencias, jogador):
    for seq in sequencias:
        if all(tabela[i-1] == jogador for i in seq):
            return True
    return False

menu()
exibir_tabuleiro(tabela)
jogando_jogo()