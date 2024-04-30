class impressora:
    def __init__(self, variavel='Vazio'):
        self.variavel = variavel 
        print(f'Dado: {self.variavel}')
        print('----')
        if self.variavel == 'Vazio':
            print('O campo deve conter algum valor.')
        elif isinstance(self.variavel, str):
            print('Será impressa como um texto.')
        elif isinstance(self.variavel, list):
            print('Será impresso como uma lista.')
        elif isinstance(self.variavel, dict):
            print('Será impresso como um dicionário.')
        elif isinstance(self.variavel, tuple):
            print('Será impresso como uma tupla.')
        else:
            print('Forma de impressão não identificada.')
            
text = impressora()