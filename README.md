# FINE3300-2025-AI
This repository is for Assignment 1 in FINE3300 course which contains code in Python using Visual Studio Code for Canadian Home Mortgage Payments class and Bank of Canada Currency Exchange Rates class.   

## Contents
### Mortgage Payments
`MortgagePayments.py` This project implements a **MortgagePayment** class that calculates mortgage payments for Canadian home loans under different payment frequencies. It converts a quoted annual interest rate (with semi-annual compounding) into an effective annual rate, then computes payments using the **Present Value of an Annuity (PVA)** formula. This tool can be reused across various home mortgages requiring standardized mortgage payment calculations.

The program prompts the user for 3 key inputs and returns the corresponding mortgage payments for different frequencies

**Users:**
- Principal amount ($)
- Interest rate (%)
- Amortization period (years)

**Outputs:**
- Monthly
- Semi-Monthly
- Bi-Weekly
- Weekly
- Rapid Bi-Weekly
- Rapid Weekly  

### Exchange Rates
`ExchangeRates.py` This project implements an **ExchangeRates** class that reads a **Bank of Canada Exchange Rate CSV file** and converts between USD and CAD currencies. The class extracts the most recent USD/CAD exchange rate from the file and applies it to user-entered amounts.

**User Inputs:**
- Amount to convert
- Source currency (USD or CAD)
- Target currency (USD or CAD)

**Outputs:**
Converted amount in the target currency, formatted to two decimal places.

### README File
`README.md` This file describes two parts of the project, a Mortgage Payments class and an Exchange Rates class.

