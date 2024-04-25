alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input('What is your text:\n').lower()
shift=int(input('Type shift Number\n'))
direction = input('encode or decode?\n')


def ceaser(start_text,shift_amount,intended_direction):
    text_result=''
    if intended_direction == 'decode': ###
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position +  shift_amount
        text_result+=alphabet[new_position]
    print(f'The {intended_direction}d text is {text_result}')

ceaser(start_text=text,shift_amount=shift,intended_direction=direction)





# def encrypt(plain_text,shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f'the new encoded text is {cipher_text}')
#
#
#
# def decrypt(ciphered_text,shift_amount):
#     decipher_text = ''
#     for letter in ciphered_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         decipher_text += new_letter
#     print(f'the new decoded text is {decipher_text}')
#
# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(ciphered_text=text, shift_amount=shift)
