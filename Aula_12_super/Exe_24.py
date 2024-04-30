class veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo
        
    def mostrar_info(self):
        print('Informações: ')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        
class carro(veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
        
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Cor: {self.cor}')
        print('-' * 20)

carro1 = carro('Ferrari','Roma','Vinho')
carro1.mostrar_info()

    
