import json
import re
import pandas as pd

def find_ips(input_string):
    # Basit bir IP adresi regex deseni
    ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
    ips = re.findall(ip_pattern, input_string)
    return ips

# Tüm IP adreslerini bir liste içinde toplamak için
all_ips = []

# json dosyasını aç ve her satırı ayrı bir json nesnesi olarak oku
with open(r"C:\Users\erene\Desktop\shodanip.json", 'r') as f:
    for line in f:
        data = json.loads(line)
        for key, value in data.items():
            if isinstance(value, str):  # değer bir string ise
                all_ips.extend(find_ips(value))
            elif isinstance(value, list):  # değer bir liste ise
                for item in value:
                    if isinstance(item, str):
                        all_ips.extend(find_ips(item))

# IP adreslerini bir pandas DataFrame'ine dönüştür
df = pd.DataFrame(all_ips, columns=['IP Adresleri'])

# DataFrame'i bir Excel dosyasına yaz
df.to_excel(r"C:\Users\erene\Desktop\ip_adresleri.xlsx", index=False)
