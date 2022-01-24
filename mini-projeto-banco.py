class Login:
    def __init__(self, usuario, senha, saldo):
        self.usuario = usuario
        self.senha = senha
        self.saldo = saldo

        #CAMPOS INPUT
        self.InputLogin = input('Usuario: ')
        self.InputPasswd = input('Senha: ')

    def logar_usuario(self):
        if self.usuario == self.InputLogin and self.senha == self.InputPasswd:
            print('=================================================')
            print('===========ITALU====UNIBANKO=====================')
            print('=================================================')
            print('=================================================')
            print(f'Olá {self.usuario}, Seja bem vindo(a) ao CAIXA!')
            print('=================================================')
            print('\n 1 - Saldo \n 2 - Sacar \n 3 - Depositar (qualquer valor) \n Digite a opção desejada: ')
            print('=================================================')
            if self.usuario == self.InputLogin:
                sessao.painel_usuario()
        else:
            print('Usuario ou Senha invalido')

    def painel_usuario(self):
        
        self.painel = input()

        print('Você escolheu a opção: ' + self.painel)

        if self.painel == '1':
            sessao.meu_saldo()
        elif self.painel == '2':
            sessao.meu_saque()
        elif self.painel == '3':
            sessao.meu_deposito()
        else:
            return sessao.painel_usuario()
            
    
    def meu_saldo(self):
        # OPÇÃO 1 DO PAINEL - SALDO
            print('Seu saldo é de: R$', sessao.saldo)
            return sessao.painel_usuario()

    def meu_saque(self):
        print(f'Você possui o saldo de: R$ {sessao.saldo}\n Qual valor deseja sacar ?')
        self.saque = int(input())

        if sessao.saldo >= self.saque:
            sessao.saldo -= self.saque
            print(f'Saque do valor {self.saque} efetuado com sucesso!')
            print(f'Saldo Total em sua conta R$', sessao.saldo)
            return sessao.painel_usuario()           
        else:
            print('Saldo insulficiente.')
            print(f'Saldo Total em sua conta R$', sessao.saldo)
            return sessao.painel_usuario()
        

    def meu_deposito(self):
        print(f'Você possui o saldo de: R$ {sessao.saldo}\n Qual valor deseja depositar ?')
        self.depositar = int(input())

        if sessao.saldo >= 0:
            sessao.saldo += self.depositar
            print(f'Deposito do valor {self.depositar} efetuado com sucesso!')
            print(f'Saldo Total em sua conta R$', sessao.saldo)
            return sessao.painel_usuario()
        else:
            print('Erro Contate o administrador.')
            print(f'Saldo Total em sua conta R$', sessao.saldo)
            return sessao.painel_usuario()
            
            

sessao = Login('joao', '123', 1)
sessao.logar_usuario()