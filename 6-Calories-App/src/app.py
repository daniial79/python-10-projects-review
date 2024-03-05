from flask import Flask
from veiws import HomePage, ClaoriesFormPage ,ResultPage

app = Flask(__name__)


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/form", view_func=ClaoriesFormPage.as_view("calories_form_page"))
app.add_url_rule("/result", view_func=ResultPage.as_view("result_page"))

app.run(debug=True)