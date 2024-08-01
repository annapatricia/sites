import pyodbc
#server é onde esta nosso banco de dados e esta dentro do computdador 

dados_conexao= (
    "Driver={SQL Server};"
    "Server =projeto;"
    "Database=PythonSQL;"
)
conexao=pyodbc.connect(dados_conexao)
print("conexao bem sucedida")