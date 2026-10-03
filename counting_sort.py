from random import randint, seed

seed(123)
n = int(input("podaj n: "))
T = [randint(1, 6) for _ in range(n)]



def counting_srt(A):
    max_v = max(A)  # złożoność liniowa
    min_v = min(A)  # złożoność liniowa

    count_A = [0] * (max_v - min_v + 1)

    # zliczanie
    for el in A:
        count_A[el - min_v] += 1

    # tablica skumulowana
    for i in range(1, len(count_A)):
        count_A[i] += count_A[i - 1]

    out_A = [0] * len(A)
    for el in reversed(A):
        i = count_A[el - min_v]
        out_A[i - 1] = el
        count_A[el - min_v] -= 1


    return  out_A

print(T)
A = counting_srt(T)
print(A)
