from math import ceil

print("Enter the loan principal:")

loan_amount = int(input())

print("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")

action = input()

if action == "m":
    print("Enter the monthly payment:")
    monthly_payment = int(input())

    n_months = round(loan_amount / monthly_payment)
    if n_months == 1:
        print(f"It will take {n_months} month to repay the loan")
    else:
        print(f"It will take {n_months} months to repay the loan")

elif action == "p":
    print("Enter the number of months:")
    n_months = int(input())
    payment = ceil(loan_amount / n_months)
    if loan_amount % n_months != 0:
        last_payment = loan_amount - (n_months - 1) * payment
        print(f"Your monthly payment = {payment} and the last payment = {last_payment}.")
    else:
        print(f"Your monthly payment = {payment}")
