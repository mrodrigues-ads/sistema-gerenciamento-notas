import unittest

from gerenciador_notas import calcular_media, verificar_aprovacao


class TestGerenciadorNotas(unittest.TestCase):

    def test_calcular_media_com_sucesso(self):
        """Testa o cálculo correto da média."""
        notas = [8.0, 7.0, 9.0]
        self.assertEqual(calcular_media(notas), 8.0)

    def test_verificar_aprovacao(self):
        """Testa a aprovação com média acima da mínima."""
        self.assertEqual(
            verificar_aprovacao(8.0),
            "Aprovado"
        )

    def test_verificar_reprovacao(self):
        """Testa a reprovação com média abaixo da mínima."""
        self.assertEqual(
            verificar_aprovacao(5.0),
            "Reprovado"
        )

    def test_lista_vazia(self):
        """Testa o comportamento com lista de notas vazia."""
        self.assertEqual(
            calcular_media([]),
            0.0
        )

    def test_media_minima_zero(self):
        """Testa aprovação quando a média mínima é zero."""
        self.assertEqual(
            verificar_aprovacao(0.0, media_minima=0),
            "Aprovado"
        )


if __name__ == "__main__":
    unittest.main()
