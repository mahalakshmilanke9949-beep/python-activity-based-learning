
# Hospital Billing and Patient Classification System

# Fixed consultation fee
CONSULTATION_FEE = 500

# Function to calculate hospital bill
def calculate_bill(age, consultations, diagnostic, treatment):

    # Calculate consultation charges
    consultation_charge = consultations * CONSULTATION_FEE

    # Calculate total charges
    total = consultation_charge + diagnostic + treatment

    # Apply conditional concession
    if age >= 60:
        concession = total * 15 / 100
    else:
        concession = 0

    # Calculate final bill
    final_bill = total - concession

    return consultation_charge, total, concession, final_bill


# Function to classify patient
def classify_patient(amount):

    if amount < 5000:
        return "Low Payment Category"

    elif amount <= 15000:
        return "Medium Payment Category"

    else:
        return "High Payment Category"


# Main program
print("===== HOSPITAL BILLING SYSTEM =====")

# Enter patient details
patient_id = input("Enter Patient ID: ")
patient_name = input("Enter Patient Name: ")

age = int(input("Enter Patient Age: "))

consultations = int(input("Enter Number of Consultations: "))

diagnostic = float(input("Enter Diagnostic Charges: Rs. "))

treatment = float(input("Enter Treatment Charges: Rs. "))


# Validate billing constraints
if age <= 0:
    print("Invalid Age!")

elif consultations < 0:
    print("Invalid Number of Consultations!")

elif diagnostic < 0 or treatment < 0:
    print("Charges cannot be negative!")

else:

    # Calculate bill
    consultation, total, concession, final_bill = calculate_bill(
        age, consultations, diagnostic, treatment
    )

    # Classify patient
    category = classify_patient(final_bill)

    # Display bill
    print("\n===== HOSPITAL BILL DETAILS =====")

    print("Patient ID:", patient_id)
    print("Patient Name:", patient_name)
    print("Patient Age:", age)

    print("\nConsultation Charges: Rs.", consultation)
    print("Diagnostic Charges: Rs.", diagnostic)
    print("Treatment Charges: Rs.", treatment)

    print("\nTotal Charges: Rs.", total)
    print("Concession: Rs.", concession)
    print("Final Bill Amount: Rs.", final_bill)

    print("\nPatient Classification:", category)

    print("\n===== BILL GENERATED SUCCESSFULLY =====")
