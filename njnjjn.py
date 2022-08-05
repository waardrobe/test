def summa(a, b=7, c=8):
    print(a, b, c)
summa(c=1, b=20, a=21)


def summa(*args):
    print(args)
summa(7, 8, 9, 10)

def summa(*numbers):
    print(sum(numbers))
summa(7, 8, 9, 10)


def brand(**brands):
    for x, y in brands.items():
        print(x, ":", y)
brand(a="Apple", s="Samsung")