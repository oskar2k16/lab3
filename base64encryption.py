import base64

def encrypt_message(message):
    encoded_message = base64.b64encode(message.encode())
    return encoded_message.decode()

def decrypt_message(encrypted_message):
    decrypt_result = base64.b64decode(encrypted_message).decode()
    return decrypt_result

example_message = "Base64test"
print("Before base64 encrypted message:", example_message)
encoded_message = encrypt_message(example_message)
print("Encrypted message by base64:", encoded_message)
decoded_message = decrypt_message(encoded_message)
print("Decrypted text:", decoded_message)








