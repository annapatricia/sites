import pyodbc
import pandas as pd

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

cursor = conexao.cursor()

try:
    # Corrigindo a consulta SQL
    tabela = pd.read_sql('SELECT * FROM Vendas', conexao)
    tabela
except Exception as e:
    print("Erro na execução da consulta SQL:", e)

# Fechando a conexão
conexao.close()