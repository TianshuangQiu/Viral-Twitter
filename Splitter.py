import csv


def write(s, data):
    with open('Data/Sorted/' + s + ".csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow(row)


with open("Data/us-counties.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    my_list = ["NOT DATA"]
    for row in reader:
        if row[0] != my_list[-1][0]:
            print(row[0])
            write(my_list[-1][0], my_list)
            my_list.clear()
            my_list.append(["NOT DATA"])
        my_list.append(row)


