class animal:

    def fazer_som(self):
        print('O animal faz o som de...')

class cachorro(animal):
    def __init__(self):
        super().__init__()
        
    def fazer_som(self):
        print('O cachorro faz Woof Woof')
        
    def latir(self):
        print('Woof Woof')

class gato(animal):
    def __init__(self):
        super().__init__()
        
    def fazer_som(self):
        print('O gato faz Miau Miau')
    
    def miar(self):
        print('Miau Miau')
   
animal = animal()
animal.fazer_som()
cachorro = cachorro()
cachorro.fazer_som()
cachorro.latir()  
print('-' * 20)     
gato = gato()
gato.fazer_som()
gato.miar()