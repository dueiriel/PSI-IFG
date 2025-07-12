# database.py
import sqlite3

DB_NAME = "estoque.db"

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados SQLite."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_table():
    """Cria a tabela de produtos se ela não existir."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL DEFAULT 0
    );
    """)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    print("Banco de dados e tabela criados com sucesso.")