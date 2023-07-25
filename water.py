from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def hello():
    return "Hello World!"

def remind_to_drink():
    # Prints reminder message t
    print("Take a sip of your water bottle!")

@app.route('/set-reminder/<int:interval>')

def set_reminder(interval):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=remind_to_drink, trigger='interval', seconds=interval)
    scheduler.start()
    return f"Reminder set for every {interval} seconds"

if __name__ == '__main__':
    app.run(debug=True)