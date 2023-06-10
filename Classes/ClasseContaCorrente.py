class conta_corrente:
    def __init__(self,nome='unknown',numero_conta=0,saldo=0):
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo
        
    def alterarNome(self):
        pergunta = input('\nQuer alterar o nome da sua conta? [s/n]: ')
        pergunta = pergunta[0].lower()
        if pergunta =='s':
            novo_nome = input('\nColoque o novo nome da conta: ')
            self.nome = novo_nome
            print('Seu nome foi atualizado para %s'%self.nome)
        else: print('Seu nome continua o mesmo %s'%self.nome)
        
    def despositar(self):
        pergunta = input('\nGostaria de depositar na sua conta? [s/n]: ')
        pergunta = pergunta[0].lower()
        if pergunta == 's':
            novo_saldo = int(input('\nColoque a quantia que gostaria de depositar: '))
            self.saldo = novo_saldo
            print('Seu saldo foi pra %5.2f'%self.saldo)
        else: print('Seu saldo continua o mesmo $%5.2f'%self.saldo)
        
    def sacar(self):
        pergunta = input('\nGostaria de sacar da sua conta? [s/n]: ')
        pergunta = pergunta[0].lower()
        if pergunta == 's':
            novo_saque = int(input('\nColoque o quanto quer sacar de sua conta: '))
            if novo_saque > self.saldo:
                print('Voce nao possui tanto dinheiro assim ;-;')
            else:
                novo_saque = self.saldo - novo_saque
                print('Seu novo saldo é de $%5.2f'%novo_saque)
        else: print('Seu saldo continua o mesmo $%5.2f'%self.saldo)
        
Vitor = conta_corrente('Vitor')
Vitor.alterarNome()
Vitor.despositar()
Vitor.sacar()