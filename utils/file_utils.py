import csv
def read_names_from_csv(filename):
    """Reads the first column of a CSV file and returns a list of names."""
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        new_colleagues = []
        for line in reader:
            new_colleagues.append(line[0])
    return new_colleagues