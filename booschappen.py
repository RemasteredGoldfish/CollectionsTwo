list1 = []
while True:
    groceries = input('Add your items in your groceries list: ')
    groceries2 = int(input('and how much of the items u want?: '))
    list1.append(groceries)
    list1.append(groceries2)
    choice = input('want to quit? press yes, otherwise press anykey')
    if choice == 'yes':
        break

print(list1)