name = input('Digite o nome do filme: \n')
yearLaunch = int(input('Digite o ano de lançamento: \n'))
noteMovie = float(input('Digite a nota do filme: \n'))

# 1ª forma
# print('Dados do filme')
# print('===================================')
# print('Nome do filme: ', name)
# print('Ano do lançamento: ', yearLaunch)
# print('Nota do filme: ', noteMovie)


# 2ª forma
# print('Nome do filme: ', name, '\nAno de lançamento: ', yearLaunch, '\nNota do filme: ', noteMovie)

# 3ª forma
print(f"Nome do filme: {name}\n"
      f"Ano de lançamento: {yearLaunch}\n"
      f"Nota do filme: {noteMovie}\n"
      )