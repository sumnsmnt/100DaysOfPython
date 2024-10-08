#################### Caesar Cipher #####################
# Go through all the steps written below for better understanding
###################### Final Code ######################

from art import logo, alphabet
print(logo)

def caesar(start_text, shift_number, direction_choice):
    end_text = ""
    if direction_choice == "decode":
        shift_number *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_number
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {direction_choice}d text is {end_text}")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    shift = shift % 26
    
    caesar(start_text=text, shift_number=shift, direction_choice=direction)

    result = input("Type 'yes' if you want to do it again, otherwise type 'no'")
    if result == "no":
        should_continue = False
        print("Good Bye")


# Go through all 4 steps for better understading
# I have written down how do I approch to solve the problem


# ############### Step 1 ###############

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

# text = input("Type your message: ").lower()
# shift = int(input("Type the shift number: "))

# # Todo 1: Create a function called 'encrypt' that takes the text and 'shift' as inputs.
# def encrypt(plain_text, shift_number):
#     cipher_text = ""
#
#     # Todo 2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the
#     # 'alphabet' by the 'shift' amount and print the encrypted text.
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_number
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(cipher_text)


# # Todo 3: Call the 'encrypt' function and pass in the user inputs. You should be able to
# # test the code and 'encrypt' a message.
# encrypt(plain_text=text, shift_number=shift)


# ############### Step 2 ###############

# # Fixed 'list index out of range' issue by adding 1 more set of alphabets
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z',
#             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

# # Added a option for user, now they can do encode and decode
# direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
# text = input("Type your message: ").lower()
# shift = int(input("Type the shift number: "))

# def encrypt(plain_text, shift_number):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_number
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(cipher_text)
# # Todo 1: Create a function called decrypt that takes the text and shift as inputs.
# def decrypt(cipher_text, shift_number):
#     plain_text = ""
#     # Todo 2: Inside the decrypt function, shift each letter of the text backwards
#     # in the alphabet by the shift number and print the decrypted text
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_number
#         plain_text += alphabet[new_position]
#     print(plain_text)

# # Todo 3: Check if the user wanted to encrypt or decrypt the message by checking the direction
# # variable. Then call the correct function based on that direction variable. You should be 
# # able to test the code to encrypt and decrypt a message.
# if direction == "encode":
#     encrypt(plain_text=text, shift_number=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_number=shift)
# else:
#     print("Please give the right input")


# ############### Step 3 ###############

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z',
#             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

# direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
# text = input("Type your message: ").lower()
# shift = int(input("Type the shift number: "))

# # Todo 1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# def caesar(start_text, shift_number, direction_choice):
#     end_text = ""
#     if direction_choice == "decode":
#         shift_number *= -1
#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_number
#         end_text += alphabet[new_position]
#     print(f"The {direction_choice}d text is {end_text}")

# # Todo 2: Call the caesar() function, passing over the text, shift and direction values.
# caesar(start_text=text, shift_number=shift, direction_choice=direction)


# ############### Step 4 ###############

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z',
#             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#             'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

# def caesar(start_text, shift_number, direction_choice):
#     end_text = ""
#     if direction_choice == "decode":
#         shift_number *= -1
#     for char in start_text:
#         # Todo 3: What happens if the user enters a number/symbol/space?
#         # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_number
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#     print(f"The {direction_choice}d text is {end_text}")

# # Todo 1: Import and print the logo from art.py when program starts.
# from art import logo
# print(logo)

# # Todo 4: Can you figure out a way to ask the user if they want to restart the cipher program?
# # e.g. Type 'yes' if you want to go again, otherwise type 'no'
# # If they type 'yes' then ask then call the caesor funtion again.
# # We have to create a new funtion that calls itself if they type 'yes'
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt and 'decode' to decrypt: ")
#     text = input("Type your message: ").lower()
#     shift = int(input("Type the shift number: "))

#     # Todo 2: What if the user enter a shift that is greater than the number of letters in the
#     # alphabet? We can fix that using modulus %
#     shift = shift % 26
#     caesar(start_text=text, shift_number=shift, direction_choice=direction)

#     result = input("Type 'yes' if you want to do it again, otherwise type 'no'")
#     if result == "no":
#         should_continue = False
#         print("Good Bye")