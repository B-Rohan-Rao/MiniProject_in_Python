alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("Type 'e' to encrypt and 'd' to decrypt\n").lower()
if direction != "e" or direction != "d":
    print("Not a valid command") 


def encrypt(orignal_text, shift_amount):
    cipher_text = ""
    for letter in orignal_text:
        shiftted_position = alphabet.index(letter) + shift_amount

        shiftted_position %= len(alphabet)
        cipher_text += alphabet[shiftted_position]
    print(f"{cipher_text}")    

def decrypt(orignal_text, shift_amount):
    output_text = ""
    for letter in orignal_text:
        shiftted_position = alphabet.index(letter) - shift_amount

        shiftted_position %= len(alphabet)
        output_text += alphabet[shiftted_position]
    print(f"{output_text}")


text = input("Enter your Message\n").lower()
shift = int(input("Type the shift number \n"))

if direction == "e":
    encrypt(text, shift)   
elif direction == "d":
    decrypt(text, shift)
    