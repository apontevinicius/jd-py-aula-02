# INT
# %%
'''
1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número número: '))

r = f'O resultado da soma dos dois números é: {n1 + n2}'

print(r)
# %%
'''
2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
'''
RESTO = 5
n1 = int(input('Digite um número: '))

r = f'O resto da divisão de {n1} por {RESTO} é de {n1 % RESTO}'

print(r)
# %%
'''
3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número número: '))

r = f'O resultado da multiplicação dos dois número é: {n1 + n2}'

print(r)
# %%
'''
4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número número: '))

r = f'O resultado da divisão inteira dos dois número é: {n1 // n2}'

print(r)
# %%
'''
5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
'''
n1 = int(input('Digite um número: '))
QUADRADO = 2

r = f'O resultado do quadrado do número digitado é de: {n1 ** QUADRADO}'

print(r)

#FLOAT
# %%
'''
6. Escreva um programa que receba dois números flutuantes e realize sua adição.
'''
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número número: '))

r = f'O resultado da soma dos dois números é: {n1 + n2}'

print(r)
# %%
'''
7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
'''
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número número: '))

r = f'O resultado da média dos dois número é: {(n1 + n2) / 2}'

print(r)
# %%
'''
8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
'''
n1 = float(input('Base: '))
n2 = float(input('Expoente: '))

r = f'O resultado da potenciação é: {(n1 ** n2)}'

print(r)
# %%
'''
9. Faça um programa que converta a temperatura de Celsius para Fahrenheit
'''

n1 = float(input('Digite o valor em Celsius: '))

r = f'O valor digitado em Celsius convertido em F é igual a: {n1 * 9 / 5 + 32}'

print(r)
# %%
'''
10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
'''
n1 = float(input('Digite o raio do circulo: '))

r = f'A área do circulo é de: {(n1 / 3.14) ** 0.5}'

print(r)
# %%
