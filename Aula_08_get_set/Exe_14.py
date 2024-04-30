class produto:
    def __init__(self, nome, preco):
        self.nome = nome 
        self.preco = preco  
        
    def set_preco(self, preco):
        if preco <= 0:
            print('O valor não pode ser zero ou negativo.')
        else:
            self.preco = preco
    
    def porcentagem(self, porcento):
        if self.preco > 0:
            self.novo_preco = self.preco - (porcento / 100 * self.preco)
            self.set_preco(self.novo_preco)
        else:
            print('O valor do preço está zerado.')
    
    def get_preco(self):
        print(f'Saldo: R${self.preco}')

p = produto('Camisa', 50)
p.get_preco()
p.porcentagem(50)
p.get_preco()