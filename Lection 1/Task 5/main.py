import math

def calcDiscriminant(a, b, c):
    return (b ** 2) - (4 * a * c)

num_a = int(input('Enter a: '))
num_b = int(input('Enter b: '))
num_c = int(input('Enter c: '))

if num_a == 0:
    print('This is not a quadratic equation :)')
else:
    D = calcDiscriminant(num_a, num_b, num_c)

    if D > 0:
        x1 = ((-num_b + math.sqrt(D)) / (2 * num_a))
        x2 = ((-num_b - math.sqrt(D)) / (2 * num_a))

        print("x1: " + str(x1))
        print("x2: " + str(x2))
    elif D == 0:
        x = -(num_b / (2 * num_a))

        print("x: " + str(x))
    else:
        print('No real solutions')
