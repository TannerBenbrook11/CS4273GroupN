import pandas as pd
import re

# Initialize a list to store data for each section
sections = []

# Open and read the file
with open("cpu_info.txt", "r") as file:
    lines = file.readlines()

    # Initialize variables to track the current section
    current_section = {}
    section_name = None

    for line in lines:
        # Check for section headers (e.g., c001, c002)
        # this regex matches lines that start with a 'c' followed by one or more digits
        if re.match(r'^c\d+$', line.strip()):
            # Save the current section (if it exists)
            # and the current_section is not empty
            # if the current_section is finished, then append it to the sections list
            # and reset the current_section to an empty dictionary
            if current_section:
                sections.append((section_name, current_section))
                current_section = {}  # Reset for the next section

            # Set the name of the new section
            section_name = line.strip()

        # Skip lines that are just dashes or empty
        elif re.match(r'^-+$', line.strip()) or line.strip() == '':
            continue

        # Process key-value pairs and add it to the current section
        elif ':' in line:
            key, value = line.split(':', 1)
            current_section[key.strip()] = value.strip()

    # Add the last section (if it exists)
    if current_section:
        sections.append((section_name, current_section))

# Convert the list of sections into a DataFrame
rows = []
for section_name, section_data in sections:
    for key, value in section_data.items():
        rows.append([section_name, key, value])

# Create a DataFrame from the list of rows
df = pd.DataFrame(rows, columns=["Section", "Key", "Value"])

# Save the DataFrame to a CSV file
df.to_csv("formatted_cpu_info.csv", index=False)