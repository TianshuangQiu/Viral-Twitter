import csv


def write(s, data):
    """
    writes data to file with name s
    """
    # console output so i don't get scared
    print("PRINTING", s)
    with open('Data/Counties/' + s + ".csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            writer.writerow(row)


with open("Data/us-counties.csv", newline='') as csvfile:
    """
    searches for the data until it reaches the end of the file
    """
    reader = csv.reader(csvfile, delimiter=',')
    my_list = []
    full_file = []
    used_list = []
    for row in reader:
        full_file.append(row)

    for line in full_file:
        # finds a new target
        if not line[1] in used_list:
            used_list.append(line[1])
            # searches the entire file for that target
            for other_line in full_file:
                if other_line[1] == line[1]:
                    my_list.append(other_line)
            # writes and clears list
            write(line[1], my_list)
            my_list.clear()
