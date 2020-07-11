from random import randint

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

