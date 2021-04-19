














import random
flip_sides = []
heads = ["heads"]
tails =["tails"]
flip_sides= heads +tails
print(random.shuffle(flip_sides))




print("Welcome to the Coin Toss App")

print(f"I will flip a coin a set number of times")
flip_no = int(input("\nHow many times would you like to flip the coin: "))
import random
if flip_no >0:
    result = random.shuffle(flip_sides)
    flip_no=-1

    flip_result_question = input("Would you like to see the results of each flip?")
    print(type(flip_result_question))
    if flip_result_question.lower() == "y":
        print(result)
    elif flip_result_question == "n":
        print("okay")
    else:
        print("Select y(YES) or n(NO)")

import random

flip_sides = []
flip_sides = ["head", "tail"]

# shffled = random.sample(flip_sides, len(flip_sides))
# print(shffled[0])

print("Welcome to the Coin Toss App")
print("I will flip a coin a set number of times")

flip_no = int(input("\nHow many times would you like to flip the coin: "))

if flip_no > 0:
    flip_result = []
    for i in range(flip_no):
        side = random.sample(flip_sides, len(flip_sides))[0]
        flip_result.append(side)

    show_result = input("Would you like to see the results of each flip? ")

    if show_result.lower() == "y":
        print(flip_result)
        for i in flip_result:
            print(i)
    elif show_result.lower() == "n":
        print("You have chosen not to see the result")
    else:
        print("Select y(YES) or n(NO)")