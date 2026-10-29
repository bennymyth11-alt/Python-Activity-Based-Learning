# Case Study 8: Manufacturing Cost and Profitability Analysis

mat = float(input("Enter material cost: "))
lab = float(input("Enter labour charges: "))
wast = float(input("Enter wastage cost: "))
mach = float(input("Enter machine cost: "))
sell = float(input("Enter total selling price: "))
target = float(input("Enter profit target: "))

total_cost = mat + lab + wast + mach
profit = sell - total_cost

print("\n--- Profitability Report ---")
print("Total Production Cost :", total_cost)
print("Selling Price         :", sell)
print("Actual Profit / Loss  :", profit)

if profit >= target:
    print("Status: Profit target MET successfully!")
elif profit > 0:
    shortfall = target - profit
    print("Status: Profit made, but BELOW target by:", shortfall)
else:
    print("Status: Production resulted in a LOSS.")
  
