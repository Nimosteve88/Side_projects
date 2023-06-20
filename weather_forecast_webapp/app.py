from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, validators, SubmitField
from sunnyday import Weather

app = Flask(__name__)


# app.secret_key = 'supersecretkey'


class CityForm(Form):
    city = StringField('City Name', validators=[validators.InputRequired()])
    apikey = StringField('API Key', validators=[validators.InputRequired()])
    latitude = StringField('Latitude', validators=[validators.InputRequired()])
    longitude = StringField('Longitude', validators=[validators.InputRequired()])
    button = SubmitField("Enter")


class Weather_info(MethodView):


    def get(self):
        form = CityForm(request.form)
        return render_template('index.html', form=form)

    def post(self):
        form = CityForm(request.form)
        city_name = form.city.data
        api = form.apikey.data
        lat = form.latitude.data
        lon = form.longitude.data
        # You can replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
        weather = Weather(apikey=api, city=city_name, lat=lat, lon=lon)
        weather_info = weather.next_12h_simplified()
        weather_icon = weather.getweathericon()
        print(weather_icon)
        return render_template('weather.html', weather_info=weather_info, weather_icon=weather_icon)

price = []


#app.add_url_rule('/', view_func=CityForm.as_view('city_form'))
app.add_url_rule('/', view_func=Weather_info.as_view('weather_info'))
app.add_url_rule('/weather', view_func=Weather_info.as_view('weather'))

app.run(debug=True)
