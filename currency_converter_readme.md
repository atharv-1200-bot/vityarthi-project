# Currency Converter

## Project Title
**Simple Currency Converter - Python CLI Application**

## Overview of the Project
This is a simple command-line currency converter application built with Python. The program allows users to convert amounts between different currencies using pre-defined exchange rates. It provides a user-friendly interface where users can select source and target currencies, enter an amount, and instantly get the converted value along with the exchange rate.

The application is lightweight, requires no external dependencies, and runs entirely offline using a built-in dictionary of exchange rates.

## Features
- ✅ **Simple and Easy to Use**: Clean command-line interface with clear prompts
- ✅ **Multiple Currency Support**: Supports 10 major world currencies including USD, EUR, GBP, INR, JPY, AUD, CAD, CHF, CNY, and AED
- ✅ **Accurate Conversion**: Uses mathematical conversion through USD as base currency
- ✅ **Exchange Rate Display**: Shows the current exchange rate between selected currencies
- ✅ **Input Validation**: Validates currency codes and amount inputs
- ✅ **No Internet Required**: Works completely offline with built-in exchange rates
- ✅ **Zero Dependencies**: No external libraries needed - uses only Python standard library

## Technologies/Tools Used
- **Programming Language**: Python 3.x
- **Development Approach**: Procedural Programming
- **Interface**: Command Line Interface (CLI)
- **Data Storage**: Dictionary-based exchange rate storage

## Steps to Install & Run the Project

### Prerequisites
- Python 3.x installed on your system
- No additional libraries required

### Installation Steps

1. **Clone or Download the Project**
   - Download the currency_converter.py file to your computer
   - Or clone the repository if available

2. **Navigate to Project Directory**
   - Open terminal or command prompt
   - Navigate to the folder containing the project file

3. **Verify Python Installation**
   - Check if Python is installed on your system
   - Open terminal and type: python --version
   - Or try: python3 --version

### Running the Project

1. **Run the Program**
   - Open terminal in the project directory
   - Type: python currency_converter.py
   - Press Enter
   
   **Or if using Python 3 specifically:**
   - Type: python3 currency_converter.py
   - Press Enter

2. **Follow the On-Screen Prompts**
   - View the list of available currencies
   - Enter source currency code (e.g., USD, INR, EUR)
   - Enter target currency code (e.g., GBP, JPY, AUD)
   - Enter the amount you want to convert
   - View the conversion result and exchange rate

### Example Usage

```
==================================================
        CURRENCY CONVERTER
==================================================

Available currencies:
  - USD
  - EUR
  - GBP
  - INR
  - JPY
  - AUD
  - CAD
  - CHF
  - CNY
  - AED

Enter source currency: USD
Enter target currency: INR
Enter amount in USD: 100

==================================================
100.0 USD = 8312.00 INR
Exchange Rate: 1 USD = 83.1200 INR
==================================================
```

## Customization

### Updating Exchange Rates
You can update the exchange rates in the get_exchange_prices() function by editing the dictionary values with current market rates.

### Adding New Currencies
Simply add new currency codes and their rates (relative to USD) in the exchange rates dictionary within the program file.

## Project Structure
```
currency-converter/
│
├── currency_converter.py    # Main program file
└── README.md                # Project documentation
```

## License
This project is open source and available for educational purposes.

## Author
Created as a simple demonstration of Python programming concepts.

---

**Note**: Exchange rates are approximate and should be updated regularly for accurate conversions. For production use, consider integrating with a live exchange rate API.