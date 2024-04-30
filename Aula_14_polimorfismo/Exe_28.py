class veiculo:
    def mover(self):
        print('Veiculo se move por: ')

class carro(veiculo):
    def mover(self):
        print('Carro: se move por terra.')

class barco(veiculo):
    def mover(self):
        print('Barco: se move na água.')

class aviao(veiculo):
    def mover(self):
        print('Avião: se move voando.')
        
geral = veiculo()
geral.mover()
carro = carro()
carro.mover()
barco = barco()
barco.mover()
aviao = aviao()
aviao.mover()