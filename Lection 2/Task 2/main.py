elements = input("Input elements array: ").split()

for element in elements:
    if element.isdigit():
        print(element, end = " ")

