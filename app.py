import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/recipes')
def recipes():
    return 'Recipes Page'

if __name__ == '__main__':
    app.run(debug=True)