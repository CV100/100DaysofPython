import random
import ascii_drawings

user_input = input("Enter your choice: ")

paper_choice = ascii_drawings.paper
rock_choice = ascii_drawings.rock
scissors_choice = ascii_drawings.scissors

if user_input == "rock":
 user_input = rock_choice
 print(ascii_drawings.rock)
elif user_input == "paper":
 user_input = paper_choice
 print(ascii_drawings.paper)
elif user_input == "scissors":
 user_input = paper_choice
 print(ascii_drawings.scissors)



computer_choice = random.choice(ascii_drawings.rps_drawings)

print(computer_choice)

if computer_choice == user_input:
    print("You draw!")
elif computer_choice == ascii_drawings.rock and user_input == paper_choice:
    print("You loose!")
elif computer_choice == ascii_drawings.rock and user_input == scissors_choice:
    print("You win!")
elif computer_choice == ascii_drawings.paper and user_input == rock_choice:
    print("You loose!")
elif computer_choice == ascii_drawings.paper and user_input == scissors_choice:
    print("You win!")
elif computer_choice == ascii_drawings.scissors and user_input == rock_choice:
    print("You win!")
elif computer_choice == ascii_drawings.scissors and user_input == paper_choice:
    print("You loose!")
