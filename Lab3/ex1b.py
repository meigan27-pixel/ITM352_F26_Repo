from cryptography.fernet import Fernet

key = Fernet.generate_key()
cypherSuite = Fernet(key)

encodedText = cypherSuite.encrypt(b"Hello, World!")
print("Encoded text:", encodedText)
decodedText = cypherSuite.decrypt(encodedText)
print("Decoded text:", decodedText)
