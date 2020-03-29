def ex1():
    m = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]
    m = [row.split(" ") for row in m]
    m = [[row[i] for row in m] for i in range(len(m[0]))]
    m = [" ".join(row) for row in m]
    print(m)


ex1()
