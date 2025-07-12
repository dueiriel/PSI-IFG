# main.py
from service import ProdutoService
from database import create_table

class MainApp:
    def __init__(self):
        self.produto_service = ProdutoService()
        create_table() # Garante que a tabela exista ao iniciar

    def exibir_menu(self):
        print("\n--- Sistema de Controle de Estoque (SCE) ---")
        print("1. Adicionar Produto")
        print("2. Listar Todos os Produtos")
        print("3. Registrar Entrada de Estoque")
        print("4. Registrar Saída de Estoque")
        print("5. Remover Produto")
        print("6. Sair")
        return input("Escolha uma opção: ")

    def main_loop(self):
        while True:
            opcao = self.exibir_menu()
            try:
                if opcao == '1':
                    self.adicionar_produto()
                elif opcao == '2':
                    self.listar_produtos()
                elif opcao == '3':
                    self.registrar_entrada()
                elif opcao == '4':
                    self.registrar_saida()
                elif opcao == '5':
                    self.remover_produto()
                elif opcao == '6':
                    print("Saindo do sistema. Até logo!")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError as e:
                print(f"Erro: {e}")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {e}")

    def adicionar_produto(self):
        print("\n-- Adicionar Novo Produto --")
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço (ex: 49.99): "))
        quantidade = int(input("Quantidade Inicial: "))
        self.produto_service.adicionar_produto(nome, descricao, preco, quantidade)
        print("Produto adicionado com sucesso!")

    def listar_produtos(self):
        print("\n-- Lista de Produtos --")
        produtos = self.produto_service.listar_todos_produtos()
        if not produtos:
            print("Nenhum produto cadastrado.")
            return
        
        for p in produtos:
            print(f"ID: {p.id_produto} | Nome: {p.nome} | Preço: R${p.preco:.2f} | Qtd: {p.quantidade}")

    def registrar_entrada(self):
        print("\n-- Registrar Entrada de Estoque --")
        self.listar_produtos()
        id_produto = int(input("Digite o ID do produto para dar entrada: "))
        quantidade = int(input("Digite a quantidade de entrada: "))
        self.produto_service.registrar_entrada(id_produto, quantidade)
        print("Entrada registrada com sucesso!")
        
    def registrar_saida(self):
        print("\n-- Registrar Saída de Estoque --")
        self.listar_produtos()
        id_produto = int(input("Digite o ID do produto para dar saída: "))
        quantidade = int(input("Digite a quantidade de saída: "))
        self.produto_service.registrar_saida(id_produto, quantidade)
        print("Saída registrada com sucesso!")

    def remover_produto(self):
        print("\n-- Remover Produto --")
        self.listar_produtos()
        id_produto = int(input("Digite o ID do produto que deseja remover: "))
        # Adicionar uma confirmação
        confirmacao = input(f"Tem certeza que deseja remover o produto ID {id_produto}? (s/n): ").lower()
        if confirmacao == 's':
            self.produto_service.remover_produto(id_produto)
            print("Produto removido com sucesso!")
        else:
            print("Operação cancelada.")


if __name__ == "__main__":
    app = MainApp()
    app.main_loop()