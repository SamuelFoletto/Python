import sqlite3

conexao = sqlite3.connect('titulo.db')

cursor = conexao.cursor()

cursor.execute(
    """
        INSERT INTO filmes(nome, ano,nota)
        VALUES('Sonic', 2020, 8);
    """
)

conexao.commit()
conexao.close()
print('Dados adicionados com sucesso!')