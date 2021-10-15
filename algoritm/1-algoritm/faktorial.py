# 1 dan N gacha bo'lgan faktarialni hisoblash

def faktorial(N):
    i = 1
    fakt = 1
    while i != N + 1:
        fakt = fakt * i
        i += 1
    return fakt


if __name__ == '__main__':
    print(faktorial(5))
    print(faktorial(6))
    print(faktorial(8))


    # shart orqali
    def factorial(n):
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)


    print(factorial(5))
