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
    reader = csv.reader(csvfile, delimiter=',')  # Vesszővel tagolt fájl
    data = list(reader)  # Minden sort beolvasunk

print("Beolvasott adatok:", data)  # Ellenőrzés céljából kiírjuk a beolvasott adatokat

# Eredmények tárolása dictionaryben
results = {}

# Feldolgozás soronként
for i in range(len(data) - num_of_rows):
    # Ellenőrizzük, hogy van-e elég elem a sorban
    if len(data[i]) < 2:
        print(f"Átugrott üres vagy hiányos sor: {data[i]}")
        continue  # Ha nincs, ugorjuk át ezt a sort

    # Az aktuális sor második eleme
    try:
        current_value = float(data[i][1])
        print(f"A(z) {i + 1}. sor második eleme: {current_value}")  # Debug print
    except ValueError:
        print(f"Hiba történt a {i + 1}. sorban található érték konvertálása során: {data[i][1]}")
        continue  # Hibás érték esetén ugorjuk át ezt a sort

    values_to_divide = []

    # Először osztás az aktuális sor többi elemével
    for k in range(2, len(data[i])):  # Az aktuális sor második elemétől kezdve
        try:
            divided_value = current_value / float(data[i][k])
            rounded_value = round(divided_value, precision)
            values_to_divide.append(str(rounded_value))
            print(f"Osztás eredménye (aktuális sor {i+1}, oszlop {k+1}): {rounded_value}")  # Debug print
        except (ValueError, ZeroDivisionError) as e:
            print(f"Hiba történt az osztás során: {e}")
            continue  # Hibás érték vagy 0-val való osztás esetén ugorjuk át ezt az osztást

    # Majd osztás a következő sorok második elemével
    for j in range(i + 1, min(i + 1 + num_of_rows, len(data))):
        for k in range(1, len(data[j])):
            try:
                divided_value = current_value / float(data[j][k])
                rounded_value = round(divided_value, precision)
                values_to_divide.append(str(rounded_value))
                print(f"Osztás eredménye (sor {i+1} / sor {j+1}, oszlop {k+1}): {rounded_value}")  # Debug print
            except (ValueError, ZeroDivisionError) as e:
                print(f"Hiba történt az osztás során: {e}")
                continue  # Hibás érték vagy 0-val való osztás esetén ugorjuk át ezt az osztást

    # Hash érték generálása az eredményekből
    combined_string = ','.join(values_to_divide)
    print(f"Kombinált string a hash-hez (sor {i+1}): {combined_string}")  # Debug print
    hash_object = hashlib.sha256(combined_string.encode())
    hash_value = hash_object.hexdigest()

    # Eredmények tárolása a dictionary-ben
    date_key = data[i][0]
    results[date_key] = hash_value
    print(f"Hash érték (sor {i+1}): {hash_value}")  # Debug print

# Eredmények kiíratása
print("Eredmények:")
for date, hash_val in results.items():
    print(f"{date}: {hash_val}")