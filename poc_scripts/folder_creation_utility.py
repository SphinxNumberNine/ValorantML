import os

file = open("labels.txt")
for line in file.readlines():
    os.mkdir("./test_dataset/" + line.lower().strip())
