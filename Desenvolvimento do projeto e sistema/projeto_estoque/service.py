# service.py
from model import Produto
from dao import ProdutoDAO

class ProdutoService:
    """Camada de serviço com as regras de negócio para produtos."""
    def __init__(self):
        self.produto_dao = ProdutoDAO()

    def adicionar_produto(self, nome: str, descricao: str, preco: float, quantidade: int) -> Produto:
        """Adiciona um novo produto."""
        if preco <= 0 or quantidade < 0:
            raise ValueError("Preço e quantidade devem ser valores positivos.")
        if not nome:
            raise ValueError("O nome do produto não pode ser vazio.")
        
        produto = Produto(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade)
        return self.produto_dao.salvar(produto)

    def listar_todos_produtos(self) -> list[Produto]:
        """Retorna todos os produtos."""
        return self.produto_dao.listar_todos()

    def remover_produto(self, id_produto: int):
        """Remove um produto pelo ID."""
        if not self.produto_dao.buscar_por_id(id_produto):
            raise ValueError("Produto não encontrado.")
        self.produto_dao.deletar(id_produto)

    def registrar_entrada(self, id_produto: int, quantidade: int):
        """Registra a entrada de itens no estoque."""
        if quantidade <= 0:
            raise ValueError("A quantidade de entrada deve ser maior que zero.")
        
        produto = self.produto_dao.buscar_por_id(id_produto)
        if not produto:
            raise ValueError("Produto não encontrado.")
            
        produto.quantidade += quantidade
        self.produto_dao.atualizar(produto)

    def registrar_saida(self, id_produto: int, quantidade: int):
        """Registra a saída de itens do estoque."""
        if quantidade <= 0:
            raise ValueError("A quantidade de saída deve ser maior que zero.")

        produto = self.produto_dao.buscar_por_id(id_produto)
        if not produto:
            raise ValueError("Produto não encontrado.")
        
        if produto.quantidade < quantidade:
            raise ValueError("Estoque insuficiente para a saída.")
            
        produto.quantidade -= quantidade
        self.produto_dao.atualizar(produto)