class rotina:
    def __init__(self, nome):
        self.nome = nome
        self.disperso = True
        self.comendo = True
        self.dirigindo = False
    
    def acordar(self):
        if self.disperso == False:
            print(f'{self.nome} está acordando.')
            print(f'{self.nome} agora está acordado.')
            self.disperso = True
        else:
            print(f'{self.nome} já está acordado.')

    def comer(self):
        if self.disperso == False or self.dirigindo == True:
            print(f'{self.nome} não pode comer por que está dirigindo ou dormindo.')
        elif self.comendo:
            print(f'{self.nome} já está comendo.')
         
        else:
            print(f'{self.nome} está indo comer.')
            print(f'{self.nome} está comendo agora.') 
            self.comendo = True 
              
    def parar_de_comer(self):
        if self.comendo:
            print(f'{self.nome} está parando de comer.')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo no momento.')
           
    def dirigir(self):
        if self.disperso == False or self.comendo == True:
            print(f'{self.nome} não pode dirigir por que está dormindo ou comendo.')
        elif self.dirigindo:
            print(f'{self.nome} já está dirigindo.')
        else:
            print(f'{self.nome} está indo dirigir.')
            self.dirigindo = True
            
    def parar_de_dirigir(self):
        if self.dirigindo:
            print(f'{self.nome} está parando de dirigir.')
            self.dirigindo = False
        else:
            print(f'{self.nome} não está dirigindo no momento.')
            
    def dormir(self):
        if self.comendo == True or self.dirigindo == True:
            print(f'{self.nome} não pode dormir por que está comendo ou dirigindo')
        elif self.disperso == False:
            print(f'{self.nome} já está dormindo.')
        else:
            print(f'{self.nome} foi dormir.')
            self.disperso = False
            
            
eu = rotina('Eduardo') 
eu.acordar()
eu.comer()
eu.comer()
eu.parar_de_comer()
eu.dirigir()
eu.dirigir()
eu.parar_de_dirigir()
eu.dormir()
eu.dormir()
eu.dirigir()
eu.parar_de_comer()