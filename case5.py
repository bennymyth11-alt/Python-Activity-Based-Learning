# Case Study 39: Multi-Stage Examination Eligibility System

name = input("Enter Student Name: ")
att = float(input("Enter Attendance Percentage: "))
lab = input("Is Laboratory Work Completed? (YES/NO): ").upper()
inter = float(input("Enter Internal Assessment Marks (out of 40): "))
fee = input("Is Tuition Fee Cleared? (YES/NO): ").upper()

print("\n--- Eligibility Audit for", name, "---")
eligible = True

if att < 75.0:
    print("- Unmet Condition: Attendance is below 75%")
    eligible = False

if lab != "YES":
    print("- Unmet Condition: Laboratory work is incomplete")
    eligible = False

if inter < 20.0:
    print("- Unmet Condition: Internal marks are below 20")
    eligible = False

if fee != "YES":
    print("- Unmet Condition: Tuition fee is not cleared")
    eligible = False

if eligible == True:
    print("Final Status: ELIGIBLE for the Final Examination.")
else:
    print("Final Status: NOT ELIGIBLE for the Final Examination.")
  
