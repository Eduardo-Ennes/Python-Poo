class manipulador:
    def __init__(self, lista):
        self.lista = lista
        
    def mostrar_lista(self):
        if len(self.lista) > 0:
            print(f'Lista: {self.lista}')
        else:
            print('A lista está vazia.')
        
    def maior(self):
        if len(self.lista) > 0:
            print(f'O maior número é: {max(self.lista)}')
        else:
            print('A lista está vazia.')
        
    def menor(self):
        if len(self.lista) > 0:
            print(f'O Menor número é: {min(self.lista)}')
        else:
            print('A lista está vazia.')
        
    def media(self):
        if len(self.lista) > 0:
            media_lista = sum(self.lista) / len(self.lista)
            print(f'A média da lista é: {media_lista:.1f}')
        else:
            print('A lista está vazia.')
        
    def adicionar(self, num):
        if num in self.lista:
            print(f'O número {num} já se encontra na lista. Digite outro.')
        elif num <= 0:
            print('Digite números que sejam diferentes de 0 e não negativos.')
        else:
            print('Adicionado com sucesso.')    
            self.lista.append(num) 
    
    def deletar(self, num):
        if num in self.lista:
            print('Número removido com sucesso.')
            self.lista.remove(num)
        else:
            print(f'O número {num} não está na lista.')

li = []  
while True:
    try: 
        num = int(input('Digite um número: '))
    except:
        print('Digite apenas números interios.')
    else:
        li.append(num)
        lista = manipulador(li)
    res = str(input('Deseja continuar [S/N]: '))[0]
    if res not in 'SsNn':
        print('Digite apenas SIM ou Não.')
    elif res in 'Ss':
        print('Continuando')
    else:
        break

while True:    
    print()    
    print('-' * 20)
    print('Escolha uma opção:\n1 - adicionar número\n2 - Remover número\n3 - Maior número\n4 - Menor número\n5 - Calcular média\n6 - Mostrar lista\n7 - Sair')
    while True:
        print()
        op = int(input('Digite uma das opções: '))
        if op < 0 or op > 7:
            print('Digite apenas uma das opções.')
        else:
            break   
    
    if op == 1:
        print()
        print('-' * 20)
        print('Adicionar número.')
        while True:
            try: 
                num = int(input('Digite um número: '))
            except:
                print('Digite apenas números interios.')
            else:
                li.append(num)
                lista = manipulador(li)
            res = str(input('Deseja continuar [S/N]: '))[0]
            if res not in 'SsNn':
                print('Digite apenas SIM ou NÃO.')
            elif res in 'Ss':
                print('Continuando')
            else:
                break
            
    elif op == 2:
        print()
        print('-' * 20)
        print('2 - Remover número.')
        while True:
            try:
                num = int(input('Digite um número: '))
            except:
                print('Digite apenas números inteiros.')
            else:
                lista.deletar(num)
            res = str(input('Deseja continuar [S/N]: '))[0] 
            if res not in 'SsNn':
                print('Digite apenas SIM ou Não.')
            elif res in 'Ss':
                print('Continuando')
            else:
                break
            
    elif op == 3:
        print()
        print('-' * 20)
        print('Maior número')
        lista.maior()
    
    elif op == 4:
        print()
        print('Menor número')
        lista.menor()
        
    elif op == 6:
        print()
        print('-=' * 20)
        print('Mostrar lista.')
        lista.mostrar_lista()
        print('-=' * 20)
    
    elif op == 5:
        print()
        print('-' * 20)
        print('Calculando a média.')
        lista.media()
        
    if op == 7:
        print('SAINDO DO PROGRAMA. MUITO OBRIGADO!')
        break    