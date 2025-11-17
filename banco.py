import sqlite3

def conectar():
    return sqlite3.connect("estoque.db")

def criar_tabela():
    con = conectar()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT,
            preco REAL,
            quantidade INTEGER
        );
    """)

    con.commit()
    con.close()

def inserir_produto(nome, categoria, preco, quantidade):
    con = conectar()
    cur = con.cursor()

    cur.execute("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (?, ?, ?, ?)",
                (nome, categoria, preco, quantidade))

    con.commit()
    con.close()

def listar_produtos():
    con = conectar()
    cur = con.cursor()

    cur.execute("SELECT * FROM produtos")
    dados = cur.fetchall()

    con.close()
    return dados

def excluir_produto(id_produto):
    con = conectar()
    cur = con.cursor()

    cur.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))

    con.commit()
    con.close()
