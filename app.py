import datetime
from flask import Flask, render_template #importing two files from flask package

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    return render_template('indexBasedOnTemplate.html', utc_dt=datetime.datetime.utcnow()) # Use render template library
# Template must use what variables you send it

# ...
@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/comments/')
def comments():
    comments = ['This is the first comment.',
                'This is the second comment.',
                'This is the third comment.',
                'This is the fourth comment.'
                ]

    return render_template('comments.html', comments=comments)