# Operadores in e not in
'''nome = 'Otávio'
print(nome[2])
print('á' in nome)
print('zero' in nome)
print('-'*10)
print('vio' not in nome)
print('zero' in nome)'''

nome = input('Digite seu nome: ').upper([1])

encontrar = input('O que você deseja encontar?: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')