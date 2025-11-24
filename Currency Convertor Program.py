def get_exchange_rates():
    """Returns a dictionary of exchange rates relative to USD"""
    return {
        'USD': 1.0,      # US Dollar
        'EUR': 0.92,     # Euro
        'GBP': 0.79,     # British Pound
        'INR': 83.12,    # Indian Rupee
        'JPY': 149.50,   # Japanese Yen
        'AUD': 1.52,     # Australian Dollar
        'CAD': 1.36,     # Canadian Dollar
        'CHF': 0.88,     # Swiss Franc
        'CNY': 7.24,     # Chinese Yuan
        'AED': 3.67,     # UAE Dirham
    }

def convert_currency(amount, from_currency, to_currency, rates):
    """Convert amount from one currency to another"""
    if from_currency not in rates or to_currency not in rates:
        return None
    
    # Convert to USD first, then to target currency
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    
    return converted_amount

def display_available_currencies(rates):
    """Display all available currencies"""
    print("\nAvailable currencies:")
    for currency in rates.keys():
        print(f"  - {currency}")

def main():
    rates = get_exchange_rates()
    
    print("=" * 50)
    print("        CURRENCY CONVERTER")
    print("=" * 50)
    
    display_available_currencies(rates)
    
    # Get user input
    from_curr = input("\nEnter source currency: ").upper()
    to_curr = input("Enter target currency: ").upper()
    
    # Validate currencies
    if from_curr not in rates:
        print(f"\nError: {from_curr} is not available!")
        return
    
    if to_curr not in rates:
        print(f"\nError: {to_curr} is not available!")
        return
    
    try:
        amount = float(input(f"Enter amount in {from_curr}: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    
    # Convert currency
    result = convert_currency(amount, from_curr, to_curr, rates)
    
    if result is not None:
        print("\n" + "=" * 50)
        print(f"{amount} {from_curr} = {result:.2f} {to_curr}")
        
        # Calculate and show exchange rate
        rate = rates[to_curr] / rates[from_curr]
        print(f"Exchange Rate: 1 {from_curr} = {rate:.4f} {to_curr}")
        print("=" * 50)
    else:
        print("\nError: Could not convert currency.")

if __name__ == "__main__":
    main()
