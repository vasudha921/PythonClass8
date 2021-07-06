import csv


with open ("SOCR-HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
newData = []
for i in range (len(file_data)):
    n_num = file_data[i][1]
    newData.append(float(n_num))

n = len(newData)
total = 0

for a in newData:
    total += a
    
mean = total/n
print(mean)
