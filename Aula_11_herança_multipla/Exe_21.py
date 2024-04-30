class mamifero:
    def __init__(self):
        print('Sou um mamifero')
    
    def comendo(self):
        print('Comendo...')

class ave:
    def __init__(self):
        print('Sou uma ave')
        
    def voar(self):
        print('Voando...')

class morcego(ave, mamifero):
    def __init__(self):
        print('Sou um morcego')
        
    def emitir_som(self):
        print('Emitindo som de ecolocalização')
        
morcego = morcego()
