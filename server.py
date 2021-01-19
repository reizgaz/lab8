from algorithm import factorization
from flask import Flask, redirect, url_for, render_template, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key' 


class MyForm(FlaskForm):
    input_number = StringField("Enter your number:", validators=[DataRequired()])
    submit = SubmitField('OK')



@app.route('/')
def go_to_index():
    return redirect(url_for('index'))


@app.route('/index', methods=['GET', 'POST'])
def index(): 
    form = MyForm()
    if form.validate_on_submit():
        number = form.input_number.data
        return redirect(url_for('result', number=number)) 
    return render_template('index.html', form=form)


@app.route('/result/<number>')
def result(number): 
    try:
        res = factorization(int(number)) 
    except ValueError:
        res = "error, wrong data type, use only <int>" 
    return render_template('result.html', number=number, result=res)


if __name__ == "__main__":
    app.run()
