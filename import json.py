import json
import re
import pandas as pd

def find_ips(input_string):
    # Simple IP address regex pattern
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    ips = re.findall(ip_pattern, input_string)
    return ips

# Collect all IP addresses in a list
all_ips = []

# Open the json file and read each line as a separate json object
with open(r"path_to_your_file.json", 'r') as f:
    for line in f:
        data = json.loads(line)
        for key, value in data.items():
            if isinstance(value, str):  # if the value is a string
                all_ips.extend(find_ips(value))
            elif isinstance(value, list):  # if the value is a list
                for item in value:
                    if isinstance(item, str):
                        all_ips.extend(find_ips(item))

# Convert the IP addresses into a pandas DataFrame
df = pd.DataFrame(all_ips, columns=['IP Addresses'])

# Write the DataFrame to an Excel file
df.to_excel(r"path_to_your_file.xlsx", index=False)
