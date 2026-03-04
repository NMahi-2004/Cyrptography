def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    cipher = ""
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            cipher_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            cipher += cipher_char
            key_index += 1
        else:
            cipher += char

    return cipher


def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plain = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            plain_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plain += plain_char
            key_index += 1
        else:
            plain += char

    return plain


text = input("Enter plaintext: ")
key = input("Enter key: ")

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)
