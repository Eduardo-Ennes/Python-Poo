class estudantes:
    def __init__(self):
        self.lista = list()
        
    def adicionar(self, nome, n1, n2):
        self.dados = []
        self.dados.append(nome)
        self.dados.append(n1)
        self.dados.append(n2)
        self.dados.append((n1 + n2) / 2)
        self.lista.append(self.dados[:])
        self.dados.clear
        
    def mostrar_geral(self):
        if len(self.lista) == 0:
            print()
            print('-' * 20)
            print('A lista de alunos está vazia.')
        else:
            print()
            print('-' * 20)
            print('Lista geral de alunos: ')
            for i, c in enumerate(self.lista):
                print(f'Número: {i} - Nome: {c[0]}')
        
    def mostrar_aluno(self, n):
        if len(self.lista) == 0:
            print()
            print('-' * 20)
            print('A lista de alunos está vazia.')
        else:
            print()
            print('-' * 20)
            print('Informações: ')
            print(f'Nome: {self.lista[n][0]}, Nota 1: {self.lista[n][1]}, Nota 2: {self.lista[n][2]}, Média: {self.lista[n][3]}')
            
    def atualizar_info(self, i1, i2, valor):
        self.lista[i1][i2] = valor
        if i2 == 1 or i2 == 2:
            self.lista[i1][3] = (self.lista[i1][1] + self.lista[i1][2]) / 2
        else:
            self.lista[i1][0] = valor
        print('Atualizado com sucesso.')
        

p = estudantes()   
while True:
    print()
    print('-' * 20)
    print('1 - Adicionar aluno')
    print('2 - Mostrar lista geral')
    print('3 - Mostrar informações do aluno(a)')
    print('4 - Atualizar informação')
    print('5 - Sair do programa')
    print('-' * 20)
    while True:
        print()
        print('-' * 20)
        try:
            res = int(input('Digite uma das opções: '))
        except:
            print('Digite apenas uma das opções disponivés!')
        else:
            break
    
    if res == 1:
        nome = str(input('Digite um nome: ')).upper().strip()
        
        while True:
            try:
                nota1 = float(input('Digite a nota 01: '))
            except:
                print('Digite um nota válida!')
            else:
                break
            
        while True:
            try:
                nota2 = float(input('Digite a nota 02: '))
            except:
                print('Digite um nota válida!')
            else:
                break
        p.adicionar(nome, nota1, nota2)
    
    elif res == 2:
        p.mostrar_geral()
        
    elif res == 3:
        p.mostrar_aluno(int(input('Digite o número correspondente para visualizar as notas do aluno(a): ')))
    
    elif res == 4:
        while True:
            try:
                ind1 = int(input('Digite o número correspondente do aluno: '))
            except:
                print('Digite apenas um dos indices correspondentes!')
            else: 
                break
        while True:
            try:
                ind2 = int(input('Digite o número correspondente do que deseja atualizar: '))
            except:
                print('Digite apenas um dos indices correspondentes!')
            else: 
                break
        if ind2 == 0: 
            valor = str(input('Digite o nome do aluno(a): '))
            p.atualizar_info(ind1, ind2, valor)
        elif ind2 == 1 or ind2 == 2:
            valor = float(input('Digite a nova nota: '))
            p.atualizar_info(ind1, ind2, valor)
        else:
            print('Indice errado...Tente novamente!')
    
    elif res == 5:
        print('-' * 20)
        print('Saindo do programa... Muito obrigado!')
        print()
        break
    
    else:
        print()
        print('ATENÇÃO!')
        print('Digite uma das opções do menu!')
        print('-' * 20)   