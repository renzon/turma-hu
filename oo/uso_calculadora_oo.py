from oo.calculadora_oo import Calculadora, Operacao


class Multiplicacao(Operacao):
    sinal = '*'

    def calcular(self, n, n2):
        return n * n2


mult = Multiplicacao()
calculadora = Calculadora()
calculadora.adicionar(mult)
print(calculadora.efetuar_operacao())
