print('Select an option:')
print('1 - Convert F to C')
print('0 - Convert C to F')

option = int(input('Enter your choice: '))

while option != 0 and option != 1:
  option = int(input('Enter your choice: '))

deg = int(input('Enter deg: '))

if option == 1:
  print("{} F is {} C".format(deg, ((deg * 1.8) + 32)))
elif option == 0:
  print("{} C is {} F".format(deg, ((deg - 32) / 1.8)))