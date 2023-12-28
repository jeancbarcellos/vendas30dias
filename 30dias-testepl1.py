import pyodbc

def conectar_banco():
    server = 'dbvenasuprimentos.database.windows.net'  # Substitua pelo seu servidor
    database = 'dbvenasuprimentos_backup'  # Substitua pelo nome do seu banco de dados
    username = 'usr_vena'  # Substitua pelo seu usuário
    password = '!@#passFor#@!'  # Substitua pela sua senha
    conexao_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conexao = pyodbc.connect(conexao_string)
    return conexao

def criar_tabela_e_inserir_dados(conexao):
    cursor = conexao.cursor()
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'diasteste1' AND type = 'U')
        SELECT *
        INTO rawdata.diasteste1
        FROM rawdata.totvs_estoque_cmv tec 
        WHERE dataref >= '2023-10-01' AND dataref <= '2023-11-01'
        ORDER BY dataref ASC;
    """)
    conexao.commit()

def main():
    conexao = conectar_banco()
    criar_tabela_e_inserir_dados(conexao)

if __name__ == "__main__":
    main()
