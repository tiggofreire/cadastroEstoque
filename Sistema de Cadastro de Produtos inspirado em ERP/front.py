import tkinter as tk
from tkinter import messagebox, simpledialog
from banco import (
    inserir_produto, listar_produtos, excluir_produto,
    atualizar_quantidade, calcular_giro_real
)
import matplotlib.pyplot as plt

def janela_principal():

    def cadastrar():
        nome = campo_nome.get()
        categoria = campo_cat.get()
        try:
            preco = float(campo_preco.get())
            quantidade = int(campo_qtd.get())
        except ValueError:
            messagebox.showerror("Erro", "Preço e quantidade devem ser números válidos")
            return
        if not nome:
            messagebox.showerror("Erro", "O nome do produto é obrigatório")
            return
        inserir_produto(nome, categoria, preco, quantidade)
        messagebox.showinfo("OK", f"Produto '{nome}' cadastrado!")
        mostrar()
        limpar_campos()

    def deletar():
        try:
            idp = int(campo_excluir.get())
        except ValueError:
            messagebox.showerror("Erro", "ID inválido")
            return
        excluir_produto(idp)
        messagebox.showinfo("OK", f"Produto ID {idp} excluído!")
        mostrar()
        campo_excluir.delete(0, tk.END)

    def entrada_estoque():
        try:
            idp = int(simpledialog.askstring("Entrada de Estoque", "ID do produto:"))
            qtde = int(simpledialog.askstring("Entrada de Estoque", "Quantidade a adicionar:"))
            if qtde <= 0:
                raise ValueError
        except (TypeError, ValueError):
            messagebox.showerror("Erro", "ID e quantidade devem ser números positivos válidos")
            return
        sucesso = atualizar_quantidade(idp, qtde)
        if sucesso:
            messagebox.showinfo("OK", "Estoque atualizado com entrada!")
            mostrar()
        else:
            messagebox.showerror("Erro", "Produto não encontrado")

    def saida_estoque():
        try:
            idp = int(simpledialog.askstring("Saída de Estoque", "ID do produto:"))
            qtde = int(simpledialog.askstring("Saída de Estoque", "Quantidade a retirar:"))
            if qtde <= 0:
                raise ValueError
        except (TypeError, ValueError):
            messagebox.showerror("Erro", "ID e quantidade devem ser números positivos válidos")
            return
        sucesso = atualizar_quantidade(idp, -qtde)
        if sucesso:
            messagebox.showinfo("OK", "Estoque atualizado com saída!")
            mostrar()
        else:
            messagebox.showerror("Erro", "Produto não encontrado")

    def mostrar():
        dados = listar_produtos()
        texto.config(state="normal")
        texto.delete("1.0", tk.END)
        if not dados:
            texto.insert(tk.END, "Nenhum produto cadastrado.\n")
        else:
            for d in dados:
                linha = f"ID:{d[0]} | {d[1]} | {d[2]} | R${d[3]:.2f} | Qtd:{d[4]}\n"
                if d[4] <= 5:
                    texto.insert(tk.END, linha, "baixo")
                else:
                    texto.insert(tk.END, linha)
        texto.tag_config("baixo", foreground="red")
        texto.config(state="disabled")

    def limpar_campos():
        campo_nome.delete(0, tk.END)
        campo_cat.delete(0, tk.END)
        campo_preco.delete(0, tk.END)
        campo_qtd.delete(0, tk.END)

    def abrir_dashboard():
        dados = listar_produtos()
        if not dados:
            messagebox.showinfo("Dashboard", "Nenhum produto cadastrado")
            return

        nomes = [d[1] for d in dados]
        quantidades = [d[4] for d in dados]
        categorias = [d[2] for d in dados]
        custos = [d[3]*d[4] for d in dados]

        plt.figure(figsize=(15,10))

        plt.subplot(2,2,1)
        plt.plot(nomes, quantidades, marker="o", color="blue")
        plt.title("Evolução do Estoque (Simulado)")
        plt.ylabel("Quantidade")
        plt.xticks(rotation=45)

        plt.subplot(2,2,2)
        cat_dict = {}
        for i, c in enumerate(categorias):
            if c not in cat_dict:
                cat_dict[c] = 0
            cat_dict[c] += quantidades[i]
        plt.bar(cat_dict.keys(), cat_dict.values(), color="green")
        plt.title("Comparação de Quantidade por Categoria")
        plt.ylabel("Quantidade")
        plt.xticks(rotation=45)

        plt.subplot(2,1,2)
        custos_ordenados = sorted(zip(nomes, custos), key=lambda x: x[1], reverse=True)
        nomes_abc, custos_abc = zip(*custos_ordenados)
        plt.bar(nomes_abc, custos_abc, color="orange")
        plt.title("Curva ABC de Custos de Estoques")
        plt.ylabel("Custo Total (R$)")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    def relatorios_gerenciais():
        dados = listar_produtos()
        if not dados:
            messagebox.showinfo("Relatórios Gerenciais", "Nenhum produto cadastrado")
            return

        relatorio = ""
        for d in dados:
            id_, nome, cat, preco, qtd = d
            giro_estoque = calcular_giro_real(id_)
            custo_manutencao = preco * qtd * 0.1
            estoque_seguranca = int(0.2 * qtd)
            tempo_medio_reposicao = 5
            relatorio += (
                f"Produto: {nome}\n"
                f" - Giro de Estoque: {giro_estoque:.2f}\n"
                f" - Custo de Manutenção: R${custo_manutencao:.2f}\n"
                f" - Tempo Médio de Reposição: {tempo_medio_reposicao} dias\n"
                f" - Estoque de Segurança: {estoque_seguranca}\n\n"
            )

        janela_rel = tk.Toplevel()
        janela_rel.title("Relatórios Gerenciais")
        text_rel = tk.Text(janela_rel, width=70, height=25)
        text_rel.pack(padx=10, pady=10)
        text_rel.insert(tk.END, relatorio)
        text_rel.config(state="disabled")

    janela = tk.Tk()
    janela.title("Mini-ERP de Estoque")
    janela.geometry("600x650")
    janela.resizable(False, False)

    tk.Label(janela, text="Cadastro de Produto", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, pady=5)
    tk.Label(janela, text="Nome:").grid(row=1, column=0, sticky="e", padx=5)
    campo_nome = tk.Entry(janela, width=30)
    campo_nome.grid(row=1, column=1, padx=5)
    tk.Label(janela, text="Categoria:").grid(row=2, column=0, sticky="e", padx=5)
    campo_cat = tk.Entry(janela, width=30)
    campo_cat.grid(row=2, column=1, padx=5)
    tk.Label(janela, text="Preço:").grid(row=3, column=0, sticky="e", padx=5)
    campo_preco = tk.Entry(janela, width=30)
    campo_preco.grid(row=3, column=1, padx=5)
    tk.Label(janela, text="Quantidade:").grid(row=4, column=0, sticky="e", padx=5)
    campo_qtd = tk.Entry(janela, width=30)
    campo_qtd.grid(row=4, column=1, padx=5)
    tk.Button(janela, text="Cadastrar Produto", command=cadastrar, width=20).grid(row=5, column=0, columnspan=2, pady=10)

    tk.Label(janela, text="Excluir Produto", font=("Arial", 12, "bold")).grid(row=6, column=0, columnspan=2, pady=5)
    tk.Label(janela, text="ID do produto:").grid(row=7, column=0, sticky="e", padx=5)
    campo_excluir = tk.Entry(janela, width=30)
    campo_excluir.grid(row=7, column=1, padx=5)
    tk.Button(janela, text="Excluir Produto", command=deletar, width=20).grid(row=8, column=0, columnspan=2, pady=10)

    tk.Button(janela, text="Entrada no Estoque", command=entrada_estoque, width=20).grid(row=9, column=0, pady=5)
    tk.Button(janela, text="Saída do Estoque", command=saida_estoque, width=20).grid(row=9, column=1, pady=5)

    tk.Button(janela, text="Abrir Dashboard", command=abrir_dashboard, width=25).grid(row=10, column=0, columnspan=2, pady=5)
    tk.Button(janela, text="Relatórios Gerenciais", command=relatorios_gerenciais, width=25).grid(row=11, column=0, columnspan=2, pady=5)

    tk.Label(janela, text="Relatório de Produtos", font=("Arial", 12, "bold")).grid(row=12, column=0, columnspan=2, pady=5)
    texto = tk.Text(janela, width=70, height=12, state="disabled")
    texto.grid(row=13, column=0, columnspan=2, padx=10, pady=5)
    tk.Button(janela, text="Atualizar Relatório", command=mostrar, width=25).grid(row=14, column=0, columnspan=2, pady=5)

    mostrar()
    janela.mainloop()
