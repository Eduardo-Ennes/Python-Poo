class contatos:
    def __init__(self):
        self.telefones = []
        self.lista = {}
        
    def menu(self):
        print()
        print('-' * 20)
        print('1 - Adicionar contato')
        print('2 - Remover contato')
        print('3 - Todos os contatos da agenda')
        print('4 - Buscar conatato')
        print('5 - Mostrar menu')
        print('6 - Sair do programa')
        print('-' * 20)
    
    def adicionar(self, nome, numero, email):
        self.lista['Nome'] = nome
        self.lista['Número'] = numero
        self.lista['Email'] = email
        self.telefones.append(self.lista.copy())
        self.lista.clear
        print('Adicionado com sucesso.')
        
    def remover(self, num):
        try:
            self.telefones.remove(self.telefones[num])
            print('Removido com sucesso.')
        except:
            print('Contato não encontrado.')
    
    def lista_contatos(self):
        if len(self.telefones) <= 0:
            print('Lista de contatos se encontra vazia.')
        else:
            print()
            print('-' * 20)
            for i, c in enumerate(self.telefones):
                print(f'{i}° - {c}')
            
    def contato(self, nome):
        if len(self.telefones) <= 0:
            print('Lista de contatos se encontra vazia.')
        else:
            print()
            print('-' * 20)
            for c in self.telefones:
                for v in c.items():
                    if nome in c['Nome']:
                        print(v)
             
cel = contatos()
cel.menu()
while True:
    print()
    print('-' * 20)
    while True:
        try:
            res = int(input('Digite uma das opções: '))
        except:
            print('Digite apenas uma das opções correspondentes.')
        else:
            break
    
    if res == 1:
        print()
        nome = str(input('Digite o nome: ')).upper().strip()
        while True:
            try:
                numero = int(input('Digite o número de telefone: '))
            except:
                print('Digite um número de telefone válido.')
            else:
                if numero > 99999999999:
                    print('Digite um número de telefone válido.')
                else:
                    break
        while True: 
            email = str(input('Digite o e-mail: '))
            if '@' not in email:
                print('Digite um e-mail válido.')
            else:
                break 
        cel.adicionar(nome, numero, email)
        
    elif res == 2:
        print()
        while True: 
            try:
                indice = int(input('Digite o número do índice do contato que deseja remover: '))
            except:
                print('Digite apenas número inteiro.')
            else:
                cel.remover(indice)
                break
    
    elif res == 3:
        cel.lista_contatos()
        
    elif res == 4:
        print()
        print('-' * 20)
        print('Deve-se digitar o nome inteiro e corretamente da pessoa.')
        cel.contato(str(input('Digite o nome do contato que deseja encontrar: ')).upper().strip())
    
    elif res == 5:
        cel.menu()
    
    elif res == 6:
        print()
        print('-' * 20)
        print('Saindo do programa...Muito obrigado')
        print('-' * 20)
        print()
        break

    else:
        print()
        print('Digito inválido...')
        print('Digite apenas uma das opções correspondentes.')