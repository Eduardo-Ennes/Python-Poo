class conversor:
    def __init__(self, palavra):
        self.palavra = palavra
        
    def maiuscula(self):
        print(self.palavra.upper())
        print()
        
    def minusculas(self):
        print(self.palavra.lower())
        print()
        
    def capitalizar(self):
        print(self.palavra.capitalize())
        print()
        
    def titulo(self):
        print(f'Formatação de titulo: {self.palavra.title()}')
        
    def numvogais(self):
        num = 0
        for c in self.palavra:
            if c.lower() in 'aeiouòàèìùáéóíãôê':
                num += 1
        print(f'A palavra ({self.palavra}) tem {num} vogais.')
        print()
        
    def numconsoantes(self):
        num = 0
        for c in self.palavra:
            if c.strip() not in 'aeiouAEIOUéÉãÃóÓõ':
                num += 1
        print(f'A palavra ({self.palavra}) tem {num} consoantes.')
        print()
        
    def numa(self):
        num = self.palavra.count('a')
        print(f'Letra (A) aparece {num} vezes na palavra {self.palavra}.')
        
    def pesquisar(self, nome):
        print(self.palavra)
        pesquisa = nome.lower()
        nova = self.palavra.lower().count(pesquisa)
        if nova > 0:
            print(f'A palavra {pesquisa} aparece {nova} vezes na frase.')
        else:
            print(f'A palavra {pesquisa} não aparece {nova} em frase.')
            
    def frase_atual(self):
        print(f'Palavra atual: {self.palavra}')
        print()


a = conversor(str(input('Digite um palavra: ')))
print('1 - Maiuscula\n2 - Minusculas\n3 - Capitalizar a primeria letra\n4 - Formatação de titulo\n5 - Números de vogais\n6 - Número de consoantes\n7 - Número da letra A\n8 - Pesquisar palavra\n9 - Mostra frase atual\n10 - Sair')
while True:
    while True:
        try:
            print()
            num = int(input('Digite uma das opções: '))
        except:
            print('Digite apenas uma das opções.')
        else:
            break
    if num == 1:
        a.maiuscula()
        
    elif num == 2:
        a.minusculas()
        
    elif num == 3:
        a.capitalizar()

    elif num == 4:
        a.titulo()
        
    elif num == 5:
        a.numvogais()
        
    elif num == 6:
        a.numconsoantes()
        
    elif num == 7:
        a.numa()
        
    elif num == 8:
        print('Verificar se a palavra faz parte da palavra digitada.')
        a.pesquisar(str(input('Digite a palavra que deseja pesquisar: ')))
    
    elif num == 9:
        a.frase_atual()
        
    elif num == 10:
        print('Saindo do programa')
        break
print('Muito obrigado!')  