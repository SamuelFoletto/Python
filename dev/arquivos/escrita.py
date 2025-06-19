name = input('Digite o nome do aluno:\n')

"""
Arquivos - Modos de Operação:

1 - Modo W - write (escrita)
2 - Modo A - append (adiciona ao final)
3 - Modo R - read (apenas leitura)
"""


# Primeira implementação

# file = open('dados/names.txt', 'a', encoding='utf-8')

# file.write(f'{name}\n')

# file.close()


with open('dados/names.txt', 'a', encoding='utf-8') as file:
    file.write(f'{name}\n')
