# P = principle amount
# r = monthly rate of interest
# n = no.of months

car_principle_amount = 604870 
annual_rate_of_interest  = 9
monthly_rate_of_interest = (annual_rate_of_interest / 100) / 12 
no_of_months = int(input("Enter Number of Months: "))

car_emi = (car_principle_amount *  monthly_rate_of_interest *  (1 + monthly_rate_of_interest)**no_of_months)/ ((1 + monthly_rate_of_interest)**no_of_months - 1)

print(f"Monthly EMI for the car is: {car_emi}")