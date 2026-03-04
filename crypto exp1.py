def caesar_encrypt(text, k):
    result = ""

    for char in text:
        if char.isalpha():
            shift = k % 26

            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char

    return result


def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)


text = input("Enter the message: ")
k = int(input("Enter shift value (1-25): "))

encrypted = caesar_encrypt(text, k)
decrypted = caesar_decrypt(encrypted, k)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
