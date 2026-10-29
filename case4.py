# Case Study 33: Campus Registration Identifier Analyzer

n = int(input("Enter number of student IDs to analyze: "))

for i in range(1, n + 1):
    reg = input("\nEnter Registration ID (Format YYBBBNN, e.g., 26CSE01): ").upper()

    if len(reg) != 7:
        print("Status: INVALID (Length must be 7 characters)")
    else:
        yr = reg[0:2]
        br = reg[2:5]
        num = reg[5:7]

        if yr.isdigit() and br.isalpha() and num.isdigit():
            print("Status         : VALID")
            print("Admission Year : 20" + yr)
            print("Branch Code    :", br)
            print("Student Number :", num)
        else:
            print("Status: INVALID (Format must be 2 digits, 3 letters, 2 digits)")
          
