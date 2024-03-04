from flask.views import MethodView
from flask import render_template, request
from wtforms import Form, StringField, SubmitField

import utility.bill as bill
import utility.flat as flat
import utility.report as report


class BillForm(Form):
    amount = StringField("Bill Amount: ", default=3500)
    period = StringField("Bill Period: ", default="March 2024")
    
    flatmate_one_name = StringField("What is your name: ", default="danial")
    flatmate_one_days = StringField("Days you've at flat spent: ", default=30)
    
    flatmate_two_name = StringField("what is your name: ", default="parmis")
    flatmate_two_days = StringField("Days you've at flat spent: ", default=20)
    
    button = SubmitField("Calculate")
    

class HomePage(MethodView):

    def get(self):
        return render_template("index.html")

class BillFormPage(MethodView):
    
    def get(self):
        bill_form = BillForm()
        return render_template("billFormPage.html", 
                               billform=bill_form)

class ResultPage(MethodView):
    
    def post(self):
        bill_form = BillForm(request.form)
        
        the_bill = bill.Bill(
            amount=float(bill_form.amount.data), 
            period=bill_form.period.data
        )
        
        flatmate_one = flat.Flatmate(
            bill_form.flatmate_one_name.data, 
            float(bill_form.flatmate_one_days.data)
        )
        
        flatmate_two = flat.Flatmate(
            bill_form.flatmate_two_name.data, 
            float(bill_form.flatmate_two_days.data)
        )
        
        bill_report = report.PayReport(
            filename=f"{'-'.join(the_bill.period.split())}",
            bill=the_bill,
            flatmates=[flatmate_one, flatmate_two]
        )
        

        return render_template("resultPage.html", flatmate_one=flatmate_one, flatmate_two=flatmate_two)
        

