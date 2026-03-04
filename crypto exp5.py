import math

# Encryption
def affine_encrypt(text, a, b):
    result = ""
    for char in text.upper():
        if char.isalpha():
            p = ord(char) - ord('A')
            c = (a * p + b) % 26
            result += chr(c + ord('A'))
        else:
            result += char
    return result


# Decryption
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def affine_decrypt(cipher, a, b):
    result = ""
    a_inv = mod_inverse(a, 26)

    for char in cipher.upper():
        if char.isalpha():
            c = ord(char) - ord('A')
            p = (a_inv * (c - b)) % 26
            result += chr(p + ord('A'))
        else:
            result += char
    return result


text = input("Enter plaintext: ")
a = int(input("Enter key a: "))
b = int(input("Enter key b: "))

if math.gcd(a, 26) != 1:
    print("Invalid key 'a'. It must be coprime with 26.")
else:
    cipher = affine_encrypt(text, a, b)
    plain = affine_decrypt(cipher, a, b)

    print("Encrypted text:", cipher)
    print("Decrypted text:", plain)
