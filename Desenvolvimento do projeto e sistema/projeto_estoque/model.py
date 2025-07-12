# model.py
from dataclasses import dataclass

@dataclass
class Produto:
    """Classe que representa um produto no sistema."""
    id_produto: int = 0
    nome: str = ""
    descricao: str = ""
    preco: float = 0.0
    quantidade: int = 0