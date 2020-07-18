import csv

# path to the file we are editing
path = "Data/States/00PROCESSEDArizona.csv"

# file to keep the data when the stream closes
storage = []

# opening the file and reading it, the stream closes when the operation concludes
with open(path, newline='') as csvfile:
    """
    reads the data and calculates the daily cases by subtracting the last one from before
    """
    reader = csv.reader(csvfile, delimiter=',')
    data = []
    for row in reader:
        data.append(row)

    data = data[1:]

    for x in range(0, data.__len__()):
        p = str(data[x][3])
        print(int(str(data[x][3])))
        cases_holder = int(str(data[x][3]))
        deaths_holder =int(str(data[x][4]))
        for i in range(0, x):
            # subtrating previous deaths
            cases_holder -= int(str(data[i][3]))
            deaths_holder -= int(str(data[i][4]))

        rowx = data[x]
        print(row)
        rowx[3] = cases_holder
        rowx[4] = deaths_holder
        storage.append(rowx)

with open("Output/COMPLETE_AZ.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in storage:
        writer.writerow(row)
