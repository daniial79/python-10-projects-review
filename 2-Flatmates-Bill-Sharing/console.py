from bill import Bill
from flat import Flatmate

def get_bill_data() -> Bill:
    while True:
        try:
            bill_amount = float(input("Enter your bill amount: "))
            bill_period = input("Enter your bill period (e.g March 2017): ")
            print("-" * 20)
            return Bill(bill_amount, bill_period)
        except ValueError:
            print("Bill amount must be number!")


def get_flatmate_quantities() -> int:
    while True:
        try:
            flatmates_quantity = int(input("Enter number of flatmates: "))
            print("-" * 20)
            return flatmates_quantity
        except ValueError:
            print("flatmates quantity must be an integer")


def get_flatmate_list(flatmate_quantity: int) -> list[Flatmate]:
    flatmates = []
    try:
        i = 1
        while i <= flatmate_quantity:
            flatmate_name = input(f"Enter name of flatmate number {i}: ")
            days_in_house = int(input(f"How many days {flatmate_name} has stayed home? "))
            flatmates.append(Flatmate(flatmate_name, days_in_house))
            print("-" * 20)
            i += 1
    except ValueError:
        print("Days in house must be a number")
        print("-" * 20)

    return flatmates