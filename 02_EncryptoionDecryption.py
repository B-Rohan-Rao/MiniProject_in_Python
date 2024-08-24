alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

direction = input("Type 'e' to encrypt and 'd' to decrypt\n").lower()
if direction != "e" and direction != "d":
    print("Not a valid command")


def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Encrypted message: {cipher_text}")


def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Decrypted message: {output_text}")


text = input("Enter your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "e":
    encrypt(text, shift)
elif direction == "d":
    decrypt(text, shift)
