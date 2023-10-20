def middle(start, ending):
    return (start + ending) // 2


start = 1
ending = 50
print('think of a number between 1-50. ')
while True:
    x = int(middle(start, ending))
    response = input(f"Is the number {x}? Please type 'higher', 'lower' or 'yes': ")
    if response.lower() == 'higher':
        start = x
    elif response == 'lower':
        ending = x
    elif response == 'yes':
        print(f'The number is {x}')
    else:
        print("Invalid input please type 'yes', 'lower' or 'higher")
    break




