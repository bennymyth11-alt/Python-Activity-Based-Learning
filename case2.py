# Case Study 12: Attendance Recovery Computation

att = int(input("Enter classes attended so far: "))
tot = int(input("Enter total classes held so far: "))
thresh = float(input("Enter required attendance percentage (e.g., 75): "))

curr_pct = (att / tot) * 100
print("\nCurrent Attendance Percentage:", round(curr_pct, 2), "%")

if curr_pct >= thresh:
    print("Status: You are already eligible! Minimum extra classes needed: 0")
else:
    extra = 0
    while ((att + extra) / (tot + extra)) * 100 < thresh:
        extra = extra + 1

    new_pct = ((att + extra) / (tot + extra)) * 100
    print("Minimum consecutive classes needed:", extra)
    print("Attendance after attending", extra, "classes:", round(new_pct, 2), "%")
  
