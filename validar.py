#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(0.5)   #contagem em segundos 
print('CONTAGEM')


#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

conta = 0
soma = 0

for s in range(1, 501, 2):
    if s % 3 == 0:
        soma += s
        conta += 1
print(f'A soma de todos os valores {conta} e solicitados {soma} ')





#mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Numero:    '))

for i in range(0, 11):
    print('{} x {} = {}'.format(n, i, n*i))
print('Tabuada')

#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
for i in range(1 , 7):
    user = int(input('Digita um numero:   '))
    if user % 2 == 0:
        soma += user
print(f'A soma dos numeros pares é: {soma}')


#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Qual é o seu nome?   '))
tot = 0
for a in range(1, num + 1):
    if num % a == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(a), end=' ')
print('\nO numero {} foi divisivel por {} vezes'.format(num, tot))

#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:


frase = input(':').strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for i in range(len(junto) - 1, -1, -1):
    inverso += junto[i]
print('o inverso {} e {}'.format(junto, inverso))
if inverso == junto:
    print('E um palindromo')
else:
    print('Não um palindromo')

#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

maior = 0
menor = 0
for i in range(1, 8):
    ano = int(input(f'Em que ano a {i} pessoa nasceu: '))
    idade = 2024 - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade ')
print(f'Ao todo tivemos {menor} pessoas menores de idade ')


#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'O peso {p} pessoa:   '))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso lido foi {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')

n1 = float(input(':'))
n2 = float(input(':'))
n3 = float(input(':'))
n4 = float(input(':'))

media = (n1 + n2 + n3 + n4)/4

if media >= 7:
    print('Aprovado')
elif media <= 7:
    print('Reprovado ')
else:
    print('Recuperar nota')

#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa,
#mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0
media = 0
maioridadehomen = 0
nomevelho = ' '
mulher = 0

for x in range(1, 5):
    print(f'----- {x} pessoa ------')
    nome = input('NOME: ')
    idade = int(input('IDADE: '))
    sexo = input('GENERO: [M]/[F] ').strip()
    soma += idade
    if x == 1 and sexo in 'Mn':
        maioridadehomen = idade
        nomevelho = nome
    if sexo  in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1



media = idade / 4
print(f'A idade do grupo de pessoas é a média de {media} anos')
print(f'O homen mais velho tem {maioridadehomen} e se chama {nomevelho}')
print(f'Ao todo são {mulher} mulheres com menos de 20 anos')


# usando while impar ou par
n = 1
par = impar = 0
while n != 0:
    n = int(input(':  '))
    if n != 0:
        if n % 2 == 0:
            par += 1
    else:
        impar += 1

print(f'Voce digitou {n} numeros pares {par} e o numeros impares {impar}')