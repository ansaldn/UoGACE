import cryptography

from cryptography.fernet import Fernet
key = Fernet.generate_key()

file = open('key.key', 'wb')
file.write(key)
file.close()