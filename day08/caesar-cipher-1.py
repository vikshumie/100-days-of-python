alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(raw_text, shift_num):
    encrypted = ""
    
    for letter in raw_text:
        # if there is a space then space should just get appended, otherwise error as ' ' is not in alphabet list
        if letter != ' ':
            position = alphabet.index(letter)
            new_position = position + shift_num
            if new_position > 25:
                new_position -= 26 # minus 26 as this includes 0 as well
            encrypted += alphabet[new_position]
        else:
            encrypted += letter
            
    print(f"The encoded text is {encrypted}")

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypt(text, shift)