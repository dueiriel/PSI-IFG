# dao.py
from model import Produto
from database import get_db_connection

class ProdutoDAO:
    """DAO para a entidade Produto, utilizando SQLite."""

    def salvar(self, produto: Produto) -> Produto:
        """Salva um novo produto no banco de dados."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (?, ?, ?, ?)",
            (produto.nome, produto.descricao, produto.preco, produto.quantidade)
        )
        produto.id_produto = cursor.lastrowid
        conn.commit()
        conn.close()
        return produto

    def atualizar(self, produto: Produto):
        """Atualiza os dados de um produto existente."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE produtos SET nome = ?, descricao = ?, preco = ?, quantidade = ? WHERE id = ?",
            (produto.nome, produto.descricao, produto.preco, produto.quantidade, produto.id_produto)
        )
        conn.commit()
        conn.close()

    def deletar(self, id_produto: int):
        """Deleta um produto do banco de dados pelo seu ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
        conn.commit()
        conn.close()

    def buscar_por_id(self, id_produto: int) -> Produto | None:
        """Busca um produto pelo seu ID."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos WHERE id = ?", (id_produto,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Produto(id_produto=row['id'], nome=row['nome'], descricao=row['descricao'],
                           preco=row['preco'], quantidade=row['quantidade'])
        return None

    def listar_todos(self) -> list[Produto]:
        """Retorna uma lista de todos os produtos cadastrados."""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos ORDER BY nome")
        rows = cursor.fetchall()
        conn.close()
        produtos = []
        for row in rows:
            produtos.append(
                Produto(id_produto=row['id'], nome=row['nome'], descricao=row['descricao'],
                        preco=row['preco'], quantidade=row['quantidade'])
            )
        return produtos