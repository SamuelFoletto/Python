perguntas = [
    {
        'Pergunta' : 'Quanto é 2 + 2?',
        'Opções' : ['1', '2', '3', '4'],
        'Resposta' : '4'
    },
    {
        'Pergunta' : 'Quanto é 5 * 5?',
        'Opções' : ['25', '55', '10', '45'],
        'Resposta' : '25'
    },
    {
        'Pergunta' : 'Quanto é 10 / 2?',
        'Opções' : ['2', '5', '10', '0'],
        'Resposta' : '5'
    }
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i}', opcao)

    escolha = input('Escolha uma opção: \n')
    if escolha == pergunta['Resposta']:
        print('Resposta correta!')
    else:
        print('Resposta incorreta!')

