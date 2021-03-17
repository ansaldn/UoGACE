import csv
import cryptography

#Usually instead of 'txt' we should have the data being passed from the base or moonBuggy
text = "Hello World"

from cryptography.fernet import Fernet
text.encode()
f = Fernet(key)
encrypted = f.encrypt(text)

with open('data.csv', 'w', newline='') as file:
    #reader = csv.reader(f)
    writer = csv.writer(file)
    writer.writerow(text)
file.close()

