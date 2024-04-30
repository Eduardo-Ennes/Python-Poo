class fatorial:
    def __init__(self, num):
        valor = 1
        for c in range(num, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            valor *= c 
        print(valor)
        
numero = fatorial(5)