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

#STRING
# %%
'''
11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
'''
str1 = input('Digite o valor que deseja converter para maiúsculo: ')

r = f'Valor em maiúscula: {str1.upper()}'

print(r)
# %%
'''
12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
'''
str1 = input('Digite seu nome completo: ')

r = f'Valor em minuscula: {str1.lower()}'

print(r)
# %%
'''
13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
'''
str1 = input('Digite uma frase: ')

r = f'Valor sem espaços no inicio e fim: {str1.strip()}'

print(r)
# %%
'''
14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
'''
str1 = input('Digite uma data: ')
lista = str1.split('/')

r = f'Dia: {lista[0]} \nMês: {lista[1]} \nAno: {lista[2]}'

print(r)
# %%
'''
15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
'''

str1 = input('Digite uma palavra: \n')
str2 = input('Digite otra palavra: \n')

r = f'{str1 + str2}'

print(r)

#BOOL
# %%
'''
16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
'''
v1 = True
v2 = False

print(f'and {v1 and v2}')
print(f'or {v1 or v2}')
print(f'invertendo valor {not v1}')
print(f'igualdade {5 == 5}')
print(f'diferença {4 != 5}')

# %%
