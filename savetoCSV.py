import csv

#Usually instead of 'txt' we should have the data being passed from the base or moonBuggy
text = "Hello World"

with open('data.csv', 'w', newline='') as file:
    #reader = csv.reader(f)
    writer = csv.writer(file)
    writer.writerow(text)
file.close()
