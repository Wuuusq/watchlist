import os,sys
import click
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URL'] = prefix + os.path.join(app.root_path,)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 创建数据库模型类
class User(db.Model):
    id = db.Column(db.Integer,primay_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):
    id = db.Column(db.Integer, primay_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

# 自定义指令initdb
@app.cli.command()
@click.option('--drop',is_flag=True,help='删除之后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')

# 自定义命令forge，把数据写入数据库
@app.cli.command()
def forge():
    db.create_all()
    name = "wuuusq"
    movies = [
        {"titel": "《扫毒》", "year": "2015"},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
        {"titel": "《》", "year": ""},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(titel=m['titel'],year=m['year'])
    

@app.route('/')
def indeex():
    # movies = Movie.query.all()
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.context_processor  # 模板上下文处理函数
def inject_user():
    user = User.query.first()
    return dict(user=user)
