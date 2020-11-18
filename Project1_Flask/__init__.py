from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY']='cop4813'

from Project1_Flask import routes