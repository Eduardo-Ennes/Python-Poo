class animal:
    def som(self):
        print('O animal faz o som de:')
        
class cachorro(animal):
    def som(self):
        print('O cachorro late')
        
class gato(animal):
    def som(self):
        print('O gato mia')
        
animal = animal()
animal.som()
cachorro = cachorro()
cachorro.som()
gato = gato()
gato.som()