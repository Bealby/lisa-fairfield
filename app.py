
# Imports

import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# 'MONGO_URI' and 'EMAILJS_KEY' stored in Enviroment Variables

app.config["MONGO_DBNAME"] = 'magnet_fishing'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

EMAILJS_KEY = os.environ.get("EMAILJS_KEY")

mongo = PyMongo(app)

# Function to load 'Home' page as default


@app.route('/')
def home():
    return render_template("intro-communication/index.html")