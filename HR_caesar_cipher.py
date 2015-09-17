import string


def caesar_cipher(msg, rotator):
    alphabet = string.lowercase
    new_msg = ""
    for letter in msg:
        if letter in string.punctuation:
            new_msg += letter
        elif letter in string.digits:
            new_msg += letter
        else:
            upper = False
            if letter.isupper():
                upper = True
            letter = letter.lower()
            orig_index = alphabet.index(letter)
            new_index = orig_index + rotator
            if new_index > 25:
                new_index = new_index % 26
            letter = alphabet[new_index]
            if upper:
                letter = letter.upper()
            new_msg += letter
    return new_msg

string_length = raw_input()
msg = raw_input()
rotator = int(raw_input())

print caesar_cipher(msg, rotator)
