import csv
import hashlib

# Felhasználói bemenetek
file_path = 'Munkalap3.csv'  # CSV fájl elérési útja
num_of_rows = 3  # Felhasználó által megadott sorok száma
precision = 5  # Kerekítés pontossága

# CSV fájl beolvasása
with open(file_path, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    data = list(reader)
print(data)
print(type(data))