# -*- coding: utf-8 -*-
"""Confere os dois caminhos e mede o que a busca encontrou."""
from . import busca, cadeia, juiz


def conferir_contra_juiz(limite, ate_digitos):
    """Compara os menores achados por multiconjunto com a varredura bruta.

    So compara as persistencias que a varredura bruta alcanca dentro do limite.
    Devolve quantas persistencias foram conferidas.
    """
    por_multiconjunto = busca.varrer_multiconjuntos(ate_digitos)
    por_forca_bruta = juiz.menores_por_persistencia(limite)
    conferidas = 0
    for p, numero in sorted(por_forca_bruta.items()):
        if p not in por_multiconjunto:
            raise AssertionError('a busca por multiconjunto nao achou persistencia %d' % p)
        if por_multiconjunto[p] != numero:
            raise AssertionError(
                'persistencia %d: multiconjunto diz %d, forca bruta diz %d'
                % (p, por_multiconjunto[p], numero))
        conferidas += 1
    return conferidas


def conferir_cadeias(numeros):
    """Confere que cada passo da cadeia e mesmo o produto dos digitos."""
    passos = 0
    for n in numeros:
        c = cadeia.cadeia(n)
        for anterior, seguinte in zip(c, c[1:]):
            if cadeia.produto_dos_digitos(anterior) != seguinte:
                raise AssertionError('a cadeia de %d errou: %d nao vira %d'
                                     % (n, anterior, seguinte))
            passos += 1
        if c[-1] >= 10:
            raise AssertionError('a cadeia de %d nao terminou em um digito' % n)
    return passos


def conferir_ordem_nao_importa(limite):
    """Confere que numeros com os mesmos digitos tem a mesma persistencia.

    E a propriedade que autoriza varrer multiconjuntos em vez de numeros. Se
    ela falhar em um caso, a busca inteira esta errada.
    """
    por_digitos = {}
    conferidos = 0
    for n in range(10, limite + 1):
        chave = tuple(sorted(str(n)))
        p = cadeia.persistencia(n)
        if chave in por_digitos:
            if por_digitos[chave] != p:
                raise AssertionError(
                    'dois numeros com os mesmos digitos tem persistencias diferentes: '
                    '%d e o outro de %r' % (n, chave))
            conferidos += 1
        else:
            por_digitos[chave] = p
    return conferidos


def economia(ate_digitos):
    """Multiconjuntos contra numeros."""
    multi = busca.quantos_multiconjuntos(ate_digitos)
    nums = busca.quantos_numeros(ate_digitos)
    return multi, nums, nums / multi


def tabela_dos_menores(ate_digitos):
    """Os menores numeros de cada persistencia, em ordem."""
    melhores = busca.varrer_multiconjuntos(ate_digitos)
    return [(p, melhores[p]) for p in sorted(melhores)]
