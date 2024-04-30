class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0
        
    def acelarar(self):
        self.velocidade += 10
        print('O carro acelerou')
        print(f'A velocidade atual é de: {self.velocidade} km')
        
    def frear(self):
        self.velocidade -= 10
        if self.velocidade > 0:
            print('O carro diminuiu')
            print(f'A velocidade atual é de: {self.velocidade} km')
        if self.velocidade < 0:
            self.velocidade = 0
            print('O carro está parado')
            print(f'A velocidade atual é de: {self.velocidade} km')
        
    def exibir(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}, velocidade: {self.velocidade} km/h')
        
lista_carros = []

while True:
    print('--- MENU --- ')
    print('1 - Adicionar novo carro')
    print('2 - Exibir Informações dos carros')
    print('3 - Acelerar o carro')
    print('4 - Frear o carro')
    print('5 - Sair')
    
    while True:
        try:
            res = int(input('Digite um opção: '))
        except:
            print('Digite apenas números inteiros!')
        else:
            if res < 1 or res > 5:
                print('Tente novamente... Escolha uma das 5 opções')
            else:
                break
            
    if res == 1:
        marca = str(input('Digite a marca do carro: '))
        modelo = str(input('Digite o modelo do carro: '))
        ano = str(input('Digite o ano do carro: '))
        novo_carro = carro(marca, modelo, ano)
        lista_carros.append(novo_carro)    
         
    elif res == 2:
        if lista_carros:
            for c in lista_carros:
                c.exibir()
        else:
            print('A lista se encontra vazia')
            
    elif res == 3:
        modelo =str(input('Qual o modelo deseja acelerar: '))
        for carro in lista_carros:
            if carro.modelo == modelo:
                carro.acelarar()
                break
            else:
                print('Modelo não encontrado!')
        
    elif res == 4:
        modelo =str(input('Qual o modelo deseja frear: '))
        for c in lista_carros:
            if carro.modelo == modelo:
                carro.frear()
                break
        else:
            print('Modelo não encontrado!')
        
    elif res == 5:
        print('Saindo do programa')
        break