import sqlite3

conexao = sqlite3.connect("meu_banco.db")

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', ('Teste 2', 'teste1@gmail.com'))
    conexao.commit()
except Exception as exec:
    print(f"Ops! Algo deu errado! {exec}")
    conexao.rollback()