# Case Study 59: Campus Transport Allocation

cap = int(input("Enter seating capacity per bus: "))
fleet = int(input("Enter total buses available in college fleet: "))
routes = int(input("Enter number of routes: "))

total_unserved = 0

for r in range(1, routes + 1):
    print("\n--- Route", r, "---")
    r_name = input("Enter Route Name: ")
    demand = int(input("Enter passenger demand: "))

    needed = (demand + cap - 1) // cap

    if needed <= fleet:
        alloc = needed
        unserved = 0
        fleet = fleet - alloc
    else:
        alloc = fleet
        served = alloc * cap
        unserved = demand - served
        fleet = 0

    total_unserved = total_unserved + unserved
    print("Route:", r_name, "| Buses Needed:", needed, "| Allocated:", alloc, "| Unserved Passengers:", unserved)

print("\n=== Transport Summary ===")
print("Remaining Buses in Fleet  :", fleet)
print("Total Unserved Passengers :", total_unserved)
