import math

operator = str(input('Enter operatior: '))

a = 0
num = int(input('Enter: '))

match operator:
    case "+":

        while num != 0:
            a += num
            num = int(input('Enter: '))

        print(a)

    case "-":
   
        while num != 0:
            a -= num
            num = int(input('Enter: '))

        print(a)

    case "*":

        while num != 0:
            a *= num
            num = int(input('Enter: '))

        print(a)

    case "/":

        while num != 0:
            num = int(input('Enter: '))
            if num != 0:
                a /= num

        print(a)

    case "root":
        num = int(input('Enter: '))

        print(math.sqrt(num))

    case "exponent":
        num = int(input('Enter: '))
        exponent = int(input('Enter exponent: '))

        print(num ** exponent)

    case _:
        print('Invalid operation')
