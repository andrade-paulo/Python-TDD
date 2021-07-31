from excecoes import LanceInvalido
from unittest import TestCase # Biblioteca padrão para TDD
from dominio import Leilao, Usuario

# python3 -m unittest {nome_arquivo.py} -> Realiza todos os testes do arquivo
# python3 -m unittest {nome_arquivo.py}.{nomeClasse}.{nome_funcao} -> Realiza o teste de uma função específica

class TestAvaliador(TestCase):

    def setUp(self): # Método para isolar código e evitar repetição
        self.gui = Usuario('Gui', 1000.0)
        self.leilao = Leilao('Celular')


    def test_deve_retornar_o_maior_e_menor_valor_quando_leilao_tiver_em_ordem_crescente(self): # Nomeclatura detalhada
        yuri = Usuario('Yuri', 1500.0)

        yuri.propoe_lance(self.leilao, 100.0)
        self.gui.propoe_lance(self.leilao, 150.0)

        menor_valor = 100
        maior_valor = 150

        self.assertEqual(menor_valor, self.leilao.menor_lance)
        self.assertEqual(maior_valor, self.leilao.maior_lance)
    

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        yuri = Usuario('Yuri', 1500.0)

        with self.assertRaises(LanceInvalido): # O teste passa, caso o resultado seja um LanceInvalido
            self.gui.propoe_lance(self.leilao, 150.0)
            yuri.propoe_lance(self.leilao, 100.0)


    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.gui.propoe_lance(self.leilao, 150.0)


    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 1500.0)

        yuri.propoe_lance(self.leilao, 100.0)
        self.gui.propoe_lance(self.leilao, 150.0)
    

    def test_nao_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_igual(self):

        with self.assertRaises(LanceInvalido): # Testando exceção
            self.gui.propoe_lance(self.leilao, 150.0)
            self.gui.propoe_lance(self.leilao, 200.0)
    
    
