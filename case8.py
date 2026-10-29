# Case Study 51: Bus Passenger Occupancy Simulation

cap = int(input("Enter maximum bus seating capacity: "))
stops = int(input("Enter number of bus stops: "))

p_cnt = 0
viol_cnt = 0

for s in range(1, stops + 1):
    print("\n--- Stop", s, "---")
    board = int(input("Enter passengers boarding: "))
    alight = int(input("Enter passengers alighting: "))

    p_cnt = p_cnt + board - alight
    if p_cnt < 0:
        p_cnt = 0

    print("Passengers in bus at Stop", s, ":", p_cnt)

    if p_cnt > cap:
        extra = p_cnt - cap
        print("ALERT: Capacity Violation! Overloaded by", extra, "passengers.")
        viol_cnt = viol_cnt + 1

print("\n=== Simulation Summary ===")
print("Final Passengers on Bus   :", p_cnt)
print("Total Capacity Violations :", viol_cnt)
