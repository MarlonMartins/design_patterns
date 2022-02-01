from impostos import ICMS, ICPP, IKCV, ISS


class CalculadorDeImpostos(object):
    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


if __name__ == "__main__":
    from orcamento import Item, Orcamento

    calculador = CalculadorDeImpostos()

    orcamento = Orcamento()
    orcamento.adiciona_item(Item("ITEM - 1", 50))
    orcamento.adiciona_item(Item("ITEM - 2", 200))
    orcamento.adiciona_item(Item("ITEM - 3", 250))

    print("ISS e ICMS")
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print("ICPP e IKVC")
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())
