"""
Przedziały jednostajne.

Chcemy posortować tablicę T.

Tablica zawiera N liczb. Mamy k przedziałów.   [a1, b1), [a2, b2), [ak, bk).
Każdy z tych przedziałów ma prawdopodobieństwo   c1          c2       ck.
Granice przedziałów to liczby naturalne.

Wybieramy przedział,

Tworzymy tablice:
    1) Losujemy przedzial zgodnie z ich prawdopodobienstwami
    2) Wybieramy element z przedzialu
    i tak k razy

Idea:
    Bierzemy kubelek,
    kazdy kubelek dane rozlozone jednostajnie
    robimy bucket sort
"""
