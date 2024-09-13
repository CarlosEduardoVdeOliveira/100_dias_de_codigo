
import csv
import os
#D:\\www\\codiacademy\\Dia 09\\

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
