# Case Study 45: Weekly Electricity Consumption Matrix

n = int(input("Enter number of appliances: "))
limit = float(input("Enter weekly consumption limit per appliance (units): "))

grid = []

for i in range(n):
    print("\nEnter 7 days readings for Appliance", i + 1, ":")
    row = []
    for d in range(7):
        u = float(input("  Day " + str(d + 1) + " units: "))
        row.append(u)
    grid.append(row)

print("\n--- Appliance-Wise Weekly Totals ---")
for i in range(n):
    app_tot = 0.0
    for d in range(7):
        app_tot = app_tot + grid[i][d]

    if app_tot > limit:
        print("Appliance", i + 1, "Total:", app_tot, "units [EXCEEDED LIMIT!]")
    else:
        print("Appliance", i + 1, "Total:", app_tot, "units [Within Limit]")

print("\n--- Day-Wise Total Consumption ---")
for d in range(7):
    day_tot = 0.0
    for i in range(n):
        day_tot = day_tot + grid[i][d]
    print("Day", d + 1, "Total:", day_tot, "units")
  
