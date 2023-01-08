logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(raw_text, shift_num, direction_choice):
    cipher_text = ""

    if direction_choice == "decode":
        shift_num *= -1
    
    for char in raw_text:
        # if there is a space then space should just get appended, otherwise error as ' ' is not in alphabet list
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_num) % 26 #if new_position over 26, remainder is the new_position
            cipher_text += alphabet[new_position]    
        else:
            cipher_text += char

    print(f"The {direction_choice}d text is {cipher_text}")
    
print(logo)
play_again = True

while play_again:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 #debugging for shifts that are higher than 26 positions
    
    caesar_cipher(raw_text = text, shift_num = shift, direction_choice = direction)
    
    loop = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if loop == "no":
        play_again = False
        print("Goodbye")

