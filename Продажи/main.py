import csv 

with open('SalesJan2009.csv', newline='') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    print(row[4])