def encrypt(text, shift):
    result = ""

    for char in text:
        result += chr(ord(char) + shift)

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        result += chr(ord(char) - shift)

    return result


with open("resource/secret.txt", "r", encoding="utf-8") as file:
    text = file.read()

encrypted = encrypt(text, 3)

with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write(encrypted)

with open("encrypted.txt", "r", encoding="utf-8") as file:
    encrypted_text = file.read()

decrypted = decrypt(encrypted_text, 3)

with open("decrypted.txt", "w", encoding="utf-8") as file:
    file.write(decrypted)

print("Шифрование и расшифровка завершены")