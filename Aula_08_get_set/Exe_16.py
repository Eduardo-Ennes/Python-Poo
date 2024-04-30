class pet:
    def __init__(self):
        self._nome = '<desconhecido>'
        self._idade = 0
        self._peso = 0.0
    
    def mostrar_menu(self):
        print()
        print('1 - Definir o nome do pet')
        print('2 - definir a idade do pet')
        print('3 - definir o peso do pet')
        print('4 - mostrar informações')
        print('5 - Mostrar menu')
        print('6 - sair')
        print()
         
    def set_nome(self, nome):
        self._nome = nome
        
    def get_nome(self):
        return self._nome
    
    def set_idade(self, num):
        self._idade = num
           
    def get_idade(self):
        return self._idade 
    
    def set_peso(self, num):
        self._peso = num
        
    def get_peso(self):
        return self._peso
            
    def get_exibir(self):
        print()
        print('----- Dados do pet -----')
        print(f'Nome: {self._nome}')
        print(f'Idade: {self._idade} anos')
        print(f'Peso: {self._peso} kg')
        print('-' * 20)
        print()
  
p = pet()
            
print()
print('1 - Definir o nome do pet')
print('2 - definir a idade do pet')
print('3 - definir o peso do pet')
print('4 - mostrar informações')
print('5 - Mostrar menu')
print('6 - sair')

while True:
    print()
    print('-' * 20)
    num = int(input('Digite uma opção? '))
    
    if num < 1 or num > 6:
        print()
        print('-' * 20)
        print('Digite apenas uma das opções válidas.')
        
        
    
    elif num == 1:
        print('-' * 20)
        print()
        print('Nome')
        p.set_nome(input('Digite o nome do pet: '))
        
        
    elif num == 2:
        print('-' * 20)
        print()
        print('Idade')
        while True:
            try:
                idade = int(input('Digite uma idade: '))
            except:
                print('Digite uma idade válida.')
            else:
                p.set_idade(idade)
                break
    
    elif num == 3:
        print('-' * 20)
        print()
        print('Peso')
        while True:
            try:
                peso = float(input('Digite o peso do seu cachorro: '))
            except:
                print('Digite um peso válido.')
            else:
                p.set_peso(peso)
                break
    elif num == 4:
        p.get_exibir()  
        
    elif num == 5:
        p.mostrar_menu()    
        
    elif num == 6:
        print('-' * 20)
        print()
        print('Finalizando o programa. Muito obrigado(a).')
        print('-' * 20)
        break