import csv


# Map machine types to power draw divisor
machine_type_map = {
    "dell-5580": 1,
    "dell-6580": 1000,
    "dell-7580": 100
}

class Normalizer:    
    def read_csv_file(self):
        content = []
        with open(self.file_name, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                content.append(row)
        return content
    
    def normalize_power_draw(self, csv_content):
        # Normalize the power draw values
        for row in csv_content[1:]:
            machine_type = row[1]
            power_draw = int(row[2])
            # Check if this entry is a machine type we know about
            if machine_type in machine_type_map:
                # if it is, normalize the power draw value by dividing it by the divisor
                row[2] = str(power_draw // machine_type_map[machine_type])

        # return the updated content
        return csv_content