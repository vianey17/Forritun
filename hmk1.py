# Write a Python program that allows the user to input 
# a principal amount for a loan and then prints out information
# about the individual payments. 
# The loan has a given face value and monthly
# interest rate and is paid back in equal monthly
# installments.
# You should only use the methods/material discussed in Chapters 0-2
# Note the following items:
#
# 1. The monthly loan payment is always at most $50, and includes
# the principal payment and interest.
#
# 2. Allow the user to input the face value (in $). However, you can
# assume that the user will always input an amount < $2500.
#
#  3. The interest rate should vary such that if the amount borrowed is 
# <= $1000 the rate is 1.5% per month, else 2.0% per month. Note, however,
# that the interest rate is fixed during the lifetime of the loan.
# 
# 4. For each payment, the program should output the month number, the total
# amount paid and the interest paid for the month, and the remainder of the loan.
# 
# 5. All float numbers should be written out with at most two digits after
# the decimal point. You should use the built-in Python function
# round() for this purpose.

principle = float(input('Input the cost of the item in dollars: $'))
apr = float(0)
interest = float(0)
balance = principle + interest
month = int(0)
payment = 0
t_interest = 0

if principle >= 2500:
    print('Please enter an amount under $2500')

elif principle <= 0:
    print("You can't borrow $0 or under, you silly goose.")

else: 
    while balance > 0:
                
        month += 1
        interest = round(balance * apr,2) 
        if principle <= 1000:
            apr = 1.5/100
        else:
            apr = 2/100
        if balance >= 50:
            payment = 50
        else:
            payment = balance + interest
            balance = 0
        
        if balance != 0:
            balance = round(balance + interest - payment,2)       
             
        print("Month: ", month, "Payment: ", payment, "Interest paid: $", interest, "Remaining debt: $", balance)
        
        t_interest = round(t_interest + interest,2)
    if balance <= 0:
        print("Number of months: ", month, "Total interest paid: ", t_interest)
