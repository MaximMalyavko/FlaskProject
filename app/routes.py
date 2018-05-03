from app import app
from flask import render_template, redirect, flash, url_for, request
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

@app.route("/")
@app.route("/index")
@login_required
def index():
    #user = {'username':'Fedor'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Иполит'},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    return render_template('index.html', title='Main page', posts=posts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Wrong login or password!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        print('111')
        print(next_page)
        print('222')
        print(url_parse(next_page))
        if not next_page or url_parse(next_page).netloc != '':
            print('333')
            next_page = url_for('index')
            print('444')
        print('555')
        return redirect(next_page)
        print('777')
    return render_template('login.html', title='Sign in', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))
