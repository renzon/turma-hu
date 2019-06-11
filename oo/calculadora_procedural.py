def obter_entrada_numerica(msg):
    while True:
        try:
            n = float(input(msg))
        except ValueError as e:
            print('Valor deve ser um número, tente novamente')
        else:
            return n


def efetuar_operacao():
    """
    Função que efetua operações simples de adição e subtração
    :return: float com resultado da operação
    """
    # Inputs
    n_1 = obter_entrada_numerica('Digite o primeiro número: ')

    sinal = input('Digite o sinal da operação (+ ou -): ')

    n_2 = obter_entrada_numerica('Digite o segundo número: ')

    # Processamento
    if sinal == '+':
        resultado = n_1 + n_2
    elif sinal == '-':
        resultado = n_1 - n_2
    # Apresentação
    return resultado


if __name__ == '__main__':
    print(efetuar_operacao())
