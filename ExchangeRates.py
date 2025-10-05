# Question 3:
# Client wants an ExchangeRates class to read a Bank of Canada Exchange Rate file and calculate currency conversions between USD and CAD.
# The class reads the latest available USD/CAD exchange rate from the CSV file.
# It provides a public method to convert a user-specified amount between currencies.

# Attributes of the ExchangeRates class: filename (CSV file name), rate (latest USD/CAD rate)
# Public Method: convert
#                takes an amount and two currency codes ('USD' or 'CAD') as parameters
#                returns the converted amount using the latest exchange rate
# Assumes the CSV file is formatted correctly and located in the right file path location.
import csv

class ExchangeRates:
    def __init__(self, filename):
        # Store the filename and load the rate on initialization
        self.filename = filename
        self.usd_cad_rate = None
        self._read_file()

    def _read_file(self):
        """Read the CSV file and get the latest USD/CAD exchange rate"""
        with open(self.filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)

            # Header row
            header = rows[0]

            # Find the column index for "USD/CAD"
            usd_index = header.index("USD/CAD")

            # Walk backwards to find the last valid row with a value
            last_row = None
            for row in reversed(rows[1:]):  # skip header
                if row[usd_index].strip():
                    last_row = row
                    break

            # Save the exchange rate (1 USD = usd_cad_rate CAD)
            self.usd_cad_rate = float(last_row[usd_index])

    def convert(self, amount, from_currency, to_currency):
        """Convert between USD and CAD using the latest rate"""
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()

        if from_currency == "USD" and to_currency == "CAD":
            return round(amount * self.usd_cad_rate, 2)
        elif from_currency == "CAD" and to_currency == "USD":
            return round(amount / self.usd_cad_rate, 2)
        else:
            raise ValueError("Only USD and CAD conversions are supported.")

# Execution starts here
if __name__ == "__main__":
    # Full path to your CSV file
    filename = r"C:\Users\Owner\OneDrive - York University\Documents\FINE 3300\BankOfCanadaExchangeRates.csv"
    
    # Create ExchangeRates object
    rates = ExchangeRates(filename)
    print(f"Latest USD/CAD rate from file: {rates.usd_cad_rate}")

    # Prompt user
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (USD or CAD): ")
    to_curr = input("To currency (USD or CAD): ")

    try:
        converted = rates.convert(amount, from_curr, to_curr)
        print(f"Converted amount: {converted} {to_curr.upper()}")
    except ValueError as e:
        print(e)