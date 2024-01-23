import requests
from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()

api_key = os.getenv('API_KEY')

app = Flask(__name__)

@app.route('/')
def index():
    return 'Home Page'

@app.route('/recipes')
def recipes():
    return 'Recipes Page'

if __name__ == '__main__':
    app.run(debug=True)