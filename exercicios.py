##Questão 1
Escreva um programa que peça ao usuário para digitar um número inteiro positivo e imprima todos os números pares de 1 até o número digitado.

number = int(input("Digite um número: "))

for number in range(0,number + 1):
    if (number % 2 == 0):
        print(number)


##Questão 2
Escreva um programa que leia um número inteiro positivo e calcule o seu fatorial. O fatorial de um número é o produto de todos os inteiros positivos menores ou iguais a ele. Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120.

numero = int(input("Digite um número: "))
if (numero == 0 or numero == 1):
    print("Não foi possivel calcular o fatorial!")
else:
    fatorial = 1
    for i in range(2,numero + 1):
        fatorial*= i

print("O resultado do fatorial de", numero, "é:", fatorial)




##Questão 3
Escreva um programa que peça ao usuário para digitar uma sequência de números inteiros terminada por 0 e calcule a soma de todos os números digitados.

lista = []

sequencia = int(input("Quantos números voce deseja digitar? "))

for i in range(sequencia):
    while True:
        numero = input("Digite um numero terminado em  0: ")
        if numero.endswith('0'):
            lista.append(int(numero))
            break
        else:
            print("O número deve terminar em 0. Tente novamente.")

print("A soma dos números é:", sum(lista))




##Questão 4
Escreva um programa que leia um número inteiro positivo e verifique se ele é um número primo. Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.  

numero = int(input("Digite um número: "))

if numero <= 1:
    print(f"{numero} não é um número primo.")
else:
    primo = True 
    for i in range(2, numero):
        if numero % i == 0:
            primo = False  
            break

    if primo:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")

    
##Questão 5
Escreva um programa que imprima a sequência de Fibonacci até o décimo termo. A sequência de Fibonacci é formada pela soma dos dois termos anteriores. Exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

a,b = 0,1

for _ in range(8):
    a,b = b,a + b
    print(b)


##Questão 6
Escreva um programa que peça ao usuário para digitar um número inteiro positivo e imprima a tabuada desse número.

number = int(input("Digite um número positivo: "))

resultado = 0
for x in range(10 + 1):
    resultado = number * x
    print(resultado)


##Questão 7
Escreva um programa que peça ao usuário para digitar um número inteiro positivo e calcule a soma dos seus dígitos.

number = input("Digite um número com mais de um digito: ")

soma_digitos = sum(int(digito) for digito in number)

print("A soma dos digitos é:", soma_digitos)


##Questão 8
Escreva um programa que peça ao usuário para digitar uma string e conte quantas vogais ela possui.

string = input("Digite uma palavra: ")
contadorVogal = 0

if string.isalpha():  
    for letra in string.lower():  
        if letra in 'aeiou':  
            contadorVogal += 1  

    print(f"Número de vogais: {contadorVogal}")
else:
    print("Por favor, digite apenas letras.")



##Questão 9
Escreva um programa que leia um número inteiro positivo e imprima o seu inverso. Exemplo: o inverso de 123 é 321.

number = input("Digite um número com mais de um digito: ")
if len(number) > 1 and number.isdigit():
    sorted_digitos = (sorted(number, reverse = True))
    sorted_number = ''.join(sorted_digitos)

    print(f"Número com dígitos em ordem decrescente: {sorted_number}")
else:
    print("Por favor, digite um número válido com mais de um dígito.")


##Questão 10
Escreva um programa que simule o jogo de adivinhação. O programa deve gerar um número aleatório entre 1 e 100 e pedir ao usuário para adivinhar o número. A cada tentativa, o programa deve informar se o número digitado é maior ou menor que o número gerado. O jogo termina quando o usuário acertar o número.

import random

number = random.randint(0,10)
tentativa = -1
while(tentativa != number):
    tentativa = int(input("Adivinhe o número(0 a 10): "))
    if(tentativa == number):
        print("Número encontrado: Parabens, voce ganhou!")
        print("O número correto era", number)
    else:
        print("tente novamente! ")
        
