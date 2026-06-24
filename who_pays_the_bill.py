import random

participants = ["Roswaldo", "hipolito", "Gertrudis", "Asurbanipal", "Consagración"]

randomizer = random.randint(0, (len(participants) - 1))

the_payer = participants[randomizer]

print(the_payer + " pays the bill")

