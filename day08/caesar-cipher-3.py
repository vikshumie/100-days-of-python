def caesar(raw_text, shift_num, direction_choice):
    cipher_text = ""
    
    for letter in raw_text:
        # if there is a space then space should just get appended, otherwise error as ' ' is not in alphabet list
        if letter != ' ':
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift_num
                if new_position > 25:
                    new_position -= 26 # minus 26 as this includes 0 as well
                cipher_text += alphabet[new_position]
            else:
                new_position = position - shift_num
                if new_position < 1:
                    new_position += 26 #e.g. a is 0, z is 25
                cipher_text += alphabet[new_position]
     
        else:
            cipher_text += letter

    print(f"The {direction_choice}d text is {cipher_text}")
    

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

play_again = True

while play_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(raw_text = text, shift_num = shift, direction_choice = direction)
    
    loop = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if loop == "no":
        play_again = False
    else:
        play_again = True
    

