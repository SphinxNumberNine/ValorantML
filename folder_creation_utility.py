import os

file = open("labels.txt")
for line in file.readlines():
    os.mkdir("./dataset/" + line.lower().strip())
