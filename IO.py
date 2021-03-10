import csv
import matplotlib
import sys

environment = []

f = open('in.csv', newline='')
#Note that the correct directory must be navigated to else the full file path will be needed
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader: # A list of rows
    rowlist = []
    for value in row: # A list of value
     rowlist.append(value)
     environment.append(rowlist)
     print(value) # Floats




matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
f.close() # Don't close until you are done with the reader;
        # the data is read on request.
        
