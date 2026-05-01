base_income: float = float(input("Enter your yearly income: "))
tax_rate: float = float(input("Enter the tax rate: ")) / 100
taxed: float = base_income * tax_rate

print("=" * 40)
print("Income Tax Calculator")
print("=" * 40)
print(f"Yearly Income: ${base_income:,.2f}")
print(f"Yearly Income (double): ${base_income * 2:,.2f}")
print(f"Yearly Income (half): ${base_income / 2:,.2f}")
print(f"Tax Rate: {tax_rate * 100:.2f}%")
print("-" * 40)
print(f"Taxed Amount: ${taxed:,.2f}")
print(f"Taxed Amount (double): ${taxed * 2:,.2f}")
print(f"Taxed Amount (half): ${taxed / 2:,.2f}")