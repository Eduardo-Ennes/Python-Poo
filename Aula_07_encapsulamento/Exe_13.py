class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade
        self.__saldo = 0
        
    def mostrar_nome(self):
        print(f'Nome: {self.nome}')
        
    def mostrar_idade(self):
        print(f'Idade: {self._idade}')
        
    def _aumentar_idade(self, num):
        self._idade += num
    
    def __aumentar_saldo(self, quantidade):
        self.__saldo += quantidade
            
    def depositar(self, quantidade):
        self.__aumentar_saldo(quantidade)
        print(f'Saldo: R${self.__saldo:.3f}')
 
            
p = pessoa('Arias', 28)
p.mostrar_nome()
p._aumentar_idade(2)
p.mostrar_idade()
p.depositar(50)
p.depositar(1500)  