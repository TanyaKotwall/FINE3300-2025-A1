# Question 1:
# Clients wants a MortgagePayment class to calculate various mortgage payment options.
# Client wants to use this library across different home mortgages requiring calculations.
# Returns a tuple of (monthly, semi-monthly, bi-weekly, weekly, rapid bi-weekly, rapid weekly) payments.

# Attributes of the MortgagePayment class: interest_rate, years (amortization period).
# Public Method: payments
#                takes principal amount as a parameter
#                returns a tuple of payment amounts under different frequencies using the present value of annuity factor formula
# Assumes values have been validated.
import math

class MortgagePayment:
    def __init__(self, rate_percent, years):
        """Initialize the mortgage with interest rate (%) and amortization period (years)"""
        # convert percentage to decimal
        self.rate = rate_percent / 100.0   
        self.years = years

    def _annuity_factor(self, r, n):
        """PVA = (1 - (1 + r)^-n) / r"""
        return (1 - (1 + r)**(-n)) / r

    def payments(self, principal):
        # Step 1: Convert quoted semi-annual rate to Effective Annual Rate (EAR)
        EAR = (1 + self.rate/2)**2 - 1                
        result = []

        # Step 2: Calculate periodic payments for each frequency
        """Uses a loop to iterate through payment frequencies, Monthly (12), Semi-Monthly (24), Bi-Weekly (26), Weekly (52)"""
        """Computes the corresponding periodic payments using the annuity formula"""
        for freq in (12, 24, 26, 52):
            # periodic rate
            r = (1 + EAR)**(1/freq) - 1     
            # total number of payments
            n = freq * self.years                
            result.append(round(principal / self._annuity_factor(r, n), 2))
            
        # Step 3: Add Rapid payment options (based on monthly payment)
        monthly = result[0]
        # rapid bi-weekly
        result.append(round(monthly / 2, 2))  
        # rapid weekly
        result.append(round(monthly / 4, 2))   

        # Return all payments as a tuple
        return tuple(result)

if __name__ == "__main__":
    # Prompt user for input values
    print("Mortgage Payment Calculator User Input")
    print("--------------------------------------")

    principal = float(input("Enter the principal amount ($): "))
    rate = float(input("Enter the interest rate (%): "))
    years = int(input("Enter the amortization period (Years): "))

    # Create MortgagePayment object and compute all payment options
    mortgage = MortgagePayment(rate, years)
    payments = mortgage.payments(principal)

    # Display results in required format
    print("Mortgage Payment User Output")
    print("----------------------------")

    print(f"Monthly Payment: ${payments[0]:.2f}")
    print(f"Semi-Monthly Payment: ${payments[1]:.2f}")
    print(f"Bi-Weekly Payment: ${payments[2]:.2f}")
    print(f"Weekly Payment: ${payments[3]:.2f}")
    print(f"Rapid Bi-Weekly Payment: ${payments[4]:.2f}")
    print(f"Rapid Weekly Payment: ${payments[5]:.2f}")