class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = float(valor)

class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = float('-inf') # Menor valor possível
        self.menor_lance = float('inf') # Maior valor possível

    def propoe(self, novo_lance: Lance):
        if not self.lances or (self.lances[-1].usuario != novo_lance.usuario and novo_lance.valor > self.lances[-1].valor): # Regras de negócio
            self.__lances.append(novo_lance)
            
            if novo_lance.valor > self.maior_lance:
                self.maior_lance = novo_lance.valor
            if novo_lance.valor < self.menor_lance:
                self.menor_lance = novo_lance.valor
        else:
            raise ValueError('Erro ao propor lance')

    @property
    def lances(self):
        return self.__lances[:]
