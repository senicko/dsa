from zad1testy import runtests

"""
Sebastian Flajszer

Złożoność czasowa: O(N + nlogn)
    (1): O(N)
    (2): O(nlogn)
    (3): O(n)
    
Złożoność pamięciowa: O(logn) - wywołania rekurencyjne w operacjach na heap'ie

Opis:

(1) Podczas liniowego przejścia po tablicy dla każdego słowa wybieramy leksykograficznie mniejszą wersję z niego 
    i jego odwrotności. Ten krok spowoduje, że słowa równoważne będą takimi samymi stringami.
    Następnie obliczamy hash wybranej wersji w celu zejścia ze złożoności O(k) do złożoności O(1) 
    przy porównywaniu stringów w szybkim algorytmie sortującym Heapsort. 
    
    Hash obliczany jest algorytmem "Polynomial Rolling Hash", który działa w czasie O(k). Przechodzi przez litery w przekazanym słowie 
    i sumuje ze sobą s[i]*p^i, biorąc ostatecznie % m. p i m to stałe często wykorzystywane przy tym algorytmie, m to duża 
    liczba pierwsza. W zasadzie obliczamy dwa hashe, z różnymi stałymi p i m, w celu zminimalizowania możliwości wystąpienia kolizji. 
    Elementy w tablicy T zamieniamy na krotki z obliczonymi hashami. 
    
    Złożoność kroku: O(N).
    
(2) Wykorzystujemy szybkie sortowanie Heapsort do posortowania obliczonych hashy. Pozwoli nam to na liniowe przejście
    po tablicy w celu znalezienia ilości powtórzeń pojedynczych słów. 
    
    Złożoność kroku: O(nlogn), ponieważ dzięki preprocessing'u z kroku (1) porównywanie napisów (ich hashy, którymi są liczby) zajmuje O(1). 
    
(3) Przechodzimy liniowo po posortowanej tablicy i szukamy najdłuższego podciągu o takich samych wyrazach. Możemy tak
    zrobić, ponieważ posortowaliśmy hash'e w podpunkcie (2). Długość najdłuższego podciągu to siła najsilniejszego napisu.
    
    Złożoność kroku: O(n)
"""

M1 = 10 ** 9 + 9
P1 = 31

M2 = 10 ** 9 + 7
P2 = 37


def hash(s):
    h1 = 0
    h2 = 0

    p1 = P1
    p2 = P2

    for c in s:
        h1 = (h1 + ord(c) * p1) % M1
        p1 = (p1 * P1) % M1

        h2 = (h2 + ord(c) * p2) % M2
        p2 = (p2 * P2) % M2

    return h1, h2


left = lambda i: 2 * i + 1
right = lambda i: 2 * i + 2
parent = lambda i: (i - 1) // 2


def heapify(a, n, i):
    l = left(i)
    r = right(i)
    max_index = i

    if l < n and a[l] > a[max_index]:
        max_index = l

    if r < n and a[r] > a[max_index]:
        max_index = r

    if max_index != i:
        a[max_index], a[i] = a[i], a[max_index]
        heapify(a, n, max_index)


def build_heap(a):
    n = len(a)
    for i in range(parent(n - 1), -1, -1):
        heapify(a, n, i)


def heapsort(a):
    n = len(a)
    build_heap(a)

    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)


def strong_string(T):
    n = len(T)

    # (1)
    for i in range(n):
        rev = T[i][::-1]
        T[i] = hash(T[i] if T[i] < rev else rev)

    # (2)
    heapsort(T)

    # (3)
    max_strength = 0
    current_strength = 1
    prev = T[0]

    for i in range(1, n):
        if T[i] == prev:
            current_strength += 1
        else:
            max_strength = max(max_strength, current_strength)
            current_strength = 1
            prev = T[i]

    return max(max_strength, current_strength)


# Odkomentuj by uruchomic duze testy
runtests(strong_string, all_tests=True)

# Zakomentuj gdy uruchamiasz duze testy
# runtests(strong_string, all_tests=False)
