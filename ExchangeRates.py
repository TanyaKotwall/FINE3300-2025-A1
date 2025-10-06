# Question 2:
# Client wants an ExchangeRates class to read a Bank of Canada Exchange Rate file and calculate currency conversions between USD and CAD.
# The class uses pandas and reads the latest available USD/CAD exchange rate from the CSV file.
# It provides a public method to convert a user-specified amount between currencies.

# Attributes of the ExchangeRates class: filename (CSV file name), usd_cad_rate (latest rate)
# Public Method: convert
#                takes an amount and two currency codes ('USD' or 'CAD') as parameters
#                returns the converted amount using the latest exchange rate
# Assumes the CSV file is formatted correctly and located in the right file path location and ensure pandas is installed.

# Pandas is used to read and process the exchange rate CSV file
import pandas as pd

class ExchangeRates:
    def __init__(self, filepath):
        """Initialize ExchangeRates and load the latest USD/CAD exchange rate."""
        self.filepath = filepath
        # Read only the USD/CAD column and get the most recent value (last row)
        self.usd_cad_rate = pd.read_csv(filepath, usecols=['USD/CAD']).iloc[-1].iloc[-1]

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount between USD and CAD using the latest rate and round to 2 decimal places."""
        from_currency = from_currency.strip().upper()
        to_currency = to_currency.strip().upper()

        if from_currency == "USD" and to_currency == "CAD":
            return round(amount * self.usd_cad_rate, 2)
        elif from_currency == "CAD" and to_currency == "USD":
            return round(amount / self.usd_cad_rate, 2)
        else:
            raise ValueError("Only USD and CAD conversions are supported.")

# --- Program starts here ---
if __name__ == "__main__":
    print("Bank of Canada Exchange Rate Converter")
    print("--------------------------------------")

    # Edit to match the full path to your CSV file
    filepath = r"C:\Users\Owner\OneDrive - York University\Documents\FINE 3300\BankOfCanadaExchangeRates.csv"

    # Creates ExchangeRates object and displays latest rate
    exchange = ExchangeRates(filepath)
    print(f"Latest USD/CAD rate from file: {exchange.usd_cad_rate}")

    amount = float(input("\nEnter amount ($): "))
    from_curr = input("From currency (USD or CAD): ")
    to_curr = input("To currency (USD or CAD): ")

    # Performs the currency conversion and displays result
    converted = exchange.convert(amount, from_curr, to_curr)
    print(f"Converted amount: ${converted} {to_curr.upper()}")