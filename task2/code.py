# Progressive Electricity Billing System

# Electricity slab rates
SLAB1 = 3.00       # 0-100 units
SLAB2 = 5.00       # 101-200 units
SLAB3 = 7.00       # 201-300 units
SLAB4 = 10.00      # Above 300 units

# Fixed charges and percentages
FIXED_CHARGE = 50
SURCHARGE_RATE = 5
REBATE_RATE = 5

# Function to calculate electricity charges
def calculate_bill(units):

    if units <= 100:
        energy_charge = units * SLAB1

    elif units <= 200:
        energy_charge = (100 * SLAB1) + \
                        ((units - 100) * SLAB2)

    elif units <= 300:
        energy_charge = (100 * SLAB1) + \
                        (100 * SLAB2) + \
                        ((units - 200) * SLAB3)

    else:
        energy_charge = (100 * SLAB1) + \
                        (100 * SLAB2) + \
                        (100 * SLAB3) + \
                        ((units - 300) * SLAB4)

    # Add fixed charges
    subtotal = energy_charge + FIXED_CHARGE

    # Calculate surcharge
    surcharge = subtotal * SURCHARGE_RATE / 100

    # Calculate rebate
    rebate = subtotal * REBATE_RATE / 100

    # Final bill
    total_bill = subtotal + surcharge - rebate

    return energy_charge, surcharge, rebate, total_bill


# Main program
months = []

n = int(input("Enter number of months: "))

for i in range(n):

    print("\nMonth", i + 1)

    month = input("Enter month name: ")
    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units! Enter a non-negative value.")
        continue

    energy, surcharge, rebate, bill = calculate_bill(units)

    months.append({
        "month": month,
        "units": units,
        "energy": energy,
        "surcharge": surcharge,
        "rebate": rebate,
        "bill": bill
    })


# Display monthly bills
print("\n========== ELECTRICITY BILL REPORT ==========")

for data in months:

    print("\nMonth:", data["month"])
    print("Units Consumed:", data["units"])
    print("Energy Charges: Rs.", round(data["energy"], 2))
    print("Fixed Charges: Rs.", FIXED_CHARGE)
    print("Surcharge: Rs.", round(data["surcharge"], 2))
    print("Rebate: Rs.", round(data["rebate"], 2))
    print("Final Bill: Rs.", round(data["bill"], 2))


# Calculate total bill
total = sum(data["bill"] for data in months)

print("\nTotal Electricity Bill: Rs.", round(total, 2))


# Compare monthly bills
print("\n========== MONTHLY BILL COMPARISON ==========")

for i in range(1, len(months)):

    previous = months[i - 1]["bill"]
    current = months[i]["bill"]

    if previous == 0:
        increase = 0
    else:
        increase = ((current - previous) / previous) * 100

    print("\n", months[i - 1]["month"],
          "to", months[i]["month"])

    print("Bill Change:", round(increase, 2), "%")

    if increase > 30:
        print("WARNING: Unusual increase detected!")
    else:
        print("Normal bill variation.")


print("\n========== END OF REPORT ==========")

