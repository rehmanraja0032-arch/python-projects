"""Caesar Cipher
Encrypts or decrypts a message by shifting every letter by a number of places.
Example: decrypt "Pbhentr vf sbhaq va hayvxryl cynprf." with shift 13.
"""


def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


print('=== Caesar Cipher ===')
mode = input('Encrypt or decrypt? (e/d): ').strip().lower()
message = input('Message: ')
shift = int(input('Shift (1-25): '))

if mode == 'e':
    result = encrypt(message, shift)
    print('Encrypted message:', result)
elif mode == 'd':
    result = decrypt(message, shift)
    print('Decrypted message:', result)
else:
    print('Invalid choice. Please type e or d.')

input('\nPress Enter to close...')