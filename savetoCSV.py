import csv
with open('test.csv', newLine='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
