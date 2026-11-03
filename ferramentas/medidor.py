# -*- coding: utf-8 -*-
"""Roda as tabelas que vao para o README.

    python -m ferramentas.medidor
    python -m ferramentas.medidor --completo
"""
import sys
import time

from persistencia import busca, cadeia, juiz, varredura

DIGITOS = 11
LIMITE_JUIZ = 200000
DIGITOS_JUIZ = 6
DIGITOS_COMPLETO = 15


def titulo(texto):
    print()
    print(texto)
    print('-' * len(texto))


def as_cadeias():
    titulo('Algumas cadeias')
    for n in (39, 77, 679, 6788, 277777788888899):
        c = cadeia.cadeia(n)
        print('%-18d  %s   (persistencia %d)'
              % (n, ' -> '.join(str(x) for x in c[1:]), len(c) - 1))


def os_menores():
    titulo('O menor numero de cada persistencia, ate %d digitos' % DIGITOS)
    print('%-16s %-20s %s' % ('persistencia', 'menor numero', 'digitos'))
    for p, numero in varredura.tabela_dos_menores(DIGITOS):
        print('%-16d %-20d %d' % (p, numero, len(str(numero))))
    print()
    melhores = busca.varrer_multiconjuntos(DIGITOS)
    print('maior persistencia alcancada com ate %d digitos: %d' % (DIGITOS, max(melhores)))


def os_digitos():
    titulo('Que digitos aparecem nos recordistas')
    melhores = busca.varrer_multiconjuntos(DIGITOS)
    proibidos, usados = busca.digitos_proibidos_nos_recordistas(melhores)
    print('digitos que aparecem   : %s' % usados)
    print('digitos que NAO aparecem: %s' % proibidos)
    print()
    print('A busca nao foi instruida a evitar nenhum digito. Ela chegou nisso sozinha:')
    print('   o 0 zera o produto na hora;')
    print('   o 1 nao muda o produto e so gasta uma casa, deixando o numero maior;')
    print('   o 5 com qualquer par produz um zero no fim, que zera o passo seguinte.')


def a_economia():
    titulo('Multiconjuntos contra numeros')
    print('%-10s %-18s %-24s %s' % ('digitos', 'multiconjuntos', 'numeros', 'economia'))
    for n in (5, 8, 11, 15, 20):
        multi, nums, razao = varredura.economia(n)
        print('%-10d %-18d %-24d %.3e vezes' % (n, multi, nums, razao))


def o_juiz():
    titulo('As tres conferencias')
    print('multiconjunto x varredura bruta ate %d: %d persistencias iguais'
          % (LIMITE_JUIZ, varredura.conferir_contra_juiz(LIMITE_JUIZ, DIGITOS)))
    melhores = busca.varrer_multiconjuntos(DIGITOS)
    print('cada passo e o produto dos digitos    : %d passos conferidos'
          % varredura.conferir_cadeias(sorted(melhores.values())))
    print('a ordem dos digitos nao muda nada     : %d numeros conferidos'
          % varredura.conferir_ordem_nao_importa(50000))
    print()
    maior, onde = juiz.maior_persistencia(LIMITE_JUIZ)
    print('a varredura bruta ate %d acha persistencia maxima %d, em %d'
          % (LIMITE_JUIZ, maior, onde))


def completo():
    titulo('Varredura ate %d digitos' % DIGITOS_COMPLETO)
    comeco = time.time()
    melhores = busca.varrer_multiconjuntos(DIGITOS_COMPLETO)
    print('%-16s %s' % ('persistencia', 'menor numero'))
    for p in sorted(melhores):
        print('%-16d %d' % (p, melhores[p]))
    print()
    print('maior persistencia alcancada: %d' % max(melhores))
    multi, nums, razao = varredura.economia(DIGITOS_COMPLETO)
    print('multiconjuntos olhados: %d' % multi)
    print('numeros que a forca bruta olharia: %d' % nums)
    print('economia: %.3e vezes' % razao)
    print()
    print('tempo: %.1f s' % (time.time() - comeco))

    if melhores.get(11) != 277777788888899:
        print('MEDIDA MUDOU: o menor com persistencia 11 deveria ser 277777788888899')
        sys.exit(1)
    if 12 in melhores:
        print('NOTICIA: apareceu persistencia 12, que ninguem achou ate hoje')
        sys.exit(1)
    print('o recordista 277777788888899 bateu, e nao ha persistencia 12')


def main():
    if '--completo' in sys.argv:
        completo()
        return
    as_cadeias()
    os_menores()
    os_digitos()
    a_economia()
    o_juiz()


if __name__ == '__main__':
    main()
