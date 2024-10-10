import unicodedata
import random
import string
text = '1 B X'

RANGE_ALPHA = 26
RANGE_NUMBER = 10

def encrypt(message):

    encrypted_message = ''
    normalized_message = ''.join(unicodedata.normalize('NFD', char) for char in message)
    ascii_message = normalized_message.encode('ascii', 'ignore').decode('utf-8')

    key = random.randint(1, RANGE_ALPHA - 1)
    if key > RANGE_NUMBER:
        str_key = str(key)
        key_number = key - 10 * int(str_key[0])
    else:
        key_number = key

    for letter in ascii_message:
        if letter.isspace() or letter in string.punctuation:
            encrypted_message += letter
        elif letter.isalpha():
            if ord(letter.upper()) + key > ord('Z'):
                encrypted_message += chr(ord(letter) + key - RANGE_ALPHA)
            else:
                encrypted_message += chr(ord(letter) + key)
        else:
            if ord(letter) + key_number > ord('9'):
                encrypted_message += chr(ord(letter) - key_number + RANGE_NUMBER)
            else:
                encrypted_message += chr(ord(letter) + key_number)

    return encrypted_message, key, key_number


def decipher(encrypted_message, decipher_alpha, decipher_number):

    decipher_message = ''
    for letter in encrypted_message:
        if letter.isspace() or letter in string.punctuation:
            decipher_message += letter
        elif letter.isalpha():
            if ord(letter.upper()) - decipher_alpha < ord('A'):
                decipher_message += chr(ord(letter) + RANGE_ALPHA - decipher_alpha)
            else:
                decipher_message += chr(ord(letter) - decipher_alpha)
        else:
            if ord(letter) - decipher_number < ord('1'):
                decipher_message += chr(ord(letter) + RANGE_NUMBER - decipher_number)
            else:
                decipher_message += chr(ord(letter) - decipher_number)

    return decipher_message

print(f'Original message: {text}\n')

encrypted_tupla = encrypt(text)
print(f'Encrypted message: {encrypted_tupla[0]}\nKey: {encrypted_tupla[1]}')

decipher_text = decipher(encrypted_tupla[0], encrypted_tupla[1], encrypted_tupla[2])
print(f'\nDecipher message: {decipher_text}')
