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

comando="""INSERT INTO Vendas(id_venda,cliente,produto,data_venda,preco,quantidade)
VALUES
     (2,'Anna Patricia genia','PC','2024-02-15',8000,1)"""

cursor.execute(comando)
cursor.commit()