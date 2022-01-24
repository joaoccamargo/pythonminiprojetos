class Clientes:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano

        self.lista_planos = ['Basic', 'Premium']

        if plano in self.lista_planos:
            self.plano = plano
        else:
           raise Exception('Plano invalido')
    
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
            print('Mudou para um novo plano!')
        else:
            print('Erro ao mudar de plano!')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme {filme}')
        elif self.plano == 'Premium':
            print(f'Ver filme {filme}')
        elif self.plano == 'Basic' and plano_filme == 'Premium':
            print('Você é Basic faça o upgrade para Premium')
        else:
            print('Plano Invalido!')




cliente = Clientes('Joao', 'joao@email.com', 'Premium')
print(cliente.plano)
cliente.mudar_plano('Basic')
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'Premium')
cliente.mudar_plano('Premium')
cliente.ver_filme('Harry Potter', 'Premium')
