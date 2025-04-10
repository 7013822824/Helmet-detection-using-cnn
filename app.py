from flask import Flask, render_template, jsonify,redirect, url_for, request
import json 
from distraction import detect_mobile_phone
from helmet import detect_plates
from traffic_signal import detect_signal_violation
from flask import Flask, render_template, request
import os
import time
import utils


app = Flask(__name__)

ROOT_DIR = "./"
UPLOAD_DIR = './uploads'

with open("details.json", "r") as jf:
    data = json.load(jf)
    
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)

        if username in data["login"].keys() and data["login"][username]==password:
            return redirect(url_for('helmet_compliance'))
    
    return render_template('Auth.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        data['login'][email] = password
        with open('details.json', 'w') as jf:
            json.dump(data, jf)

        return redirect(url_for('login'))
    
    return render_template('Signup.html')


@app.route('/helmet_compliance', methods=['POST', 'GET'])
def helmet_compliance():
    if request.method == 'POST':
        uploaded_file = request.files['video_file']

        if uploaded_file:
            # Get the selected file name
            file_name = uploaded_file.filename
            file_path = os.path.join(UPLOAD_DIR, file_name)

            uploaded_file.save(file_path)
            selected_location = request.form.get('location')

            ret = detect_plates(file_path, selected_location)
            
            return jsonify(ret)
            
    locations = ['CMBT', 'Anna Nagar', 'Shenoy Nagar', 'Arumbakkam', 'Vadapalani']
    return render_template('Helmet.html', location=locations)


@app.route('/signal', methods=['POST', 'GET'])
def signal_video():
    if request.method == 'POST':
        uploaded_file = request.files['video_file']

        if uploaded_file:
            # Get the selected file name
            file_name = uploaded_file.filename
            file_path = os.path.join(UPLOAD_DIR, file_name)
            uploaded_file.save(file_path)

            selected_location = request.form.get('locations')

            ret = detect_signal_violation(file_path, selected_location)
 
            return jsonify(ret)

    locations = ['CMBT', 'Anna Nagar', 'Shenoy Nagar', 'Arumbakkam', 'Vadapalani']
    return render_template('Signal.html', location = locations)


@app.route('/cellphone', methods=['POST', 'GET'])
def cellphone_video():
    if request.method == 'POST':
        uploaded_file = request.files['video_file']

        if uploaded_file:
            # Get the selected file name
            file_name = uploaded_file.filename
            file_path = os.path.join(UPLOAD_DIR, file_name)
            uploaded_file.save(file_path)

            print("Uploaded File Name:", file_name)

            # Get the selected location from the form
            selected_location = request.form.get('locations')

            ret = detect_mobile_phone(file_path, data, selected_location)
            print("Selected Location:", selected_location)
            return jsonify(ret)

    locations = ['CMBT', 'Anna Nagar', 'Shenoy Nagar', 'Arumbakkam', 'Vadapalani']
    return render_template('Cellphone.html', location = locations)


# @app.route('/alert', methods=['POST', 'GET'])
# def alert():    
#     return render_template('Alert.html')


# @app.route('/analytics', methods=['POST', 'GET'])
# def analytics():    
#     return render_template('Analytics.html')


# @app.route('/email' , methods=['POST','GET'])
# def email():
#    return render_template('Analytics.html')


if __name__ == '__main__':
    app.run(debug=True)