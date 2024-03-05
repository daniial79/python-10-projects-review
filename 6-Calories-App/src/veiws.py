from flask import request
from flask import render_template
from flask.views import MethodView 
from wtforms import Form, StringField, SubmitField

from core.temperature import Temprature
from core.calory_calculator import CaloryCalculator


class CaloriesForm(Form):
    weight = StringField("Weight: ")
    height = StringField("Height: ")
    age = StringField("Age: ")
    
    city = StringField("City: ")
    country = StringField("Country: ")
    
    button = SubmitField("Calculate")
    

class HomePage(MethodView):
    def get(self):
        return render_template("index.html")
    
class ClaoriesFormPage(MethodView):
    def get(self):
        form = CaloriesForm()
        
        return render_template("form.html", calories_form=form)    
    
class ResultPage(MethodView):
    def post(self):
        calories_form = CaloriesForm(request.form)
        
        city = calories_form.city.data
        country = calories_form.country.data
        
        region_temperature = Temprature(city, country).get()
        
        weight = float(calories_form.weight.data)
        height = float(calories_form.height.data)
        age = float(calories_form.age.data)
        
        calory_calculator = CaloryCalculator(weight, height, age, region_temperature)
        calculated_calure = calory_calculator.calculate()
        
        
        return render_template("result.html", needed_calory=calculated_calure)