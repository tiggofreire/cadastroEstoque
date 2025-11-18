import sqlite3
from datetime import datetime

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

    cur.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER,
            tipo TEXT,
            quantidade INTEGER,
            data TEXT,
            FOREIGN KEY(produto_id) REFERENCES produtos(id)
        );
    """)

    con.commit()
    con.close()

def inserir_produto(nome, categoria, preco, quantidade):
    con = conectar()
    cur = con.cursor()

    cur.execute("INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (?, ?, ?, ?)",
                (nome, categoria, preco, quantidade))
    produto_id = cur.lastrowid

    cur.execute("INSERT INTO movimentacoes (produto_id, tipo, quantidade, data) VALUES (?, 'entrada', ?, ?)",
                (produto_id, quantidade, datetime.now().isoformat()))

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
    cur.execute("DELETE FROM movimentacoes WHERE produto_id = ?", (id_produto,))
    con.commit()
    con.close()

def atualizar_quantidade(produto_id, quantidade):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT quantidade FROM produtos WHERE id = ?", (produto_id,))
    res = cur.fetchone()
    if res is None:
        con.close()
        return False
    nova_qtd = res[0] + quantidade
    if nova_qtd < 0:
        con.close()
        return False
    cur.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_qtd, produto_id))
    tipo = "entrada" if quantidade > 0 else "saida"
    cur.execute("INSERT INTO movimentacoes (produto_id, tipo, quantidade, data) VALUES (?, ?, ?, ?)",
                (produto_id, tipo, abs(quantidade), datetime.now().isoformat()))
    con.commit()
    con.close()
    return True

def calcular_giro_real(produto_id):
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT SUM(quantidade) FROM movimentacoes WHERE produto_id = ? AND tipo='saida'", (produto_id,))
    total_saida = cur.fetchone()[0] or 0
    cur.execute("SELECT quantidade FROM produtos WHERE id = ?", (produto_id,))
    estoque_atual = cur.fetchone()[0]
    estoque_medio = estoque_atual 
    con.close()
    if estoque_medio == 0:
        return 0
    return total_saida / estoque_medio
