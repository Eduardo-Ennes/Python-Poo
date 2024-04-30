class termostato:
    def __init__(self, temperatura=20):
        self.temperatura = temperatura
        print(f'A temperatura por padrão é: {self.temperatura}°')
        
    def aumentar(self, valor):
        self.temperatura += valor
        print(f'A temperatura foi aumentada em {valor}°.')
        
    def diminuir(self, valor):
        self.temperatura -= valor
        print(f'A temperatura foi diminuida em {valor}°.')
        
    def configurar(self, temperatura):
        self.temperatura = temperatura
        print(f'A temperatura foi configurada para {self.temperatura}°')
    
    def atual(self):
        print(f'A temperatura atual é: {self.temperatura}°')
   
     
a = termostato()
a.aumentar(80)
a.atual()
a.diminuir(10)
a.atual()
a.configurar(21)
a.atual()
a.diminuir(11)
a.atual()