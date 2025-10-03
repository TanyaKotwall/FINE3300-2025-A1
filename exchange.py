# Question 2: Read Bank of Canada Exchange Rate File and get USD/CAD,
# then prompt user to convert between USD and CAD using that rate.

import csv   # import CSV module

# Full path and filename of your CSV
filename = r"C:\Users\Owner\OneDrive - York University\Documents\FINE 3300\BankOfCanadaExchangeRates.csv"

with open(filename, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file)       # create CSV reader
    rows = list(reader)             # convert to list so we can index

    # First row is the header row
    header = rows[0]

    # Find the column index for "USD/CAD"
    usd_index = header.index("USD/CAD")

    # Walk backwards through rows to find the last valid row
    last_row = None
    for row in reversed(rows[1:]):  # skip the header
        if row[usd_index].strip():  # check that cell is not empty
            last_row = row
            break

    # Extract and convert the USD/CAD rate (1 USD = usd_cad_rate CAD)
    usd_cad_rate = float(last_row[usd_index])

print(f"Latest USD/CAD rate from file: {usd_cad_rate}")

# ---- Prompt user and convert using the rate printed above ----
amount = float(input("Enter amount: "))
from_curr = input("From currency (USD or CAD): ").strip().upper()
to_curr = input("To currency (USD or CAD): ").strip().upper()

if from_curr == "USD" and to_curr == "CAD":
    converted = round(amount * usd_cad_rate, 2)   # 1 USD = rate CAD
    print(f"Converted amount: {converted} CAD")
elif from_curr == "CAD" and to_curr == "USD":
    converted = round(amount / usd_cad_rate, 2)   # invert the rate
    print(f"Converted amount: {converted} USD")
else:
    print("Only USD and CAD conversions are supported. Please enter USD or CAD.")