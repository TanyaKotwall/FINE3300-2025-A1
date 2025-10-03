# Question 1: Mortgage Payments
# This class computes mortgage payments under different frequencies
# using a quoted semi-annually compounded interest rate (Canadian convention).
# Payment options include: monthly, semi-monthly, bi-weekly, weekly,
# rapid bi-weekly, and rapid weekly.

import math

class MortgagePayment:
    def __init__(self, rate_percent, years):
        # Initialize the mortgage with interest rate (%) and amortization period (years)
        self.rate = rate_percent / 100.0   # convert percentage to decimal
        self.years = years

    def _annuity_factor(self, r, n):
        # Present Value of Annuity Factor (PVA)
        # Formula: (1 - (1 + r)^-n) / r
        return (1 - (1 + r)**(-n)) / r

    def payments(self, principal):
        # Step 1: Convert quoted semi-annual rate to Effective Annual Rate (EAR)
        i_sa = self.rate / 2.0                 # semi-annual rate
        EAR = (1 + i_sa)**2 - 1                # effective annual rate

        results = []

        # Step 2: Calculate periodic payments for each frequency
        # Monthly (12), Semi-Monthly (24), Bi-Weekly (26), Weekly (52)
        for m in (12, 24, 26, 52):
            r = (1 + EAR)**(1/m) - 1           # periodic rate
            n = m * self.years                 # total number of payments
            pmt = principal / self._annuity_factor(r, n)
            results.append(round(pmt, 2))      # round to 2 decimal places

        # Step 3: Add Rapid payment options (based on monthly payment)
        monthly = results[0]
        results.append(round(monthly / 2, 2))   # rapid bi-weekly
        results.append(round(monthly / 4, 2))   # rapid weekly

        # Return all payments as a tuple
        return tuple(results)

# Execution starts here
if __name__ == "__main__":
    # Prompt user for input values
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    years = int(input("Enter the amortization period: "))

    # Create MortgagePayment object
    mortgage = MortgagePayment(rate, years)

    # Compute all payment options
    payments = mortgage.payments(principal)

    # Display results in required format
    print(f"Monthly Payment: ${payments[0]:.2f}")
    print(f"Semi-Monthly Payment: ${payments[1]:.2f}")
    print(f"Bi-Weekly Payment: ${payments[2]:.2f}")
    print(f"Weekly Payment: ${payments[3]:.2f}")
    print(f"Rapid Bi-Weekly Payment: ${payments[4]:.2f}")
    print(f"Rapid Weekly Payment: ${payments[5]:.2f}")