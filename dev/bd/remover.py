import sqlite3

conexao = sqlite3.connect('titulo.db')

cursor = conexao.cursor()


# remove dados
id = (1,2)

cursor.execute(
    """
        DELETE FROM filmes
        WHERE id in (?, ?)    
    """, 
    id
)

conexao.commit()

print('Dados removidos com sucesso!')