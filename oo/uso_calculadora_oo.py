from oo.calculadora_oo import CalculadoraInfixa, Operacao, CalculadoraPrefixa


class Multiplicacao(Operacao):
    sinal = '*'

    def calcular(self, n, n2):
        return n * n2


mult = Multiplicacao()
calculadora = CalculadoraPrefixa()
calculadora.adicionar(mult)
print(calculadora.efetuar_operacao())
