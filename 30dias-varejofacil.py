import pyodbc

def conectar_banco():
    server = 'dbvenasuprimentos.database.windows.net'  # Substitua pelo seu servidor
    database = 'dbvenasuprimentos'  # Substitua pelo nome do seu banco de dados
    username = 'usr_vena'  # Substitua pelo seu usuário
    password = '!@#passFor#@!'  # Substitua pela sua senha
    conexao_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
    conexao = pyodbc.connect(conexao_string)
    return conexao

def criar_tabela_e_inserir_dados(conexao): #cria nova tabela em dmCobertura com os últimos 30 dias de vendas
    cursor = conexao.cursor()
    cursor.execute("""
    IF NOT EXISTS (SELECT * FROM sys.tables WHERE name = 'vendas30d_vf' AND type = 'U')
        SELECT CodLoja, CodProd, Saidas, IdCp, DtRef 
        INTO dmCobertura.vendas30d_vf
        FROM rawdata.posicaoestoque_vf pv 
        WHERE dtref >= '2023-11-27' AND dtref <= '2023-12-27'
        ORDER BY dtref ASC;
    """)
    conexao.commit()

def main():
    conexao = conectar_banco()
    criar_tabela_e_inserir_dados(conexao)

if __name__ == "__main__":
    main()
