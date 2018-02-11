from app import app
from flask import render_template,flash,redirect,url_for
from app.forms import LoginForm

@app.route('/siem')
def siem():
    return render_template('siem.html')

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "admin":
            return redirect(url_for('siem'))
    return render_template('login.html', title='Log In', form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
