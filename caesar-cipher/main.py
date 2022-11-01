from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount)%26
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")


# # # # # # # # # # # # # # # # # # # # # # # # #
print(f"\u001b[33m{logo}\u001b[0m")

restart = True
while restart == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift%26 == 0:
      print("-Number must not be multiple of 26 or you're going to get the same message.\n")
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    answer = input("Do you want to restart the program? (y/n) \n")
    if answer == "n":
      restart = False
      print("GoodBye :)")
