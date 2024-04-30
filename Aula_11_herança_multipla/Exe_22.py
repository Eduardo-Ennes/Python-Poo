class musico:
    def tocando_instrumento(self):
        print('Estou tocando um instrumento')

class atleta:
    def correndo(self):
        print('Correndo na pista')
        
class musicoAtleta(musico, atleta):
    def exibir(self):
        print('Estou tocando um instrumento e correndo')

pessoa = musicoAtleta()
pessoa.tocando_instrumento()
pessoa.correndo()
pessoa.exibir()