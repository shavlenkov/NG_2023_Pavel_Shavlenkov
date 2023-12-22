number = int(input("Введите число: "))

for i in range(1, number + 1):
    dividers = ""

    for j in range(1, number + 1):
        if (i % j) == 0:
            dividers += "{:<3}".format(str(j))
    
    print(str(i) + " | " +  dividers)
   