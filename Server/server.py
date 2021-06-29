from flask import Flask, request, jsonify
from flask import render_template, url_for, flash, get_flashed_messages, redirect
import util
from form import PredictForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'b0cafc1c41a7468f36893a80'

__predicted_price = None
__category = None

@app.route('/', methods=['GET','POST'])
def predict_page():
    global __predicted_price
    global __category
    form = PredictForm()
    locations = util.get_location_names()
    form.location.choices = locations
    if request.method == 'POST':
        total_sqft = int(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhks'])
        bath = int(request.form['bathrooms'])
        __predicted_price = util.get_estimated_price(location,total_sqft,bhk,bath)
        print(__predicted_price)
        if __predicted_price >= 200:
            __predicted_price /= 100
            __category = "Crores"
        elif __predicted_price >= 100 and __predicted_price <= 200:
            __predicted_price /= 100
            __category = "Crore"
        else:
            __category = "Lakhs"
            
        if __predicted_price <= 0:
            __predicted_price = None 
            __category = "House Not Available"
        else:
            __predicted_price = round(__predicted_price, 1)
        return render_template('index.html', form=form, predicted_price=__predicted_price, category=__category)

    if request.method == 'GET':
        __predicted_price = None
        return render_template('index.html', form=form, predicted_price=__predicted_price, category=__category)


if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(debug=True)