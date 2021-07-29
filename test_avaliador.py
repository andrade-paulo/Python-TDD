from unittest import TestCase # Biblioteca padrão para TDD
from dominio import Leilao, Usuario, Lance

# python3 -m unittest {nome_arquivo.py} -> Realiza todos os testes do arquivo
# python3 -m unittest {nome_arquivo.py}.{nomeClasse}.{nome_funcao} -> Realiza o teste de uma função específica

class TestAvaliador(TestCase):

    def setUp(self): # Método para isolar código e evitar repetição
        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_menor_valor_quando_leilao_tiver_em_ordem_crescente(self): # Nomeclatura detalhada
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        menor_valor = 100
        maior_valor = 150

        self.assertEqual(menor_valor, self.leilao.menor_lance)
        self.assertEqual(maior_valor, self.leilao.maior_lance)
    
    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        with self.assertRaises(ValueError): # O teste passa, caso o resultado seja um ValueError
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_yuri)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_gui)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri')
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
    
    def test_nao_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_igual(self):
        lance_do_gui200 = Lance(self.gui, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)
    
    
