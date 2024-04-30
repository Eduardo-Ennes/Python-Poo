# NONE ---> não valor

# IF (SE)
# ELIF (SE NÃO SE)
# ELSE (SE NÃO)
# IN (ENTRE)
# NOT IN (NÃO ESTÁ ENTRE)
# IS (É)
# AND (E)
# OR (OU)
# NOT (NÃO)
# WHILE (ENQUANTO) --> '''EXISTEM DUAS MANEIRAS DE SE INTERROMPER O PROGRAMA, (COM BREAK) E
# TORNANDO UMA CONDIÇÃO FALSA.'''
# BREAK --> Encerra o programa while
# FOR --> para cada


#MODULOS PARA TEXTO
# (LEN) --> número de caracteres da frase
# (.COUNT) --> número de vezes que a letra aparece na frase
# (.FIND) --> vai procurar a palavra desejada na frase, se existir irá indicar seu começo
# (.REPLACE) --> irá substituir um caracter desejado
# (.UPPER) --> todas maiúsculas
# (.LOWER) --> todas minisculas
# (.TITLE) --> todas as letras iniciais ficaram maiusculas
# (.SPLIT) --> dividi todas a frase por palavras e reustaurando o número de caracteres
# print('-'.JOIN(nome)) --> colaca um sinal desejado entre todas as letras da frase
# (.STRIP) --> remove os espaços das palavras
# (.STARTSWITH) --> 'A palavra começa com'
# (.CAPITALIZE) --> Coloca a primeira letra em maiusculo
# (INDEX) --> Mostra a colocação do que deseja
# (.INSERT) --> insere um valor em uma lista no indice que deseja
# (.Title) --> Colaca o texto em forma de titulo
# (HASATTR) --> para verificar se um metodo existe em uma variálvel


# ITERADOR:
# ITER --> me entrega cada valor individualmente da variavel
# NEXT --> me entrega o proximo valor da variavel por vez individualemnte


# FERREAMENTAS PARA USAR EM LISTA
# .APPEND ---> adiciona um item.
# .INSERT ---> adiciona um item no indice escolhido.
#  DEL ---> apaga o que deseja.
# .POP ---> apaga o item logo acima de onde foi digitado.
# .REMOVE ---> apaga um item deseja, porem, deve digitar o seu valor.
# .CLEAR ---> limpa a lista.
# .EXTEND ---> extende a lista.
# (SORTED) #--> Organiza em ordem alfabética ou númerica.
#     --> Cria uma copia
# (SORT) #--> Organiza em ordem númerica.
# (SORT(REVERSE=TRUE) #--> Organiza em ordem decrescente.
# (MAX) #--> mostra o maior número.
# (MIN) #--> mostra o menor número.
# (SUM) #--> soma os valores.
# .ISNUMERIC #--> se é um número.
# .COPY --> #faz uma copia.
# .COPY.DEPCOPY --> faz uma copia mais aprofundada.
#  Map --> O map vai aplicar uma função em cada item de uma lista de itens, ou seja,
#         é um for com uma chamada da função para aplicá-la a cada item da sua lista.
# .isisntance --> vai verificar o tipo do valor ex: "if isinstance (valor, int)"


# TUPLA = () --> é imutável

# LISTA = [] --> mutável
    # a = [1,2,3,4]
    # b = a[:] # ---> Cria uma copia da lista A, agora a lista B pode ser modificada sem modificar a lista A

# DICIONÁRIO = {}
#   .values --> retorna os valores escrito da chave
#   .keys --> retorna a variavel da chave
#   .items --> retorna os dois
#   .uptade --> serve para adicionar e atualizar os dicionários.

# SET (COMEÇA NA 819 UDEMYP.PY)
#   --> O (set) elimina os valores duplicados.
#   --> podem não garantir os valores em ordem, os trazendo em fora de ordem.
#   --> são dicionários por padrão, porém, podem ser convertidos para listas ou tuplas.
#   --> Dentro do (set) não pode ter listas ou dicionários pq são mutáveis, só aceita tuplas
      # por ser imutaveís.
#   --> não tem indice
#   .APP --> para adicionar valor ao set, porem, aceita apenas um
#   .UPDATE --> adicionar mais de um valor ao set
#   .CLEAR --> para limpar o set
#   .DISCART --> para apagar apenas um valor em set, porem, deve digitar o valor, não há indice.
#                deve-se usar "s1.update(())"
#   | --> usado para fazer a uniãodos valores do set.
#   & --> usado para fazer a interceção ou valores iguais entre os set.
#   (-)--> Mostra o unico valor a nao ter um igual, porem, deve-se estar a esquerda.
#          exp: "s3 = s1 - s2"
#   ^ --> valores que estão presentes apenas em cada um


# 004
# tuplas = começa na linha (2)
# listas = começa na linha (199)
# listas dentro de listas = começa na linha (450)



# TRATAMENTO DE ERROS
#   error.__class__.__name__ --> mostra qual foi o erro.
#       |__>  except (TypeError, IndexError) as error:
#             print('Nome:', error.__class__.__name__)



# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self

# __str__(self) - str   --> ambos fazem a mesma função, VERIFICÃO O VALOR DOS PARAMETROS NO OBJETOS, porém,
# __repr__(self) - str      repr é mais indicado para desenvolvedores e str quando é apenas para retornar ums string.

# __enter__ and __exit__ --> exemplo na UdemyP3_poo, linha 366




