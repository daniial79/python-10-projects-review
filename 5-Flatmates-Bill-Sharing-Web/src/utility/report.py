import os.path
import webbrowser
from filestack import Client
from fpdf import FPDF



def pays(total_amount: float, coefficient: float) -> float:
    return total_amount * coefficient


def calculate_flatmates_share(flatmates_list, bill):
    total_days = 0
    for flatmate in flatmates_list:
        total_days += flatmate.days_in_house

    for flatmate in flatmates_list:
        flatmate.amount_to_pay = pays(total_amount=bill.amount,
                                      coefficient=flatmate.days_in_house / total_days)


class PayReport:
    """
    Generate a pdf file that contains 0flatmate payments and period of the bill.
    """

    def __init__(self, filename: str, bill, flatmates):
        self.filename = filename
        self.bill = bill
        self.flatmates = flatmates
        self.pdf_creator = FPDF(orientation="P", unit="pt", format="A4")

        calculate_flatmates_share(flatmates, bill)

    def generate_pdf(self):
        self.pdf_creator.add_page()
        self.pdf_creator.image("./files/house.png", w=50, h=50)
        self.pdf_creator.set_font(family="Times", size=24, style="B")

        self.pdf_creator.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        self.pdf_creator.set_font(family="Times", size=20, style="B")
        self.pdf_creator.cell(w=100, h=40, txt="Period:", border=0)
        self.pdf_creator.cell(w=150, h=40, txt=self.bill.period, border=0, align="C", ln=1)

        self.pdf_creator.set_font(family="Times", size=18)
        for flatmate in self.flatmates:
            to_pay = str(round(flatmate.amount_to_pay, 2))
            self.pdf_creator.cell(w=100, h=25, txt=flatmate.name, border=0)
            self.pdf_creator.cell(w=100, h=25, txt=to_pay, border=0, align="C", ln=1)

        self.pdf_creator.output(self.filename)
        webbrowser.open("file://" + os.path.realpath(self.filename))

class FileSharer:
    def __init__(self, filename: str, api_key: str):
        self.filename = filename
        self.client = Client(api_key)

    def share(self):
        new_file_link = self.client.upload(filepath=self.filename)
        return new_file_link.url