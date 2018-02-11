from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user
from app.models import User

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/siem')
def siem():
    return render_template('siem.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('siem'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('siem'))
    return render_template('login.html', title='Log In', form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
