class evento:
    def __init__(self):
        self.lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
    def comprar(self, num):
        if len(self.lista) == 0:
            print('Não há mais lugares disponíveis')
        elif num not in self.lista:
            print('OPS! Lugar não disponivél na lista. Tente novamente...')
        else:
            self.lista.remove(num)
            print(f'Compra realizada com sucesso.')
        
    def cancelar(self, num):
        if num in self.lista:
            print(f'OPS! revise sua reserva. Lugar se encontra disponivel na lista.')
        else:
            print('Cancelamento realizado com sucesso')
            self.lista.append(num)
        
    def disponiveis(self):
        if len(self.lista) == 0:
            print('Não há mais lugares disponíveis')
        else:
            print(f'Lugares dispóniveis:{sorted(self.lista)}')
     
            
a = evento()
a.comprar(1)
a.disponiveis()
a.comprar(2)
a.disponiveis()
a.cancelar(2)
a.disponiveis()
a.comprar(3)
a.comprar(4)
a.comprar(5)
a.disponiveis()
a.comprar(6)
a.comprar(7)
a.comprar(8)
a.disponiveis()
a.comprar(9)
a.comprar(10)
a.comprar(2)
a.disponiveis()
a.comprar(5)