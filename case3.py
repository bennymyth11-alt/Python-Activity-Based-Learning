# Case Study 18: Fuel Consumption and Route Comparison

dist = float(input("Enter journey distance (km): "))
price = float(input("Enter fuel price per liter (Rs): "))
n = int(input("Enter number of vehicles to compare: "))

min_cost = 9999999.0
best_veh = ""

for i in range(1, n + 1):
    print("\n--- Vehicle", i, "---")
    v_name = input("Enter vehicle name: ")
    mil = float(input("Enter mileage (km/l): "))
    res = float(input("Enter reserve fuel required (liters): "))

    fuel_needed = (dist / mil) + res
    trip_cost = fuel_needed * price

    print("Total Fuel Needed:", round(fuel_needed, 2), "L | Trip Cost: Rs.", round(trip_cost, 2))

    if trip_cost < min_cost:
        min_cost = trip_cost
        best_veh = v_name

print("\n=== Best Option ===")
print("Lowest-Cost Vehicle :", best_veh)
print("Minimum Journey Cost: Rs.", round(min_cost, 2))
