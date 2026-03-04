import string


plain_alphabet = string.ascii_lowercase
cipher_alphabet = "qwertyuiopasdfghjklzxcvbnm"

def encrypt(text):
    result = ""
    for char in text.lower():
        if char in plain_alphabet:
            index = plain_alphabet.index(char)
            result += cipher_alphabet[index]
        else:
            result += char
    return result

def decrypt(text):
    result = ""
    for char in text.lower():
        if char in cipher_alphabet:
            index = cipher_alphabet.index(char)
            result += plain_alphabet[index]
        else:
            result += char
    return result


message = input("Enter plaintext: ")

encrypted = encrypt(message)
decrypted = decrypt(encrypted)

print("Encrypted text:", encrypted)
print("Decrypted text:", decrypted)
