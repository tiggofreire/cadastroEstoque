# Mini-ERP de Estoque

Este é um **mini-ERP de estoque** desenvolvido em Python com interface gráfica em Tkinter e banco de dados SQLite.  
Ele simula funcionalidades de um sistema ERP real, permitindo gerenciar produtos, controlar estoque e gerar relatórios gerenciais e dashboards.

---

## Funcionalidades

O sistema possui as seguintes funcionalidades:

1. **Cadastro de produtos**
   - Informar: nome, categoria, preço e quantidade inicial.
   - Armazenar os dados no banco SQLite (`estoque.db`).

2. **Edição de produtos**
   - Editar qualquer campo de um produto existente pelo ID.

3. **Exclusão de produtos**
   - Remover produtos cadastrados pelo ID.

4. **Movimentação de estoque**
   - Entrada: adicionar unidades ao estoque existente.
   - Saída: remover unidades do estoque existente.

5. **Relatório de produtos**
   - Lista todos os produtos cadastrados.
   - Destaca produtos com **estoque baixo** (quantidade ≤ 5).

6. **Relatórios gerenciais**
   - Cálculo de giro de estoque real.
   - Estimativa de custo de manutenção.
   - Estoque de segurança.
   - Tempo médio de reposição.

7. **Dashboard com gráficos**
   - Evolução do estoque (simulado).
   - Comparação de quantidade por categoria.
   - Curva ABC de custos de estoques.

---

## Estrutura de arquivos

- `estoque.py` → Arquivo principal que inicia o sistema.  
- `front.py` → Interface gráfica em Tkinter.  
- `banco.py` → Funções para conexão e manipulação do banco de dados SQLite.  
- `estoque.db` → Banco de dados SQLite (gerado automaticamente ao rodar o sistema).  

---

## Pré-requisitos

- Python 3.x instalado  
- Biblioteca `matplotlib` instalada  

Para instalar o `matplotlib`, rode:

```bash pip install matplotlib

## ▶️ Como Rodar

1. Abra o **VS Code** ou outro terminal na pasta do projeto.

2. Verifique se o Python está instalado e acessível no terminal:

```bash
python --version

    Execute o sistema:

python estoque.py
