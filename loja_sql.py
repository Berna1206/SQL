import sqlite3
conn = sqlite3.connect("loja.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER,
    categoria TEXT
    )
''')
conn.commit()

produtos = [
    ("Notebook", 3500.00, 10, "Eletrônicos"),
    ("Smartphone", 2500.00, 20, "Eletrônicos"),
    ("Cadeira Gamer", 1200.00, 5, "Móveis"),
    ("Teclado Mecânico", 450.00, 15, "Acessórios")
]
cursor.executemany('''
    INSERT INTO produtos (nome, preco, estoque, categoria)
    VALUES (?, ?, ?, ?)
''', produtos)
conn.commit()

cursor.execute("SELECT * FROM produtos")
registros = cursor.fetchall()

if not registros:
    print("Tabela vazia.")
else:
    print("\nRegistros:")
    for registro in registros:
        print(registro)
conn.close()