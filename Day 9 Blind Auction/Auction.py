print("Welcome to the auction program")

participantes = True

dict_particpants = {}
highest_number = 0
the_winner = ""

while participantes:
    name_participant = input("what is your name? ")
    bid = int(input("what is your bid? "))

    dict_particpants[name_participant] = bid
    more_participants = input("are there more participants? ")

    #highest_bid = max(dict_particpants, key=dict_particpants.get)

    for bidder in dict_particpants:
        bid_ammount = dict_particpants[bidder]
        if bid_ammount > highest_number:
            highest_number = bid_ammount

            the_winner = bidder


    if more_participants == "yes":
        print("\n" * 10)
    else:
        print(f"the winner is {the_winner}")
        participantes = False

