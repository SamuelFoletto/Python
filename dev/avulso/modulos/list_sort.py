lista = [
    {'nome' : 'Samuel', 'sobrenome' : 'Foletto'},
    {'nome': 'Fernanda', 'sobrenome' : 'Pessoa'}
]


lista.sort(key=lambda item: item['nome'])
print(lista)