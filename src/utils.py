import csv


class CSVReader:
    # default constructor
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_csv_file(self):
        with open(self.file_name, "r") as file:
            # reader object that reads the csv file line by line
            reader = csv.reader(file)
            return list(reader)