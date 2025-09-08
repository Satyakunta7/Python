import random

generated_otp = random.randint(1000,9999)

print(generated_otp)

#checking no.of attempts
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_entered_otp = int(input("Please enter the 4 digit otp: "))
    
    #checking for OTP
    if generated_otp == user_entered_otp:
        print("Transaction Success")
        break
    else:
        attempts +=1
        print(f"Incorrect otp. Attempts left: {max_attempts - attempts}" )

if attempts == max_attempts:
    print("Maximum Attempts Reached, try after 24 Hours")




