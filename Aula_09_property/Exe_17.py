class retangulo:
    def __init__(self, altura=0, largura=0):
        self._altura = altura
        self._largura = largura
        
    @property
    def largura(self):
        print(f'Largura: {self._largura}m²')
    
    @largura.setter
    def largura(self, valor):
        if valor >= 0:
            self._largura = valor
        else:
            print('A largura deve ser maior do que zero.')
            
    @property
    def altura(self):
        print(f'Altura: {self._altura}m²')
        
    @altura.setter
    def altura(self, valor):
        if valor >= 0:
            self._altura = valor
        else:
            print('A altura deve ser maior do que zero.')
            
    @property       
    def area(self):
        print(f'Calculo: {self._altura}m² x {self._largura}m²')
        print(f'Área: {self._largura * self._altura}m²')
              
r = retangulo(7, 5)
r.largura
r.altura
r.altura = -1
r.largura = -1
r.area