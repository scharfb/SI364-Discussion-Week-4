from flask import Flask, request, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required
import requests
import json

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'
app.debug=True

apikey = "b6f6d067a6547408387b38f3f735019a"

#####################
####### FORMS #######
#####################

class WeatherForm(FlaskForm):
    zipcode = IntegerField('Enter Zipcode:', validators=[Required()])
    submit = SubmitField('Submit')

    def validate_zipcode(self, field):
        if len(str(field.data)) != 5:
            raise ValidationError("Please enter a 5 digit zipcode")



@app.route('/zipcode', methods = ['GET', 'POST'])
def zipcode_view():
    form = WeatherForm()
    if form.validate_on_submit():

    flash(form.errors)
    return render_template('weather_form.html', form = form)




if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)

