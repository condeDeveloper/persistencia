# persistencia

Multiplique os dígitos de um número. Repita com o resultado. Pare quando sobrar um dígito
só. Quantos passos levou?

```
39 → 27 → 14 → 4                          3 passos
77 → 49 → 36 → 18 → 8                     4 passos
679 → 378 → 168 → 48 → 32 → 6             5 passos
```

Isso é a **persistência multiplicativa**, e Erdős conjecturou que ela é **limitada** — que
existe um teto e nenhum número no mundo o ultrapassa. O recordista conhecido é

```
277777788888899 → 4996238671872 → 438939648 → 4478976 → 338688
                → 27648 → 2688 → 768 → 336 → 54 → 20 → 0
```

**Onze passos.** Buscas já passaram de 10²³³ sem achar um número com doze.

Este repositório encontra o recordista em **sete segundos**, varrendo 3,2 milhões de casos
em vez de 10¹⁵ números.

```bash
python -m unittest discover -s testes -t . -v   # 19 testes
python -m ferramentas.medidor                   # todas as tabelas
python -m ferramentas.medidor --completo        # até 15 dígitos (job próprio)
```

Python 3.11+, sem dependência nenhuma fora da biblioteca padrão.

## Por que não é preciso varrer números

O produto dos dígitos **não depende da ordem deles**. `39` e `93` têm exatamente a mesma
cadeia. Então não há motivo para olhar números — basta olhar **multiconjuntos de
dígitos**, que são `C(n+9, 9)`.

```
dígitos   multiconjuntos   números                  economia
5         3.002            99.999                   33x
8         43.757           99.999.999               2.285x
11        352.715          99.999.999.999           283.500x
15        3.268.759        999.999.999.999.999      3,06 × 10⁸
20        30.045.014       10²⁰                     3,33 × 10¹²
```

Essa troca é o projeto inteiro. E ela só é legítima porque a propriedade que a sustenta é
**conferida**, não suposta: um teste varre 47.253 pares de números com os mesmos dígitos e
exige que a persistência seja igual em todos.

## O menor número de cada persistência

```
persistência   menor número
0              0
1              10
2              25
3              39
4              77
5              679
6              6788
7              68889
8              2677889
9              26888999
10             3778888999
11             277777788888899
```

Repare no salto final: de **dez dígitos** para **quinze**. E depois disso, nada — até 15
dígitos não existe persistência 12, e o job de fundo falha de propósito se algum dia
encontrar uma.

## Os recordistas só usam seis dígitos

```
dígitos que aparecem    : 2, 3, 6, 7, 8, 9
dígitos que NÃO aparecem: 0, 1, 4, 5
```

A busca não foi instruída a evitar nada. Ela chegou nisso sozinha, e os motivos são
visíveis depois de medidos:

- o **0** zera o produto na hora, acabando a cadeia em um passo;
- o **1** não muda o produto e só gasta uma casa, deixando o número maior à toa;
- o **5** junto com qualquer dígito par produz um zero no fim do produto, que mata o passo
  seguinte.

O **4** é o que surpreende: ele não zera nada e é mais compacto que dois dois. Mesmo assim
não aparece em nenhum recordista medido.

## As três conferências

```
multiconjunto x varredura bruta até 200.000 : 8 persistências iguais
cada passo é o produto dos dígitos          : 55 passos conferidos
a ordem dos dígitos não muda nada           : 47.253 números conferidos
```

O juiz varre inteiro por inteiro e não sabe que a ordem dos dígitos é irrelevante. Até
200.000 ele alcança **persistência 7**, no número 68.889 — e para ali. A busca por
multiconjuntos chega a 11 no mesmo tempo.

## O que as medidas me corrigiram

**Pulei as combinações com zero e perdi o 10.** Raciocinei que um zero zera o produto na
hora, então não serve para persistência alta — e está certo. Mas o **menor número com
persistência 1 é exatamente o 10**, e minha tabela dizia **11**. O filtro "esperto"
eliminou a resposta certa de uma linha inteira. Hoje o zero entra na varredura e quem
decide é a conta.

**O juiz e a busca começavam em lugares diferentes.** A varredura bruta ia de 1 até o
limite; a busca por multiconjuntos incluía o próprio 0. Resultado: a conferência acusou
divergência na persistência 0 — a busca dizia `0`, o juiz dizia `1`. Nenhum dos dois
estava errado sobre persistência; eles discordavam sobre **onde começa a contagem**. A
conferência pegou isso na primeira execução, que é exatamente o que ela existe para fazer.

**Esperei o 4 entre os recordistas.** Ele não zera nada, não é neutro, e `4` ocupa uma
casa onde `2, 2` ocupa duas. Mesmo assim nenhum recordista medido usa um 4. A busca não
tinha opinião sobre isso; eu tinha, e estava errado.

**A varredura bruta é mais fraca do que parece.** Duzentos mil números — que soa muito —
só alcançam persistência 7. Para chegar a 11 por força bruta seria preciso varrer
10¹⁵ inteiros.

## Quatro achados

1. **O recordista mundial é encontrado em sete segundos**: `277777788888899`, com
   persistência 11, varrendo 3,2 milhões de multiconjuntos em vez de 10¹⁵ números — uma
   economia de **3 × 10⁸** vezes.
2. **Os recordistas usam apenas seis dos dez dígitos** — 2, 3, 6, 7, 8 e 9 — e a busca
   chegou nisso sem nenhuma instrução a respeito.
3. O salto entre as duas últimas persistências é **de dez dígitos para quinze**, e depois
   dele não existe mais nada: **nenhuma persistência 12** até 15 dígitos.
4. A varredura bruta até **200.000** só alcança **persistência 7** — enquanto a busca por
   multiconjuntos chega a 11 no mesmo tempo de execução.
