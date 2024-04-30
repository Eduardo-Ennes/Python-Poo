class evento:
    def __init__(self, numero=10):
        self.numero = numero
        
    def reservar(self):
        if self.numero <= 0:
            print('Não há mais reservas disponíveis.')
        else:
            print('Reserva realizada com sucesso.')
            self.numero -= 1
            
    def cancelar(self):
        if self.numero >= 10:
            print('Não há como cancelar. Todos os lugares estão disponíveis.')
        else:
            print('Cancelamento realizado com sucesso.')
            self.numero += 1
        
    def disponiveis(self):
        if self.numero > 0:
            print(f'Lugares disponíveis: {self.numero}')
        else:
            print('Reservas esgotadas!')
        
        
a = evento()
a.disponiveis()
a.reservar()
a.disponiveis()
a.reservar()
a.disponiveis()
a.cancelar()
a.cancelar()
a.cancelar()
a.disponiveis()