def fact(n):
    f = 1
    for i in range(n):
        f = f * i
    return n


def R_f(n):
    if n == 0 or n == 1:
        return 1

    return n * (R_f(n - 1))


a = int(input("Enter the number for factorial--->"))
b = bool(input("Enter 0 to use iterative method and 1 to use recursive method--->"))

if b == 0:
    print("using iterative", fact(a))
else:
    print("using recursive", R_f(a))
