f = open("Data/recovery_7_17.txt")

data = []
for line in f:
    buffer = []
    if line.__contains__("GATHERING"):
        data.append(buffer)
        buffer.clear()
        table = line.split("'")
        # collecting items from the cases csv
        buffer.append((table[1]))
        buffer.append((table[3]))
        buffer.append((table[5]))
        buffer.append((table[7]))
        buffer.append((table[9]))
        print(buffer)