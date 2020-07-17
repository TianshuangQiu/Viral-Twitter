import csv

# path to the file we are editing
path = ""

# file to keep the data when the stream closes
storage = []

# opening the file and reading it, the stream closes when the operation concludes
with open("path", newline='') as csvfile:
    """
    reads the data and calculates the daily cases by subtracting the last one from before
    """
    reader = csv.reader(csvfile, delimiter=',')
    data = []
    for row in reader:
        data.append(row)

    for x in (0, data.__len__()):
        cases_holder = int(data[x][3])
        deaths_holder = int(data[x][4])
        for i in (0, x):
            # subtrating previous deaths
            cases_holder -= int(data[i][3])
            deaths_holder -= int(data[i][4])

        row = [data[x]]
        row[3] = cases_holder
        row[4] = deaths_holder
        storage.append(row)

with open("NEWcsv.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in storage:
        writer.writerow(row)
