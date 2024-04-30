# INTRODUÇÃO A POO 

class livro:
    def __init__(self, nome, autor, ano):
        self.livro = nome
        self.autor = autor 
        self.ano = ano
        
    def imagem(self):
        return f'{self.livro}, {self.autor}, {self.ano}'
   
        
meu_livro = livro('Vikings', 'Jack Morvel', '2002')
print(meu_livro.imagem())     