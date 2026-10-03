from random import choice, randrange

def create_tab(n):
    T = [[choice([True, False]) for _ in range(n)] for _ in range(n)]

    if choice([True, False]):
        k = randrange(n)
        for i in range(n):
            T[k][i] = False

        for i in range(n):
            T[i][k] = True

    for i in range(n):
        T[i][i] = "X"

    return T


def print_tab(T, n):
    print("   ", end='')
    for i in range(n):
        print(f"{i:^3}", end='')
    print()
    for i in range(n):
        print(f"{i:<3}", end='')
        for j in range(n):
            print(f"{T[i][j]:^3}", end='')
        print()


def find_idol1(T, n):
    k = None
    for i in range(n):
        for j in range(n):
            if j == i:  # pomijanie przekątnej
                continue
            elif T[i][j] == False:
                continue
            else:
                break
        else:
            k = i
            break

    if k is None:
        return  False
    else:
        for i in range(n):
            if T[i][k] == False:
                return False
    return True


def find_idol2(T, n):

    # szukamy kandydata
    k = 0
    for i in range(1, n):
        if T[k][i] == True:
            k = i

    # sprawdzamy
    T[k][k] = False
    for i in range(n):
        if T[k][i] == True:
            return False

    T[k][k] = True
    for i in range(n):
        if T[i][k] == False:
            return False

    return True



T = create_tab(5)
print_tab(T, len(T))

print(f"jest idol" if find_idol1(T, len(T)) else "brak idola")
print(f"jest idol" if find_idol2(T, len(T)) else "brak idola")
