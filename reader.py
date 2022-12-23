import csv

# flights

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open("./flights.csv", 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get the total number of rows
    print("Total no. of rows: %d" % csvreader.line_num)

# printing the field names
print('Field details are:' + ', '.join(field for field in fields))

print('\nThe rows are:\n')
for row in rows:
    # parsing each column of a row
    for col in row:
        print("%10s" % col, end=" "),
    print('\n')

ncol = len(fields)

# aeroports

with open("./aeroports.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    next(reader, None)  # skip the headers
    read_airports = [row for row in reader]

print(read_airports)
print(fields)
print(ncol)


"""
with open("./flights.csv") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    next(reader, None)  # skip the headers
    read_flights = [row for row in reader]

print(read_flights)
"""
