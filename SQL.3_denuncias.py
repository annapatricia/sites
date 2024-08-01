import pyodbc

dados_conexao = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost\\SQLEXPRESS;"
    "Database=PythonSQL;"
    "Trusted_Connection=yes;"
)

try:
    conexao = pyodbc.connect(dados_conexao)
    print("Conexão bem-sucedida!")
except Exception as e:
    print("Erro na conexão:", e)


cursor=conexao.cursor()  

comando=""" INSERT INTO denuncias (id,nome, email, mensagem)
VALUES 
     (3,'Anna', 'annapamanrique@gmail.com', 'minha denuncia é sobre uma loja de eletrodomesticos')"""

cursor.execute(comando)
cursor.commit()


