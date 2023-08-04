from flask import Flask, render_template, redirect, url_for, request
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess

app = Flask(__name__)
scheduler = BackgroundScheduler()

def send_macos_notification():
    script = f'display notification "hi" with title "Reminder"'
    subprocess.run(['osascript', '-e', script])

def remind_to_drink():
    # Prints reminder message
    print("Take a sip of your water bottle!")

# @app.route('/time-form')
# def time_form():
#     return render_template('time_form.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    user_input = request.form['myInput']
    scheduler.add_job(func=send_macos_notification, trigger='interval', seconds=int(user_input))
    scheduler.start()
    return f'Reminder set for every {user_input} seconds'


@app.route('/')
def home():
    return render_template('time_form.html')


if __name__ == '__main__':
    app.run(debug=True)

