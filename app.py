import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:////' + os.path.join(app.root_path,)
app.config['S']

db = SQLAlchemy(app)

@app.route('/')
def indeex():
    name = "wuuusq"
    movies = [
        {"titel":"《扫毒》","year":"2015"},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
        {"titel":"《》","year":""},
    ]
    return render_template('index.html',name=name,movies=movies)
