import csv


def write_file(s, data):
    with open('Data/States/' + s + ".csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow(row)


data = []

with open("Data/us-states.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    for row in reader:
        data.append(row)

my_list = []
used_list = []
for row in data:
    if not row[2] in used_list:
        used_list.append(row[2])
        for inner_row in data:
            if inner_row[2] == row[2]:
                my_list.append(inner_row)
        write_file(row[2], my_list)
        print("WRITING", row[2])

    my_list.clear()
