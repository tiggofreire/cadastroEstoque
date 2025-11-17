import tkinter as tk
from tkinter import messagebox
from banco import inserir_produto, listar_produtos, excluir_produto

def janela_principal():

    def cadastrar():
        nome = campo_nome.get()
        categoria = campo_cat.get()
        preco = float(campo_preco.get())
        quantidade = int(campo_qtd.get())

        inserir_produto(nome, categoria, preco, quantidade)
        messagebox.showinfo("OK", "Produto cadastrado!")
    
    def mostrar():
        dados = listar_produtos()
        texto.delete("1.0", tk.END)
        for d in dados:
            texto.insert(tk.END, f"{d}\n")

    def deletar():
        idp = int(campo_excluir.get())
        excluir_produto(idp)
        messagebox.showinfo("OK", "Produto excluído!")

    janela = tk.Tk()
    janela.title("Sistema de Estoque")

    tk.Label(janela, text="Nome:").grid(row=0, column=0)
    campo_nome = tk.Entry(janela)
    campo_nome.grid(row=0, column=1)

    tk.Label(janela, text="Categoria:").grid(row=1, column=0)
    campo_cat = tk.Entry(janela)
    campo_cat.grid(row=1, column=1)

    tk.Label(janela, text="Preço:").grid(row=2, column=0)
    campo_preco = tk.Entry(janela)
    campo_preco.grid(row=2, column=1)

    tk.Label(janela, text="Quantidade:").grid(row=3, column=0)
    campo_qtd = tk.Entry(janela)
    campo_qtd.grid(row=3, column=1)

    tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=4, column=0, columnspan=2)

    tk.Label(janela, text="ID para excluir:").grid(row=5, column=0)
    campo_excluir = tk.Entry(janela)
    campo_excluir.grid(row=5, column=1)
    tk.Button(janela, text="Excluir", command=deletar).grid(row=6, column=0, columnspan=2)

    tk.Button(janela, text="Mostrar produtos", command=mostrar).grid(row=7, column=0, columnspan=2)

    texto = tk.Text(janela, width=50, height=10)
    texto.grid(row=8, column=0, columnspan=2)

    janela.mainloop()
