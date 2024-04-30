class termometro:
    def __init__(self):
        self._temperatura = 0
    
    @property    
    def _graus(self):
        print(f'Temperatura: {self._temperatura} C°') 
        if self._temperatura <= -30:
            print('Frio extremo')
        elif self._temperatura < -15 and self._temperatura > -30:
            print('Frio quase-extremo')
        elif self._temperatura < -5 and self._temperatura >= -15:
            print('Muito frio')
        elif self._temperatura <= 0 and self._temperatura >= -5:
            print('Frio congelante')
        elif self._temperatura > 0 and self._temperatura <= 10:
            print('Frio')
        elif self._temperatura > 10 and self._temperatura < 17:
            print('Pouco frio')
        elif self._temperatura >= 17 and self._temperatura <= 25:
            print('Temperatura ambiente')
        elif self._temperatura > 25 and self._temperatura <= 30:
            print('Quente')
        elif self._temperatura > 30 and self._temperatura <= 40:
            print('Muito quente')
        elif self._temperatura > 40 and self._temperatura <= 50:
            print('Quente quase-extremo')
        elif self._temperatura > 50:
            print('Calor extremo')
            
    @_graus.setter
    def _graus(self, valor):
        try:
            isinstance(valor, float)
        except:
            print('Dígito inválido.')
            print('A temperatura deve ser um número real ou um inteiro.')
        else:
            self._temperatura = valor
        
t = termometro()      
t._graus = -5
t._graus          