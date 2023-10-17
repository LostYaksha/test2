import random

print('Welcome to cow and bulls.')

while True:
    num1 = input("Player1, please enter a 4 digit number: ")
    if len(num1) == 4 and num1.isdigit():
        break
    else:
        print("Invalid input. Please enter a 4 digit number.")

while True:
    num2 = input("Player2, please enter a 4 digit number: ")
    if len(num2) == 4 and num2.isdigit():
        break
    else:
        print("Invalid input. Please enter a 4 digit number.")

cows_p1 = 0
bulls_p1 = 0
cows_p2 = 0
bulls_p2 = 0

x = random.randint(1000, 10000)
number = list(str(x))
print(f'the correct number is {x}')

p1_cor = [num1[i] for i in range(len(num1)) if num1[i] == number[i]]
p2_cor = [num2[i] for i in range(len(num2)) if num2[i] == number[i]]
cows_p1 += len(p1_cor)
bulls_p1 += 4 - len(p1_cor)
cows_p2 += len(p2_cor)
bulls_p2 += 4 - len(p1_cor)

print(f'p1 has {cows_p1} cows and {bulls_p1} bulls')
print(f'p1 has {cows_p2} cows and {bulls_p2} bulls')

if cows_p1 > cows_p2:
    print('player 1 won.')
elif cows_p1 == cows_p2:
    print('draw')
else:
    print('player 2 won.')
