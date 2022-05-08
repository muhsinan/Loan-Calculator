import math
import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()


def loan_principle(payment, interest, periods):
    interest /= 1200
    return math.floor(payment / ((interest * pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1)))


def total_periods(payment, interest, principal):
    interest /= 1200
    return math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))


def total_annuity(principal, interest, periods):
    interest /= 1200
    return math.ceil(principal * (interest * pow((1 + interest), periods)) / (pow((1 + interest), periods) - 1))


def differentiated_payment(principal, periods, interest):
    interest /= 1200
    arr = []
    for i in range(1, periods + 1):
        arr.append(math.ceil(principal / periods + interest * (principal - (principal * (i - 1)) / periods)))
        print("Month " + str(i) + ": payment is " + str(math.ceil(principal / periods + interest * (principal - (principal * (i - 1)) / periods))))
    return sum(arr)


while True:
    if len(sys.argv) <= 4:
        print("Incorrect parameters")
        break
    elif args.interest is None:
        print("Incorrect parameters")
        break
    elif args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        break
    elif args.type == "annuity" and args.payment is None:
        your_payment = total_annuity(int(args.principal), float(args.interest), int(args.periods))
        over_payment = your_payment * int(args.periods) - int(args.principal)
        print(f"Your annuity payment = {your_payment}!")
        print(f"Overpayment = {over_payment}")
        break
    elif args.type == "annuity" and args.principal is None:
        loan = loan_principle(int(args.payment), float(args.interest), int(args.periods))
        over_payment = int(args.payment) * int(args.periods) - loan
        print(f"Your loan principal = {loan}!")
        print(f"Overpayment = {over_payment}")
        break
    elif args.type == "annuity" and args.periods is None:
        months = total_periods(int(args.payment), float(args.interest), int(args.principal))
        over_payment = int(args.payment) * months - int(args.principal)
        years = int(months / 12) if int(months / 12) != 0 else ''
        if years:
            months -= years * 12
            if months == 0:
                months = ''
        else:
            pass

        if years and months:
            if years == 1 and months == 1:
                print(f"It will take {years} year and {months} month to repay this loan!")
            elif years == 1 and months != 0:
                print(f"It will take {years} year and {months} months to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
        elif years and not months:
            if years == 1:
                print(f"It will take {years} year to repay this loan!")
            else:
                print(f"It will take {years} years to repay this loan!")
        elif not years and months:
            if months == 1:
                print(f"It will take {months} month to repay this loan!")
            else:
                print(f"It will take {months} months to repay this loan!")
        else:
            pass
        print(f"Overpayment = {over_payment}")
        break
    elif args.type == "diff" and args.principal is None:
        loan = loan_principle(int(args.payment), float(args.interest), int(args.periods))
        total_money = differentiated_payment(loan, int(args.periods), float(args.interest))
        over_payment = total_money - loan
        print("")
        print(f"Overpayment = {over_payment}")
        break
    elif args.type == "diff" and args.periods is None:
        months = total_periods(int(args.payment), float(args.interest), int(args.principal))
        total_money = differentiated_payment(int(args.principal), months, float(args.interest))
        over_payment = total_money - int(args.principal)
        print("")
        print(f"Overpayment = {over_payment}")
        break
    else:
        total_money = differentiated_payment(int(args.principal), int(args.periods), float(args.interest))
        over_payment = total_money - int(args.principal)
        print("")
        print(f"Overpayment = {over_payment}")
        break
