from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from backend import project
from pandas as pd
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import SubmitField, IntegerField
from wtforms.validators import InputRequired

import secrets




app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = foo

bootstrap = Bootstrap5(app)

csrf = CSRFProtect(app)

csrf.init_app(app)

class ExpForm(FlaskForm):
    name = IntegerField('Years of Experience', validators=[InputRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ExpForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data

    return render_template("index.html", form=form, message=message)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict' , methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        predicted_salary = 0
        exp = request.form['name']
        df = pd.DataFrame({'YearsExperience': [exp]})
        project.models.get('salarypredictor').predict(df)
        psprice = "The predicted salary for " + exp + " years of exp is: " + f"{predicted_salary}"

      
    return render_template("predict.html" , psprice=psprice)



if __name__ == '__main__':
    app.run(debug=True)
