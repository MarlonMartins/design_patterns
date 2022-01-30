from descontos import (
    DescontoPorCincoItems,
    DescontoPorMaisDeQuinhentosReais,
    SemDesconto,
)


class CalculadorDeDescontos(object):
    def calcula(self, orcamento):
        desconto = DescontoPorCincoItems(
            DescontoPorMaisDeQuinhentosReais(SemDesconto())
        ).calcula(orcamento)
        return desconto


if __name__ == "__main__":
    from orcamento import Item, Orcamento

    orcamento = Orcamento()
    orcamento.adiciona_item(Item("ITEM - 1", 100))
    orcamento.adiciona_item(Item("ITEM - 2", 50))
    orcamento.adiciona_item(Item("ITEM - 3", 400))
    print(orcamento.valor)

    calculador = CalculadorDeDescontos()
    desconto_calculado = calculador.calcula(orcamento)
    print(f"Desconto de R$ {desconto_calculado:.2f}")
