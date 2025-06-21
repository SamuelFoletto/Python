from conexao_post import conn

cursor_obj = conn.cursor()

games = [
    ('Star Wars', 2023, 9.0),
    ('League of Legends', 2013, 10.0)
]

for game in games:
    cursor_obj.execute(
        """
        INSERT INTO games(name, year, score)
        VALUES(%s, %s, %s)
        """, game
    )


conn.commit()

print('dados inseridos com sucesso"')

conn.close
