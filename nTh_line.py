import csv
import itertools

print("filename?")
filename = input()
print("keep first lines? How many? (enter number)")
keepLines = int(input())
print("keep each nTh line. n= ?")
nTh = int(input())
with open(filename, 'r', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=';')

    with open(filename + '_short', 'w', newline='') as csvWriteFile:
        writer = csv.writer(csvWriteFile, delimiter=';')

        for _ in range(keepLines):
            writer.writerow(next(reader))

        for row in itertools.islice(reader, 0, None, nTh):
            writer.writerow(row)
