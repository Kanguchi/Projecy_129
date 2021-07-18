import csv

dataset1 = []
dataset2 = []

with open('Star_Data.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open('brownDwarf.csv', 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers1 = dataset1[0]
headers2 = dataset2[0]

data1 = dataset1[1:]
data2 = dataset2[1:]

headers = headers1 + headers2

star_data = []

for index, data_row in enumerate(data1):
    star_data.append(data1[index]+data2[index])

with open("brightest_stars.csv", 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(star_data)