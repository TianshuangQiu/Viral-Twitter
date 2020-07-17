import os
import csv
import time

f = open("Data/recovery_7_17.txt")

data = []
buffer = []
for line in f:

    if line.__contains__("GATHERING DATA"):
        data.append(buffer)
        buffer = []
        table = line.split("'")
        # collecting items from the cases csv
        buffer.append((table[1]))
        buffer.append((table[3]))
        buffer.append((table[5]))
        buffer.append((table[7]))
        buffer.append((table[9]))

    elif line.__contains__("Finished:"):
        buffer.append(line.split(" ")[4])
        #time.sleep(1)


with open(os.path.join("Data/States/", "00PROCESSED" + "Florida.csv"), "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)