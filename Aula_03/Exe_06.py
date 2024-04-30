class frutas:
    def __init__(self, fruta, preco=0, quant=0):
        self.fruta = fruta
        self.preco = preco 
        self.quant = quant
        
    def exibir(self):
        print(f'Fruta: {self.fruta}')
        print(f'Preço por kg: R${self.preco:.2f}')
        print(f'Quantidade em estoque: {self.quant}')   
             
lista = []  
res = ' '    
while True:
    nome = input('Digite o nome da fruta: ')
    print('Adicionado com sucesso...')
    
    while True:
        try:
            p = float(input('Digite o preço da fruta: R$'))
        except:
            print('Digite um preço válido!')
        else:
            if p < 0:
                print('Digite um preço válido!')
            else:
                print('Adicionado com sucesso...')
                break
            
    while True:
        try:
            quant = int(input('Digite a quantidade em estoque: '))
        except:
            print('Digite um preço válido!')
        else:
            if quant < 0:  
                print('Digite um preço válido!')
            else:
                print('Adicionado com sucesso...')
                break
    produto = frutas(nome, p, quant)
    lista.append(produto)
    
    while True:
        res = str(input('Deseja continuar [S/N]: '))
        if res in 'Nn':
            break 
        elif res in 'Ss':
            print('Continuando...')
            break 
        else:
            print('Digite Sim ou Não!')
    if res in 'Nn':
        break
    
print()
print('--- FRUTAS --- ')
for c in lista:
    c.exibir()
    print('---------------')    