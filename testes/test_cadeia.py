# -*- coding: utf-8 -*-
import unittest

from persistencia import cadeia


class TestCadeia(unittest.TestCase):

    def test_produto_dos_digitos(self):
        self.assertEqual(cadeia.produto_dos_digitos(39), 27)
        self.assertEqual(cadeia.produto_dos_digitos(999), 729)
        self.assertEqual(cadeia.produto_dos_digitos(105), 0)
        self.assertEqual(cadeia.produto_dos_digitos(7), 7)

    def test_a_cadeia_do_39(self):
        self.assertEqual(cadeia.cadeia(39), [39, 27, 14, 4])
        self.assertEqual(cadeia.persistencia(39), 3)

    def test_a_cadeia_do_recordista(self):
        c = cadeia.cadeia(277777788888899)
        self.assertEqual(cadeia.persistencia(277777788888899), 11)
        self.assertEqual(c[1], 4996238671872)
        self.assertEqual(c[-1], 0)

    def test_um_digito_tem_persistencia_zero(self):
        for n in range(10):
            self.assertEqual(cadeia.persistencia(n), 0, n)

    def test_toda_cadeia_termina_em_um_digito(self):
        for n in range(1, 3000):
            self.assertLess(cadeia.cadeia(n)[-1], 10, n)

    def test_cada_passo_e_o_produto_do_anterior(self):
        for n in (39, 77, 679, 6788, 68889):
            c = cadeia.cadeia(n)
            for anterior, seguinte in zip(c, c[1:]):
                self.assertEqual(cadeia.produto_dos_digitos(anterior), seguinte)

    def test_a_ordem_dos_digitos_nao_muda_a_persistencia(self):
        self.assertEqual(cadeia.persistencia(39), cadeia.persistencia(93))
        self.assertEqual(cadeia.persistencia(679), cadeia.persistencia(976))
        self.assertEqual(cadeia.persistencia(679), cadeia.persistencia(796))

    def test_persistencia_de_digitos(self):
        self.assertEqual(cadeia.persistencia_de_digitos([3, 9]), 3)
        self.assertEqual(cadeia.persistencia_de_digitos([7, 7]), 4)
        self.assertEqual(cadeia.persistencia_de_digitos([5]), 0)

    def test_menor_numero_com_digitos(self):
        self.assertEqual(cadeia.menor_numero_com_digitos([3, 9]), 39)
        self.assertEqual(cadeia.menor_numero_com_digitos([9, 3]), 39)
        # o zero nao pode ficar na frente
        self.assertEqual(cadeia.menor_numero_com_digitos([0, 1]), 10)
        self.assertEqual(cadeia.menor_numero_com_digitos([0, 0, 5]), 500)
        self.assertEqual(cadeia.menor_numero_com_digitos([0, 0]), 0)

    def test_entrada_invalida_e_recusada(self):
        with self.assertRaises(ValueError):
            cadeia.produto_dos_digitos(-1)
        with self.assertRaises(ValueError):
            cadeia.persistencia_de_digitos([])


if __name__ == '__main__':
    unittest.main()
