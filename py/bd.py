import sqlite3;


conexao = sqlite3.connect("meu_banco.db")

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(conexao, cursor):
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
    conexao.commit()

def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?,?);', data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE clientes SET  nome=?, email=? WHERE id=?;', data)
    conexao.commit()

def remove_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?;', data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?,?);', dados)
    conexao.commit()

def recuperar_cliente(cursor, id):
    cursor.execute('SELECT nome FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()
    

def listar_clientes(cursor):
    return cursor.execute("SELECT nome, email FROM clientes ORDER BY nome desc;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

# cliente = recuperar_cliente(cursor, 3)
# print(dict(cliente))

# atualizar_registro(conexao, cursor, 'Samuel Foletto', 'sfoletto@gmail.com', 1)

# inserir_registro(conexao, cursor, 'Fernanda Pessoa', 'fernandasp@gmail.com')

# remove_registro(conexao, cursor, 2)

# dados = [
    # ('Fernanda Pessoa', 'fernandasp@gmail.com'), 
    # ('Samuel Comercial', 'samuel.foletto@gmail.com')
    # ]

# inserir_muitos(conexao,cursor, dados)

