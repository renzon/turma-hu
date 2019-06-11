class Coleira:
    def indentificar(self):
        raise NotImplementedError()


class ColeiraEletronica(Coleira):
    def indentificar(self):
        print('Mandando sinal de GPS')


class ColeiraPadrao(Coleira):
    def indentificar(self):
        print('Rua XPTO')


class Cachoro:
    olhos = 2

    def __init__(self, nome: str = '', pai: 'Cachoro' = None):
        self.coleiras = []
        self.pai = pai
        self.nome = nome

    def colocar_coleira(self, coleira: Coleira):
        self.coleiras.append(coleira)

    def latir(self):
        raise NotImplementedError()

    def retonar_ao_dono(self):
        print(f'Cachorro perdido: {self.nome}')
        for coleira in self.coleiras:
            coleira.indentificar()


class ViraLata(Cachoro):
    def latir(self):
        return f'{self.nome}: Ain Ain'


class CaoDeRacao(Cachoro):
    def latir(self):
        return f'{self.nome}: Au Au'


coleira = ColeiraPadrao()
rex = CaoDeRacao('Rex')
rex.colocar_coleira(coleira)
rex.colocar_coleira(ColeiraEletronica())

tintin = ViraLata(pai=rex)
# print(type(rex), type(tintin))
# print(isinstance('', Cachoro))
# print(isinstance(rex, Cachoro))
# print(id(rex), id(tintin))
# print(rex is tintin)
rex_clone = rex
# rex = Cachoro()
# print(rex is rex_clone)
# print(id(rex), id(rex_clone))
# print(Cachoro.olhos, rex.olhos, tintin.olhos)
tintin.nome = 'Tin Tin'
print(rex.nome)
print(tintin.nome)
print(rex.latir())
print(tintin.latir())
print(rex_clone.latir())
print(rex.__dict__)
{'nome': 'Foo'}
print(isinstance(tintin, Cachoro))
print(isinstance(tintin, ViraLata))
print(isinstance(rex, ViraLata))
cachoros = [tintin, rex]

for c in cachoros:
    print(c.latir())

print(tintin.pai.nome)
rex.retonar_ao_dono()
