import pandas as pd
import re

def parse_power_data(lines):
    # Initialize a dictionary to store the data
    data = {'CPU': [], 'Metric': [], 'Value': [], 'Unit': []}

    # Regular expression to match the key-value pairs
    pattern = re.compile(r'^(c\d+):\s*#?(.*?)=(.*?)(?:\s*\|\s*(.*))?$')

    # Iterate through the lines and extract the data
    for line in lines:
        match = pattern.match(line.strip())
        if match:
            cpu = match.group(1)
            metric = match.group(2).strip()
            value = match.group(3).strip()
            unit = match.group(4).strip() if match.group(4) else None

            # Handle cases where the unit is embedded in the value (e.g., "1468 btu/hr")
            if unit is None and re.search(r'\d+\s+\w+/\w+', value):
                # Split the value into value and unit
                value, unit = re.split(r'\s+', value, maxsplit=1)

            # Regex to check whether the value column holds a numeric value
            value_check = re.compile(r'\d+')

            # Regex to check if the value column contains a number followed by W
            value_check_2 = re.compile(r'\d+\s*W')

            # Only add to the DataFrame if the Value field is populated and matches the criteria
            if value and value_check.search(value) and value_check_2.search(value):
                data['CPU'].append(cpu)
                data['Metric'].append(metric)
                data['Value'].append(value)
                data['Unit'].append(unit)

    # Convert the dictionary to a DataFrame
    return pd.DataFrame(data)

# Main script
if __name__ == "__main__":
    with open("CS_power_info.txt", "r") as file:
        lines = file.readlines()
        df = parse_power_data(lines)
        print(df.head(40))