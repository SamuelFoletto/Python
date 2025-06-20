import sqlite3
# conectando com o database
conexao = sqlite3.connect('titulo.db')
# criando o cursor
cursor = conexao.cursor()
# criando a tabela
cursor.execute(
    """
        CREATE TABLE filmes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            ano INTEGER NOT NULL,
            nota REAL NOT NULL
        );
    """
)


# fecha conexao

conexao.close()
print('Tabela foi criada')