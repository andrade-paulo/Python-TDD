from excecoes import LanceInvalido
from dominio import Leilao, Usuario
import pytest


@pytest.fixture # Fixtures evitam repetição de código no teste
def vini():
    return Usuario("Vini", 100.0)


@pytest.fixture
def leilao():
    return Leilao("Celular")


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 20.0)

    assert vini.carteira == 80.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 40.0)

    assert vini.carteira == 60.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.0


def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(vini, leilao):
    with pytest.raises(LanceInvalido): # Testando exceção 
        vini.propoe_lance(leilao, 200.0)