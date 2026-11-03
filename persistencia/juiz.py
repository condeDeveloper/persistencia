# -*- coding: utf-8 -*-
"""O juiz: varre os numeros um a um, sem truque nenhum.

Nao sabe que a ordem dos digitos nao importa, nao pula multiplos de dez, nao
monta multiconjunto. Para cada inteiro, calcula a cadeia inteira e anota a
persistencia.

So alcanca sete ou oito digitos. E justamente por nao ter esperteza nenhuma que
ele pode julgar a busca que tem.
"""
from . import cadeia


def menores_por_persistencia(limite):
    """O menor numero de cada persistencia, varrendo de 1 ate o limite."""
    if limite < 1:
        raise ValueError('limite tem que ser positivo: %r' % (limite,))
    melhores = {}
    # comeca no ZERO: a persistencia de um digito so e zero, e o menor numero
    # com persistencia zero e o proprio 0.
    for n in range(0, limite + 1):
        p = cadeia.persistencia(n)
        if p not in melhores:
            melhores[p] = n
    return melhores


def distribuicao(limite):
    """Quantos numeros ate o limite tem cada persistencia."""
    conta = {}
    for n in range(1, limite + 1):
        p = cadeia.persistencia(n)
        conta[p] = conta.get(p, 0) + 1
    return conta


def maior_persistencia(limite):
    """A maior persistencia achada ate o limite, e onde."""
    melhor = -1
    onde = None
    for n in range(1, limite + 1):
        p = cadeia.persistencia(n)
        if p > melhor:
            melhor = p
            onde = n
    return melhor, onde
