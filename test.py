def table(data):
    maxl = 0
    for r in range(len(data[0])): maxl = maxl + max(len(str(row[r])) for row in data)
    for row in data:
        i = 0
        print("─" * (maxl + len(data[0]) * 2 + 1) + "\b")
        for cell in row:
            maxw = max(len(str(row[i])) for row in data)
            print("|" + str(cell) + " " * (maxw - len(str(cell))), end=" ")
            i += 1
            if i == len(data[0]):
                print("|" + "\b")
    print("─" * (maxl + len(data[0]) * 2 + 1) + "\b")

d = [(1, 'r', 'Resistor'), (2, 'c', 'Capacitator'), (3, 'ld', 'LED')]

table(d)