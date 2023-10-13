from flask import Flask, render_template, redirect
from .config import Configuration
from .models import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Configuration)
db.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def homepage():
    return render_template("the_big_show_homepage.html")
