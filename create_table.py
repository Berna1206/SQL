import mysql.connector
conexao_db = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='127.0.0.1',
                                     database='db_empresa')
cursor_db = conexao_db.cursor()
sql = '''CREATE TABLE IF NOT EXISTS tb_funcionario(
        id SERIAL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        salario INTEGER
)'''
cursor_db.execute(sql)
cursor_db.close()
conexao_db.close()
print("\nConexão fechada.")
