# -*- coding: utf-8 -*-
"""Persistencia multiplicativa: multiplique os digitos e repita.

    39 -> 27 -> 14 -> 4        persistencia 3
    277 -> 98 -> 72 -> 14 -> 4 persistencia 4

A persistencia de um numero e quantos passos ele leva para virar um digito so.
Erdos conjecturou que ela e LIMITADA — que existe um teto e nenhum numero no
mundo o ultrapassa. O recordista conhecido e

    277777788888899    com persistencia 11

e, apesar de buscas que passaram de 10^233, ninguem achou nada com 12.

O detalhe que torna a busca viavel: o produto dos digitos NAO depende da ordem
deles. 39 e 93 tem a mesma cadeia. Entao nao e preciso varrer numeros — basta
varrer MULTICONJUNTOS de digitos, o que troca 10^n por C(n+9, 9).
"""


def produto_dos_digitos(n):
    """O produto dos digitos de n."""
    if n < 0:
        raise ValueError('n nao pode ser negativo: %r' % (n,))
    produto = 1
    for caractere in str(n):
        produto *= int(caractere)
    return produto


def cadeia(n):
    """A cadeia inteira, de n ate um digito so."""
    saida = [n]
    atual = n
    while atual >= 10:
        atual = produto_dos_digitos(atual)
        saida.append(atual)
    return saida


def persistencia(n):
    """Quantos passos ate virar um digito so."""
    return len(cadeia(n)) - 1


def persistencia_de_digitos(digitos):
    """A persistencia de um numero formado por estes digitos.

    Como o produto nao depende da ordem, basta o multiconjunto. O primeiro
    passo e feito aqui direto, sem montar o numero.
    """
    if not digitos:
        raise ValueError('a lista de digitos esta vazia')
    produto = 1
    for d in digitos:
        produto *= d
    if len(digitos) == 1:
        return 0
    return 1 + persistencia(produto)


def menor_numero_com_digitos(digitos):
    """O menor numero que se escreve com estes digitos: os menores na frente,
    mas sem zero na primeira casa."""
    ds = sorted(digitos)
    if ds[0] == 0:
        for i, d in enumerate(ds):
            if d != 0:
                ds[0], ds[i] = ds[i], ds[0]
                break
        else:
            return 0
    return int(''.join(str(d) for d in ds))
