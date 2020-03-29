def ex3(file):
    return sum(float(line.split(" ")[-1]) for line in file)


print("Całkowita liczba bajtów: ")
print(ex3(open("test.txt")))
