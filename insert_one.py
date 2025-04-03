import mysql.connector
conexao_db = mysql.connector.connect(user='root',
                                     password='ceub123456',
                                     host='127.0.0.1',
                                     database='db_empresa')
cursor_db = conexao_db.cursor()
sql = '''INSERT INTO tb_funcionario(id, nome, salario)
        VALUES ('Bernardo', 10000)'''
cursor_db.execute(sql)
conexao_db.commit()
cursor_db.close()
conexao_db.close()
print("\nConexão fechada.")