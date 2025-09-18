print("Welcome to the treasure island. You must make the right choices to find the treasure.")
print("You are at a cross road. Where do you want to go?")
direction = input("Type 'left' or 'right': ").lower()
if direction == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    action = input("Type 'wait' to wait for a boat or 'swim' to swim across: ").lower()
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door = input("One red, one yellow and one blue. Which colour do you choose? ").lower()
        if door == "red":
            print("It's a room full of fire. Game Over.")
        elif door == "yellow":
            print("You found the treasure! You Win!")
        elif door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")