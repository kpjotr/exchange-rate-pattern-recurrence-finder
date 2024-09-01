#!/usr/bin/env python3
#
# file: Erprf_hashtable_maker.py
# project: Exchange rate pattern recurrence finder
# created: 2024. 09. 01.
# author: Pjotr 975
# pjotr957@gmail.com

import csv
import hashlib

# Felhasználói bemenetek
file_path = 'Munkalap3.csv'  # CSV fájl elérési útja
num_of_rows = 3  # Felhasználó által megadott sorok száma
precision = 4  # Kerekítés pontossága

# CSV fájl beolvasása
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    data = list(reader)

print(data)
print(type(data))

# Eredmények tárolása dictionaryben
results = {}

# Feldolgozás soronként
for i in range(len(data)): # lépdelünk a data sorain, de 3-al a vége előttig!
    # Az aktuális sor második eleme
    current_value = float(data[i][1])
    values_to_divide = []

    # Az osztások végrehajtása a következő sorok második elemével
    for j in range(i + 1, min(i + 1 + num_of_rows, len(data))):
        for k in range(1, len(data[j])):
            divided_value = current_value / float(data[j][k])
            print(float(data[j][k]))
            rounded_value = round(divided_value, precision)
            values_to_divide.append(str(rounded_value))

    # Hash érték generálása az eredményekből
    combined_string = ','.join(values_to_divide)
    hash_object = hashlib.sha256(combined_string.encode())
    hash_value = hash_object.hexdigest()

    # Eredmények tárolása a dictionary-ben
    date_key = data[i][0]
    results[date_key] = hash_value

# Eredmények kiíratása
for date, hash_val in results.items():
    print(f"{date}: {hash_val}")

