# Tuition Fee Discount Program

# Take inputs
student_name = input("Enter Student Name: ")
grade_level = int(input("Enter Grade Level: "))
is_topper = input("Is the student an Academic Topper? (Yes/No): ")
base_fee = float(input("Enter Base Tuition Fee: "))

# Base discount based on grade and topper
discount_percentage = 0

if grade_level >= 9 and grade_level <= 12:
    if is_topper == "yes":
        discount_percentage = 20
    else:
        discount_percentage = 10
elif grade_level >= 6 and grade_level <= 8:
    discount_percentage = 5
else:
    discount_percentage = 0

# Additional discounts
if grade_level == 10:
    discount_percentage += 3
elif grade_level == 12:
    discount_percentage += 5

# Calculating discount amount and final fee
discount_amount = (discount_percentage / 100) * base_fee
final_fee = base_fee - discount_amount

print(f"Student Name: {student_name}")
print(f"Grade Level: {grade_level}")
print(f"Academic Topper: {'Yes' if is_topper == 'yes' else 'No'}")
print(f"Base Tuition Fee: {base_fee:.2f}")
print(f"Total Discount Percentage: {discount_percentage}%")
print(f"Discount Amount Saved: {discount_amount:.2f}")
print(f"Final Tuition Fee after Discount: {final_fee:.2f}")
