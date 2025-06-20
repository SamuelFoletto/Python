import sqlite3

conexao = sqlite3.connect('titulo.db')

cursor = conexao.cursor()

# Lê os dados
dados = cursor.execute("SELECT * FROM filmes")

print(dados.fetchall())