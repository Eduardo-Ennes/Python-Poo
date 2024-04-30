class jogador:
    def __init__(self, nome, posicao, num_camisa, gols=0):
        self.nome = nome
        self.posicao = posicao
        self.num_camisa = num_camisa
        self.gols = gols
        
    def exibir(self):
            return f'Jogador: {self.nome}\nposicao: {self.posicao}\nNúmero da camisa: {self.num_camisa}\ngols: {self.gols}'

lista = [] 
res = ' '
while True:
    atleta = str(input('Digite o nome do jogador: '))
    posicao = str(input('Digite a posição do jogador: '))
    num = int(input('Digite o número da camisa: '))
    gol = int(input('Digite o número de gols: '))
    jogo = jogador(atleta, posicao, num, gol)
    lista.append(jogo)
    while True:
        res = str(input('Deseja continuar [S/N]: '))
        if res in 'Nn':
            break
        elif res in 'Ss':
            break
        else:
            print('Digite apenas Sim ou Não!') 
    for c in lista:
        print(c.exibir())   
    if res in 'Nn':
        print('Programa terminando...')
        break             