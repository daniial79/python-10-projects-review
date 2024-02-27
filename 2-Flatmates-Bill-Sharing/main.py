from os import getenv
from report import PayReport, FileSharer
from console import get_bill_data, get_flatmate_quantities, get_flatmate_list


def prompt(message) -> str:
    value = input(message + ": ")
    return value


def main():
    bill = get_bill_data()
    flatmates_quantity = get_flatmate_quantities()
    flatmates = get_flatmate_list(flatmates_quantity)

    payment_report = PayReport(f"{'-'.join(bill.period.split())}.pdf", bill, flatmates)
    payment_report.generate_pdf()

    file_sharer = FileSharer(payment_report.filename, getenv("API_KEY"))
    # print(file_sharer.share())


if __name__ == '__main__':
    main()
