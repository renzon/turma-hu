def _hanoi_recursivo(discos, origem, destino, aux):
    if discos == 1:
        print(f'{discos}: {origem} -> {destino}')
    else:
        _hanoi_recursivo(discos-1, origem, aux, destino)
        print(f'{discos}: {origem} -> {destino}')
        _hanoi_recursivo(discos-1, aux, destino, origem)


def hanoi(discos: int):
    _hanoi_recursivo(discos, origem='A', destino='C', aux='B')


if __name__ == '__main__':
    hanoi(3)
