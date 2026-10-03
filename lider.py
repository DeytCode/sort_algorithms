from random import randint

lider = randint(1, 10)
T = [lider if randint(0,1) else randint(1, 10) for _ in range(10)]

print(T)

# O(n^2)
def find_lider1(A):
    for i in range(len(A) // 2 + 1):
        count = 1
        k = A[i]
        for j in range(i+1, len(A)):
            if k == A[j]:
                count += 1
        if count > len(A) // 2:
            return k
    return None

# O(nlgn)
def find_lider2(A):
    A.sort()
    k = A[len(A)//2]
    count = 0
    for el in A:
        if el == k:
            count += 1
    if count > len(A) // 2:
        return k
    return None

# O(n)
def find_lider3(A):
    count = 0
    k = None
    for el in A:
        if count == 0:
            k = el
            count += 1
        elif k == el: count += 1
        else: count -= 1

    count = 0
    for el in A:
        if el == k: count += 1
    if count > len(A) // 2: return k
    return None



print(f"lider: {find_lider1(T)}" if find_lider1(T) is not None else "brak lidera")
print(f"lider: {find_lider2(T)}" if find_lider2(T) is not None else "brak lidera")
print(f"lider: {find_lider3(T)}" if find_lider3(T) is not None else "brak lidera")
