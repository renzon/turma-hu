class Cachoro:
    olhos = 2

    def __init__(self, nome: str = '', pai: 'Cachoro' = None):
        self.pai = pai
        self.nome = nome

    def latir(self):
        return f'{self.nome}: Au'


class ViraLata(Cachoro):

    def latir(self):
        return f'{self.nome}: Ain Ain'


rex = Cachoro('Rex')
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
