from numbers import Number

from oo.calculadora_procedural import obter_entrada_numerica


class Operacao:
    sinal = ''

    def calcular(self, n: Number, n2: Number) -> Number:
        raise NotImplementedError()


class Subtracao(Operacao):
    sinal = '-'

    def calcular(self, n: Number, n2: Number) -> Number:
        return n - n2


class Calculadora:
    def __init__(self):
        self.operacoes_disponiveis = {}
        self.adicionar(Subtracao())

    def adicionar(self, operacao: Operacao):
        self.operacoes_disponiveis[operacao.sinal] = operacao

    def efetuar_operacao(self):
        n, n2, sinal = self.obter_inputs()

        operacao_escolhida = self.operacoes_disponiveis[sinal]

        return operacao_escolhida.calcular(n, n2)

    def obter_inputs(self):
        raise NotImplementedError()


class CalculadoraInfixa(Calculadora):
    def obter_inputs(self):
        n = obter_entrada_numerica('Digite o primeiro número: ')
        sinais_disponiveis = ', '.join(self.operacoes_disponiveis.keys())
        sinal = input(f'Digite o sinal da operação ({sinais_disponiveis}): ')
        n2 = obter_entrada_numerica('Digite o segundo número: ')
        return n, n2, sinal


class CalculadoraPrefixa(Calculadora):
    def obter_inputs(self):
        sinais_disponiveis = ', '.join(self.operacoes_disponiveis.keys())
        sinal = input(f'Digite o sinal da operação ({sinais_disponiveis}): ')
        n = obter_entrada_numerica('Digite o primeiro número: ')
        n2 = obter_entrada_numerica('Digite o segundo número: ')
        return n, n2, sinal
