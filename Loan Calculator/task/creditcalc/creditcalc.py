import math

print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")

action = input()

if action == "n":
    print("Enter the loan principal:")
    loan_amount = int(input())
    print("Enter the monthly payment:")
    monthly_payment = float(input())
    print("Enter the loan interest")
    loan_interest = float(input())

    interest_rate = loan_interest / (12 * 100)

    n_months = math.ceil(math.log(monthly_payment / (monthly_payment - interest_rate
                                                     * loan_amount),
                                  1 + interest_rate))

    if n_months == 1:
        print("It will take 1 month to repay this loan!")
    elif n_months < 12:
        print(f"It will take {n_months} months to repay this loan!")
    elif n_months % 12 == 0:
        print(f"It will take {n_months // 12} years to repay this loan!")
    else:
        print(f"It will take {n_months // 12} years and "
              f"{n_months % 12} months to repay this loan!")

elif action == "a":
    print("Enter the loan principal:")
    loan_amount = int(input())
    print("Enter the number of periods:")
    n_months = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())

    interest_rate = loan_interest / (12 * 100)

    monthly_payment = math.ceil(loan_amount * ((interest_rate * (interest_rate + 1) ** n_months)
                                               / ((1 + interest_rate) ** n_months - 1)))

    print(f"Your monthly payment = {monthly_payment}!")

elif action == "p":
    print("Enter the annuity payment:")
    monthly_payment = float(input())
    print("Enter the number of periods:")
    n_months = int(input())
    print("Enter the loan interest:")
    loan_interest = float(input())

    interest_rate = loan_interest / (12 * 100)

    loan_amount = monthly_payment / ((interest_rate * (1 + interest_rate) ** n_months)
                                     / ((1 + interest_rate) ** n_months - 1))

    print(f"Your loan principal = {loan_amount}!")
