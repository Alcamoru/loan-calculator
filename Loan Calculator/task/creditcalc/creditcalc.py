import math
import argparse

parser = argparse.ArgumentParser("This program is a Loan calculator")
parser.add_argument("-t", "--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()


def verify_parameters(type_of_loan_arg, loan_amount_arg, monthly_payment_arg, loan_interest_arg, n_months_arg):
    if type_of_loan_arg != "annuity" or type_of_loan_arg != "diff" or not  type_of_loan_arg:
        return False
    elif type_of_loan_arg == "diff" and monthly_payment_arg:
        return False
    elif not loan_interest_arg:
        return False
    required_args = [type_of_loan_arg, loan_amount_arg, monthly_payment_arg, loan_interest_arg, n_months_arg]
    a = 0
    for i in required_args:
        if i is not None:
            a += 1
    print(a)
    if a < 4:
        return False

    return True


type_of_loan = args.type
loan_amount = args.principal
monthly_payment = args.payment
loan_interest = args.interest
n_months = args.periods

if verify_parameters(type_of_loan, loan_amount, monthly_payment, loan_interest, n_months):

    missing_parameter = ""

    if not loan_amount:
        missing_parameter = "loan amount"
    elif not monthly_payment:
        missing_parameter = "monthly payment"
    elif not n_months:
        missing_parameter = "n months"

    if type_of_loan == "annuity":

        if missing_parameter == "n months":

            interest_rate = loan_interest / (12 * 100)
            n_months = round(math.ceil(math.log(monthly_payment / (monthly_payment - interest_rate
                                                             * loan_amount),
                                          1 + interest_rate)))

            if n_months == 1:
                print("It will take 1 month to repay this loan!")
            elif n_months < 12:
                print(f"It will take {n_months} months to repay this loan!")
            elif n_months % 12 == 0:
                print(f"It will take {n_months // 12} years to repay this loan!")
            else:
                print(f"It will take {n_months // 12} years and "
                      f"{n_months % 12} months to repay this loan!")

        elif missing_parameter == "monthly payment":

            interest_rate = loan_interest / (12 * 100)
            monthly_payment = math.ceil(loan_amount * ((interest_rate * (interest_rate + 1) ** n_months)
                                                       / ((1 + interest_rate) ** n_months - 1)))

            print(f"Your monthly payment = {round(monthly_payment)}!")

        elif missing_parameter == "loan amount":

            interest_rate = loan_interest / (12 * 100)

            loan_amount = monthly_payment / ((interest_rate * (1 + interest_rate) ** n_months)
                                             / ((1 + interest_rate) ** n_months - 1))

            print(f"Your loan principal = {round(loan_amount)}!")

    elif type_of_loan == "diff":

        if not args.payment:

            interest_rate = loan_interest / (12 * 100)

else:
    print("Incorrect parameters")
