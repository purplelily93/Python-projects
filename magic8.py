name = input('Enter name here: ')
question = input("Enter your question here: ")
answer = " "
magic_8 = "Magic 8 Ball's answer: "

import random
random_number = int(input("Enter number here: "))
random.randint(1, 9)
print(random_number)

if random_number == 1:
    print(magic_8, "Yes-definitely")
elif random_number == 2:
    print(magic_8, "It is decidedly so")
elif random_number == 3:
    print(magic_8, "Without a doubt")
elif random_number == 4:
    print(magic_8, "Reply hazy, try again")
elif random_number == 5:
    print(magic_8, "Ask again later")
elif random_number == 6:
    print(magic_8, "Better not tell you now")
elif random_number == 7:
    print(magic_8, "My sources say no")
elif random_number == 8:
    print(magic_8, "Outlook not so good")
elif random_number == 9:
    print(magic_8, "Very doubtful")
else:
    print("Error")

print(name, "asks: ", question)