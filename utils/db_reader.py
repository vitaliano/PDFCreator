import sqlite3

def carregar_dados(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM especificacoes")
    colunas = [desc[0] for desc in cursor.description]
    dados = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
    conn.close()
    return dados