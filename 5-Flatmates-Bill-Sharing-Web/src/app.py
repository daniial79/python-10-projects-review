from views import HomePage, BillFormPage, ResultPage
from flask import Flask, render_template

app = Flask(__name__)


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/result", view_func=ResultPage.as_view("result_page"))


@app.errorhandler(404)
def notFoundHandler(error):
    return render_template("notFound.html"), 404

app.run(debug=True)