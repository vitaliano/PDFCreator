import sqlite3

conn = sqlite3.connect("dados.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS especificacoes (
  id INTEGER PRIMARY KEY,
  janela_id TEXT,
  nome_loja TEXT,
  texto_1 TEXT,
  texto_2 TEXT,
  texto_3 TEXT,
  texto_4 TEXT,
  imagem_path TEXT,
  logo_path TEXT
)
""")

for i in range(1, 17):
    cursor.execute("""
    INSERT INTO especificacoes (
      janela_id, nome_loja, texto_1, texto_2, texto_3, texto_4,
      imagem_path, logo_path
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        f"janela_{i}",
        f"Loja {i}",
        "Oferta especial",
        "Desconto de até 30%",
        "Válido até 31/10",
        "Consulte condições",
        "assets/imagens/imagem_padrao.png",
        "assets/logos/logo_padrao.png"
    ))

conn.commit()
conn.close()