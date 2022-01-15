from flask import render_template, request, Blueprint
from models import db, User


main = Blueprint('main', __name__)


@main.route('/')
def index():

    return render_template('index.html')


@main.route('/say', methods=['GET', 'POST'])
def say_hi():
    name = request.form['name']
    user = User.query.filter(User.user_name == name).first()
    if user:
        is_first_time = False
    else:
        user = User(user_name=name)
        db.session.add(user)
        db.session.commit()
        is_first_time = True

    return render_template('hello.html', user=user, is_first_time=is_first_time)


@main.route('/names')
@main.route('/names/p<int:page>')
def list_names(page=1):

    users = User.query.paginate(page, 5, False)

    return render_template('names.html', users=users)
