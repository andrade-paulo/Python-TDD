from excecoes import LanceInvalido

class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def nome(self):
        return self.__nome
    
    @property
    def carteira(self):
        return self.__carteira
    
    def propoe_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor):
            raise LanceInvalido("Valor inválido")

        lance = Lance(self, valor)
        leilao.propoe(lance)

        self.__carteira -= valor
    
    def _valor_eh_valido(self, valor):
        return valor <= self.__carteira

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
        if self._lance_eh_valido(novo_lance): # Regras de negócio
            if not self._tem_lances():
                self.menor_lance = novo_lance.valor
            
            self.maior_lance = novo_lance.valor
        
            self.__lances.append(novo_lance)
        else:
            raise LanceInvalido('Erro ao propor lance')


    @property
    def lances(self):
        return self.__lances[:]
    
    # Funções para melhorar a legibilidade do código

    def _tem_lances(self):
        return self.__lances
    

    def _ultimo_usuario_diferente(self, novo_lance):
        if self.lances[-1].usuario != novo_lance.usuario:
            return True
        raise LanceInvalido("Um usuário não pode dar dois lances seguidos")
    

    def _valor_maior_que_ultimo_lance(self, novo_lance):
        if novo_lance.valor > self.lances[-1].valor:
            return True
        raise LanceInvalido("O valor precisa ser maior que o do último lance")
    

    def _lance_eh_valido(self, novo_lance):
        return not self._tem_lances() or (self._ultimo_usuario_diferente(novo_lance) and 
                                          self._valor_maior_que_ultimo_lance(novo_lance))
