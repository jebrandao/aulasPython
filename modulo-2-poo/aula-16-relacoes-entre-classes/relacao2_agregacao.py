"""Agregação: o carrinho contém produtos que existem independentemente dele."""


class Produto:
    def __init__(self, nome: str, preco: float) -> None:
        self.nome = nome
        self.preco = preco


class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.produtos: list[Produto] = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.produtos.append(produto)  # recebe um objeto completo, criado fora

    def total(self) -> float:
        return sum(produto.preco for produto in self.produtos)

    def listar_produtos(self) -> None:
        if not self.produtos:
            print("Seu carrinho de compras existe, mas está vazio!")
            return
        print("Produtos no seu carrinho de compras:")
        for produto in self.produtos:
            print(f" - {produto.nome}: R$ {produto.preco:,.2f}")
        print(f"Total: R$ {self.total():,.2f}")


if __name__ == "__main__":
    carrinho = CarrinhoDeCompras()
    carrinho.listar_produtos()  # vazio

    produto1 = Produto("Celular iPhone", 5000)
    produto2 = Produto("Notebook Dell", 3800)

    carrinho.adicionar_produto(produto1)
    carrinho.adicionar_produto(produto2)
    carrinho.listar_produtos()

    # Os produtos continuam existindo mesmo que o carrinho seja descartado:
    del carrinho
    print(f"\nO produto continua existindo: {produto1.nome}")
