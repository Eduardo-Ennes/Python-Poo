# CLASSES E OBJETOS DEFININDO E INSTANCIANDO CLASSES

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
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}')
        
carro1 = carro('Ferrari', 'Roma', '2024')
carro1.exibir()
carro1.acelarar()
carro1.acelarar()
carro1.frear()
carro1.frear()
carro1.frear()      