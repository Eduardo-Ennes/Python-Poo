class pet:
    def __init__(self):
        self._nome = ''
        self._idade = 0
        self._peso = 0.0
         
    def set_nome(self):
        nome= str(input('Digite um nome: ')).strip()
        self._nome = nome
        
    def get_nome(self):
        return self._nome
    
    def set_idade(self):
        print('-' * 20)
        while True:
            try:
                idade = int(input('Digite uma idade: '))
            except:
                print('Digite uma idade válida.')
            else:
                self._idade = idade
                break
            
    def get_idade(self):
        return self._idade 
    
    def set_peso(self):
        print('-' * 20)
        while True:
            try:
                peso = float(input('Digite o peso do seu cachorro: '))
            except:
                print('Digite um peso válido.')
            else:
                self._peso = peso
                break
        
    def get_peso(self):
        return self._peso
            
    def get_exibir(self):
        print()
        print('-' * 20)
        print('----- Dados do pet -----')
        print(f'Nome: {self._nome}')
        print(f'Idade: {self._idade} anos')
        print(f'Peso: {self._peso} kg')
            
p = pet()   
p.set_nome()
p.set_idade()
p.set_peso()
p.get_exibir()