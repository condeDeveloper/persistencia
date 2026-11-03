# -*- coding: utf-8 -*-
"""Os numeros do README, presos. Todos sairam do medidor."""
import unittest

from ferramentas import medidor
from persistencia import busca, juiz, varredura


class TestMedidas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.melhores = busca.varrer_multiconjuntos(medidor.DIGITOS)

    def test_o_menor_de_cada_persistencia(self):
        esperado = [0, 10, 25, 39, 77, 679, 6788, 68889,
                    2677889, 26888999, 3778888999]
        for p, numero in enumerate(esperado):
            self.assertEqual(self.melhores[p], numero, 'persistencia %d' % p)

    def test_o_dez_e_o_menor_com_persistencia_um(self):
        # pular combinacoes com zero faria esta tabela dizer 11
        self.assertEqual(self.melhores[1], 10)

    def test_ate_onze_digitos_a_maior_persistencia_e_dez(self):
        self.assertEqual(max(self.melhores), 10)
        self.assertNotIn(11, self.melhores)

    def test_os_recordistas_so_usam_seis_digitos(self):
        proibidos, usados = busca.digitos_proibidos_nos_recordistas(self.melhores)
        self.assertEqual(usados, [2, 3, 6, 7, 8, 9])
        self.assertEqual(proibidos, [0, 1, 4, 5])

    def test_a_economia_dos_multiconjuntos(self):
        multi, nums, razao = varredura.economia(5)
        self.assertEqual(multi, 3002)
        self.assertEqual(nums, 99_999)
        self.assertAlmostEqual(razao, 33.31, places=2)

        multi, nums, razao = varredura.economia(20)
        self.assertEqual(multi, 30_045_014)
        self.assertAlmostEqual(razao / 1e12, 3.328, places=3)

    def test_a_economia_cresce_com_os_digitos(self):
        razoes = [varredura.economia(n)[2] for n in (5, 8, 11, 15, 20)]
        for anterior, seguinte in zip(razoes, razoes[1:]):
            self.assertGreater(seguinte, anterior)

    def test_as_tres_conferencias(self):
        self.assertEqual(
            varredura.conferir_contra_juiz(medidor.LIMITE_JUIZ, medidor.DIGITOS), 8)
        self.assertEqual(
            varredura.conferir_cadeias(sorted(self.melhores.values())), 55)
        self.assertEqual(varredura.conferir_ordem_nao_importa(50_000), 47_253)

    def test_a_forca_bruta_so_alcanca_persistencia_sete(self):
        maior, onde = juiz.maior_persistencia(medidor.LIMITE_JUIZ)
        self.assertEqual(maior, 7)
        self.assertEqual(onde, 68_889)

    def test_o_recordista_mundial_tem_persistencia_onze(self):
        from persistencia import cadeia
        self.assertEqual(cadeia.persistencia(277777788888899), 11)
        self.assertEqual(len(str(277777788888899)), 15)


if __name__ == '__main__':
    unittest.main()
