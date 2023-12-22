import math

def calcDiscriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a == 0:
    print('This is not a quadratic equation :)')
else:
    D = calcDiscriminant(a, b, c)

    if D > 0:
        x1 = ((-b + math.sqrt(D)) / (2 * a))
        x2 = ((-b - math.sqrt(D)) / (2 * a))

        print("x1: " + str(x1))
        print("x2: " + str(x2))
    elif D == 0:
        x = -(b / (2 * a))

        print("x: " + str(x))
    else:
        print('No real solutions')
