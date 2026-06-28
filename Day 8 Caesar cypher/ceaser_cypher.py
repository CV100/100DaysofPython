alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("do you want to encrypt or decrypt? ")

def direction_ (direct):
    if direct == "encrypt":
        message = input("what is your message? ").lower()

        displacement = int(input("what displacement do you want to have? write a number: "))
        encrypter(message, displacement)

    elif direct == "decrypt":
        unmessage = input("what is the message to decode?: ")

        undisplacement = int(input("what is the number?: "))
        decrypter(unmessage, undisplacement)



def encrypter (msg, displ):
    encrypted_word = ""
    for mens in list(msg):
        position_number = (alphabet.index(mens))

        position_number += displ

        if position_number > len(alphabet):
            position_number = position_number - len(alphabet)

        encrypted_word += alphabet[position_number]

    print(encrypted_word)




def decrypter(unmsg, undispl):
    unmessaging = list(unmsg)
    the_word = ""

    for letter in unmessaging:
        if letter in alphabet:

            pos_num = (alphabet.index(letter))

            undisplacing = pos_num - undispl

            if undisplacing > len(alphabet):
                undisplacing % len(alphabet)

            the_word += alphabet[undisplacing]
    print(the_word)

direction_(direction)