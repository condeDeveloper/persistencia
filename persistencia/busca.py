# -*- coding: utf-8 -*-
"""A busca pelo menor numero de cada persistencia, por multiconjuntos.

Varrer todos os numeros ate 10^15 e impossivel. Varrer os multiconjuntos de
ate 15 digitos sao 1,3 milhao de casos — e, como o produto dos digitos nao
muda com a ordem, nada se perde.

Para achar o MENOR numero com certa persistencia, basta montar o menor numero
possivel de cada multiconjunto (digitos em ordem crescente) e comparar.
"""
from itertools import combinations_with_replacement

from . import cadeia


def varrer_multiconjuntos(ate_digitos):
    """A melhor persistencia achada e o menor numero que a alcanca.

    Devolve {persistencia: menor numero}.
    """
    if ate_digitos < 1:
        raise ValueError('ate_digitos tem que ser positivo: %r' % (ate_digitos,))
    melhores = {}
    for n in range(1, ate_digitos + 1):
        for combinacao in combinations_with_replacement(range(10), n):
            # O zero NAO pode ser pulado. Ele zera o produto na hora, e por
            # isso nao serve para persistencia alta — mas o menor numero com
            # persistencia 1 e exatamente o 10, e pular combinacoes com zero
            # faz a tabela dizer 11. Quem decide e a conta, nao o palpite.
            numero = cadeia.menor_numero_com_digitos(combinacao)
            if len(str(numero)) != n:
                continue
            p = cadeia.persistencia_de_digitos(combinacao)
            if p not in melhores or numero < melhores[p]:
                melhores[p] = numero
    return melhores


def quantos_multiconjuntos(ate_digitos):
    """Quantas combinacoes a busca constroi."""
    total = 0
    for n in range(1, ate_digitos + 1):
        numerador = 1
        for i in range(9):
            numerador = numerador * (n + 9 - i) // (i + 1)
        total += numerador
    return total


def quantos_numeros(ate_digitos):
    """Quantos inteiros a forca bruta olharia."""
    return 10 ** ate_digitos - 1


def digitos_proibidos_nos_recordistas(melhores):
    """Quais digitos NAO aparecem nos numeros recordistas.

    Um 0 zera o produto. Um 1 nao muda nada e so gasta uma casa. Um 5 junto com
    qualquer par produz um 0 no fim do produto, que zera o passo seguinte. A
    busca nao sabe disso — a tabela mostra se ela chegou la sozinha.
    """
    usados = set()
    for p, numero in melhores.items():
        if p >= 3:
            usados.update(int(c) for c in str(numero))
    return sorted(set(range(10)) - usados), sorted(usados)
