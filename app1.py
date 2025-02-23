from markupsafe import escape # Package needed for
from flask import Flask

app = Flask(__name__)


@app.route('/') # Decorator to make a route
@app.route('/index/') # You can have two routes to the same place. This ensures the main file is index.html
def hello():
    return '<h1>Hello, World!</h1>'

@app.route('/about/') # Make your own named route
def about():
    return '<h3>This is a Flask web application.</h3>'


@app.route('/capitalize/<word>/') # <word> is sent as the parameter
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))
# escape escapes any special characters so people can't hack your system

# https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application