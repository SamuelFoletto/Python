filmsList = ['Inception', 'The Shawshank Redemption', 'The Dark Knight', 'Pulp Fiction', 'Interestellar']

# Tamanho da lista
print(len(filmsList))

# Recupera index pelo nome
print(filmsList.index('Pulp Fiction'))

# Adiciona item ao final
filmsList.append('The lord of the Rings')
print(filmsList)

# Ordena a lista
filmsList.sort()
print(filmsList)

# copia itens para outra lista
filmsCopy = filmsList.copy()


# Remove todos os itens da lista
filmsList.clear()
print(filmsList)