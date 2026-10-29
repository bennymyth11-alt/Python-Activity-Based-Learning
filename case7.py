# Case Study 49: Tuple-Based Product Catalogue Audit

n = int(input("Enter number of products: "))
catalogue = []

for i in range(n):
    print("\n--- Product", i + 1, "---")
    pid = input("Enter Product ID: ").upper()
    price = float(input("Enter Unit Price: "))
    stock = int(input("Enter Stock Quantity: "))
    catalogue.append((pid, price, stock))

total_val = 0.0
invalid_items = []
replenish_items = []

print("\n--- Product Audit Details ---")
for i in range(n):
    pid, price, stock = catalogue[i]

    if price <= 0 or stock < 0:
        print(pid, "-> INVALID RECORD (Price:", price, ", Stock:", stock, ")")
        invalid_items.append(pid)
    else:
        item_val = price * stock
        total_val = total_val + item_val
        print(pid, "-> Inventory Value: Rs.", item_val)

        if stock < 10:
            replenish_items.append(pid)

print("\n=== Catalogue Summary ===")
print("Total Valid Inventory Value : Rs.", total_val)
print("Invalid Product Records     :", invalid_items)
print("Items Needing Replenishment :", replenish_items)
