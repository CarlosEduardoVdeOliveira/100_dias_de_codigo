
import csv
import os

with open('D:\\www\\codiacademy\\Dia 09\\sales','r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
