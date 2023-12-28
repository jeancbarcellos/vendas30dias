import pyodbc

def conectar_banco():
    server = 'dbvenasuprimentos.database.windows.net'  # Substitua pelo seu servidor
    database = 'dbvenasuprimentos_backup'  # Substitua pelo nome do seu banco de dados
    username = 'usr_vena'  # Substitua pelo seu usuário
    password = '!@#passFor#@!'  # Substitua pela sua senha
    conexao_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conexao = pyodbc.connect(conexao_string)
    return conexao

def executar_consulta(conexao):
    consulta_sql = """
    SELECT *
    FROM rawdata.totvs_estoque_cmv tec 
    WHERE dataref >= '2023-10-01' AND dataref <= '2023-11-01'
    ORDER BY dataref ASC;
    """
    cursor = conexao.cursor()
    cursor.execute(consulta_sql)
    for linha in cursor:
        print(linha)

def main():
    conexao = conectar_banco()
    executar_consulta(conexao)

if __name__ == "__main__":
    main()
