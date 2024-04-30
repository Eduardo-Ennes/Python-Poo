class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    
    def mostrar_info(self):
        print(f'Nome: {self.nome}, idade: {self.idade} anos')
        
class estudante(pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        
    def estudar(self):
        print(f'{self.nome} está estudando.')
        
class professor(pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        
    def dis_info(self):
        print(f'{self.nome} é professor de {self.disciplina}.')
        
pessoa = pessoa('Maira', 99)
pessoa.mostrar_info()
estudante = estudante('ganso', 35, 12345)
estudante.estudar()
professor = professor('Eistein', 100, 'Fisíca')   
professor.dis_info()
professor.mostrar_info()