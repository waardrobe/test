f = open("1.txt", "r")
print(f.read())
f.close()

with open("1.txt", "a") as f:
    f.write("hghghg")



try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ZeroDivisionError:
    print("На ноль делить нельзя")
