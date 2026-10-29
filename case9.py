# Case Study 53: Food Waste Monitoring System

days = int(input("Enter number of days to monitor: "))
limit = float(input("Enter acceptable wastage percentage limit (e.g., 10): "))

high_waste_days = []

for d in range(1, days + 1):
    print("\n--- Day", d, "---")
    prep = int(input("Enter meals prepared: "))
    serv = int(input("Enter meals served: "))

    leftover = prep - serv
    waste_pct = (leftover / prep) * 100

    print("Leftover Meals:", leftover, "| Wastage:", round(waste_pct, 2), "%")

    if waste_pct > limit:
        print("Warning: Wastage exceeded acceptable limit!")
        high_waste_days.append(d)

print("\n=== Monitoring Summary ===")
print("Days Exceeding Acceptable Wastage Limit:", high_waste_days)
