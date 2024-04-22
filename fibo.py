def recursive_nth_fibo(n):
    if n <= 1:
        return n
    else:
        return recursive_nth_fibo(n - 1) + recursive_nth_fibo(n - 2)

def main():
    n = int(input("Zadej počet prvků Fibonacciho posloupnosti: "))
    if n <= 0:
        print("Zadejte celé kladné číslo!")
        return

    fibonacci_seq = [recursive_nth_fibo(i) for i in range(n)]
    print(f"Prvních {n} prvků Fibonacciho posloupnosti je: {fibonacci_seq}")


if __name__ == "__main__":
    main()
