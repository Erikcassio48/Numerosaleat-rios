from random import randint
from collections import defaultdict

x = range(1000)

#Criando lista

numeros = []

for h in (x):
    numeros.append(h)
#Lista criada em numeros

y = []

#Criando laço onde conseguiremos 1000 números aleatórios entre 0 e 1000
for z in (x):
    num = randint(0,z)
    y.append(num)
    
lista_tamanho =  len(y)
print (lista_tamanho) #quantidade de úmeros aleatórios

#Obtendo a média

soma = sum(y)
print (soma)

def média(lista_tamanho):
    média = soma/lista_tamanho
    print(média)

média(lista_tamanho)
numeros_ordenados = sorted(y)

#Obtendo a Moda
word_counts = defaultdict(int)

for word in numeros_ordenados:
    word_counts[word] +=1
    print (word_counts)

