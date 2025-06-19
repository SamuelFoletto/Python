pessoa = {
    'nome' : 'Samuel',
    'sobrenome' : 'Foletto'
}

# a, b = pessoa.values()
#
# print(a, b)

dados_pessoa = {
    'idade' : 25,
    'altura' : 1.82
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)