class animal:
    def falar(self):
        print('O animal está falando')
    
class cachorro(animal):
    def falar(self):
        super().falar()
        print('O cachorro diz: Au au...')
        
cachorro = cachorro()
cachorro.falar()