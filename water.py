from flask import Flask, render_template, redirect, url_for, request
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
scheduler = BackgroundScheduler()

def hello():
    return "Hello World!"

def remind_to_drink():
    # Prints reminder message t
    print("Take a sip of your water bottle!")

@app.route('/time-form')
def time_form():
    return render_template('time_form.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    user_input = request.form['myInput']
    scheduler.add_job(func=remind_to_drink, trigger='interval', seconds=int(user_input))
    scheduler.start()
    return f'Reminder set for every {user_input} seconds'

# def send_reminder():
#     print("Take a sip of water!")

# def set_reminder():
#     scheduler = BackgroundScheduler()
#     interval = request.form['myInput']
#     scheduler.add_job(func=send_reminder, trigger='interval', seconds=interval)
#     scheduler.start()

#     return 'Reminder Set'

@app.route('/')
def home():
    return render_template('time_form.html')



@app.route('/set-reminder/<int:interval>')

def set_reminder(interval):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=remind_to_drink, trigger='interval', seconds=interval)
    scheduler.start()
    return f"Reminder set for every {interval} seconds"

if __name__ == '__main__':
    app.run(debug=True)

