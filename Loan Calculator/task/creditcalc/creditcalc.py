import math
import argparse

parser = argparse.ArgumentParser(description="This program is a Loan calculator")

parser.add_argument("--type")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--payment")

args = parser.parse_args()
type_of_loan = args.type
loan_amount = args.principal
monthly_payment = args.payment
loan_interest = args.interest
n_months = args.periods


def verify_parameters(type_of_loan_arg, loan_amount_arg, monthly_payment_arg, loan_interest_arg, n_months_arg):
    if type_of_loan_arg != "annuity" and type_of_loan_arg != "diff" or not type_of_loan_arg:
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
    if a < 4:
        return False

    return True


if verify_parameters(type_of_loan, loan_amount, monthly_payment, loan_interest, n_months):

    missing_parameter = ""

    if not loan_amount:
        missing_parameter = "loan amount"
        monthly_payment = float(monthly_payment)
        loan_interest = float(loan_interest)
        n_months = int(n_months)
    elif not monthly_payment:
        missing_parameter = "monthly payment"
        loan_amount = float(loan_amount)
        loan_interest = float(loan_interest)
        n_months = int(n_months)
    elif not n_months:
        loan_amount = float(loan_amount)
        loan_interest = float(loan_interest)
        monthly_payment = float(monthly_payment)
        missing_parameter = "n months"

    if type_of_loan == "annuity":

        if missing_parameter == "n months":

            interest_rate = loan_interest / (12 * 100)
            n_months = math.ceil(math.log(monthly_payment / (monthly_payment - interest_rate
                                                             * loan_amount),
                                          1 + interest_rate))

            overpayment = monthly_payment * n_months - loan_amount

            if n_months == 1:
                print("It will take 1 month to repay this loan!\n"
                      f"Overpayment = {overpayment}")
            elif n_months < 12:
                print(f"It will take {n_months} months to repay this loan!\n"
                      f"Overpayment = {overpayment}")
            elif n_months % 12 == 0:
                print(f"It will take {n_months // 12} years to repay this loan!\n"
                      f"Overpayment = {overpayment}")
            else:
                print(f"It will take {n_months // 12} years and "
                      f"{n_months % 12} months to repay this loan!\n"
                      f"Overpayment = {overpayment}")

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

        if missing_parameter == "monthly payment":
            interest_rate = loan_interest / (12 * 100)
            overpayment = 0
            for i in range(0, n_months):
                i += 1
                payment = math.ceil(loan_amount / n_months + interest_rate * (loan_amount - ((loan_amount * (i - 1)) / n_months)))
                print(f"Month {i}: payment is {payment}")
                overpayment += payment
            overpayment -= loan_amount
            print(f"Overpayment = {round(overpayment)}")

else:
    print("Incorrect parameters")
