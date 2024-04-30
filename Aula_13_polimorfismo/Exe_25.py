class calculadora:
    def __init__(self, num1, num2, num3=None):
        if num3 == None:
            print(f'{num1} + {num2} = {num1 + num2}')
        else:
            print(f'{num1} + {num2} + {num3} = {num1 + num2 + num3}')
            
calc = calculadora(5, 3)
cal2 = calculadora(5, 3, 2)