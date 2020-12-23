a,b,c = input().split()

a = int(a)

b = int(b)

c = int(c)

while True:

    a = a*a

    b = b+b

    c = c+c

    if a == b == c:

        print(a)

        break