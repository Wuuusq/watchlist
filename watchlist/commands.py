import click
from watchlist import app, db
from watchlist.model import User, Movie


# 自定义initdb
@app.cli.command()
@click.option('--drop', is_flag=True, help='删除之后再创建')
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('初始化数据库')


# 自定义命令forge，把数据写入数据库
@app.cli.command()
def forge():
    db.create_all()
    name = "Wuuusq"
    movies = [
        {'title': '扫毒', 'year': '2003'},
        {'title': '变形金刚', 'year': '2018'},
        {'title': '速度与激情8', 'year': '2016'},
        {'title': '爱情公寓5', 'year': '2020'},
        {'title': '名侦探柯南', 'year': '1989'},
        {'title': '灌篮高手', 'year': '2020'},
        {'title': '犬夜叉', 'year': '2020'},
        {'title': '七龙珠', 'year': '2017'},
        {'title': '海贼王', 'year': '2005'},
        {'title': '火影忍者', 'year': '2015'}
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo('数据导入完成')


# 生成admin账号的函数
@app.cli.command()
@click.option('--username', prompt=True, help="用来登录的用户名")
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help="用来登录的密码")
def admin(username, password):
    db.create_all()
    user = User.query.first()
    if user is not None:
        click.echo('更新用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建用户')
        user = User(username=username, name="Admin")
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('创建管理员账号完成')
