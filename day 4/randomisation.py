import random
# import my_mdule

# randomInterger = random.randint(1, 10)
# print(randomInterger)
# print(my_mdule.my_favourite_number)

# randon_number = random.random() *10 
# random_float = random.uniform(1, 10)
# print(random_float)
# print(randon_number)

# options = ["heads", "tails"]
# coin = options[random.randint(0, 1)]
# print(coin)

options = ["Rock", "Paper", "Scissors"]
print("Rock / Paper / Scissors")
user_choice = input("").capitalize()
computer_choice = options[random.randint(0, 2)]
print(computer_choice)
if (user_choice == computer_choice):
    print("Draw")
elif (user_choice == "Rock" and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == "Scissors" and computer_choice == "Paper"):
    print("You win")
else:
    print("You lose")