import math

operator = str(input('Enter operatior: '))

counter = 0
num = int(input('Enter: '))

match operator:
    case "+":

        while num != 0:
            counter += num
            num = int(input('Enter: '))

        print(counter)

    case "-":
   
        while num != 0:
            counter -= num
            num = int(input('Enter: '))

        print(counter)

    case "*":

        while num != 0:
            counter *= num
            num = int(input('Enter: '))

        print(counter)

    case "/":

        while num != 0:
            num = int(input('Enter: '))
            if num != 0:
                counter /= num

        print(counter)

    case "root":
        num = int(input('Enter: '))

        print(math.sqrt(num))

    case "exponent":
        num = int(input('Enter: '))
        exponent = int(input('Enter exponent: '))

        print(num ** exponent)

    case _:
        print('Invalid operation')
