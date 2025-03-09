"""
Mamy dwie tablice stairs[k] oraz people[l]. Tablica stairs[k] zawiera wysokosci schodkow, a people[l] zawiera maksymala
wysokosc schodka, na ktora moze wejsc dana osoba. Jaka bedzie calkowita ilosc "krokow" wszystkich ludzi?
"""

from random import randint

"""
Pomysl:
    (1) Przechodzimy maksymalna wysokosc stopnia dla kazdej osoby.
    
    (2) Kazda osoba wchodzi po schodach tak dlugo dopoki
        nie trafi na stopien wyzszy niz jej maksymalny stopien.
        Przy kazdej "udanej" iteracji zwiekszamy licznik krokow.
        
Zlozonosc: O(l*k)
"""


def stairs_distance_v1(people, stairs):
    total = 0

    # (1)
    for max_height in people:
        # (2)
        for step in stairs:
            if step > max_height:
                break
            total += 1

    return total


"""
Pomysl:
    (1) Tworzymy tablice z minimalna wysokoscia stopnia potrzebna na dotarcie na dany stopien.
        Na przyklad tablica [1, 5, 6, 6, 6, 8, 19] informuje nas, ze dotarcie na 3 stopien wymaga od
        osoby mozliwosci wejscia na stopien o wysokosci 6. Zauwazmy ze tablica ta jest posortowana rosnaca,
        poniewaz po wystapieniu wysokosci k, wszystkie wysokosci na kolejnych indeksach musza byc conajmniej k.
        
    (2) Przechodzimy przez tablice people i dla kazdej osiagalnej wysokosci wyszukujemy binarnie w tablicy
        utworzonej w kroku (1) indeks pierwszego schodka wyzszego od szukanej wysokosci. Na przyklad
        
            Szukamy liczby stopni o wysokosci <= 4, czyli indeksu pierwszego stopnia o wysokosci > 4.
            
            count_steps([1, 2, 3, 4, 6], 4) == 4
            count_steps([1, 2, 3, 3, 6], 4) == 4
            
        Wyniki otrzymane dla kazdej osoby sumujemy.
        
Zlozonosc: O(l*logk)
        
"""


def count_steps(a, l, r, v):
    if l >= r:
        return l

    mid = l + (r - l) // 2

    if a[mid] <= v:
        return count_steps(a, mid + 1, r, v)
    else:
        return count_steps(a, l, mid, v)


def stairs_distance_v2(people, stairs):
    # (1)
    min_height = float("-inf")
    reachable = [min_height := max(min_height, step) for step in stairs]

    k = len(stairs)
    total = 0

    # (2)
    for height in people:
        total += count_steps(reachable, 0, k, height)

    return total


for _ in range(10):
    # arrange
    people = [randint(10, 90) for _ in range(5)]
    stairs = [randint(10, 50) for _ in range(10)]
    expected = stairs_distance_v1(people, stairs)

    # test
    got = stairs_distance_v2(people, stairs)

    # assert
    assert got == expected
    print("OK")
