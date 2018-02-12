from app import app
from flask import render_template,flash,redirect,url_for,request
from flask_login import current_user, login_user, logout_user,login_required
from app.models import User
from werkzeug.urls import url_parse
from app.forms import \
    LoginForm,\
    LANConfiguration,\
    SystemInformation,\
    Jamming,\
    WLANAttack,\
    BruteForceLogin,\
    RadiusLogin,\
    ServicesCli,\
    ServicesDhcp,\
    ServicesWebServer,\
    ServicesSnmp,\
    SystemDeviceMaintenance,\
    SystemStatus,\
    SystemStatistics,\
    GraylogStatus,\
    AlertsMonitor,\
    ComponentUpgrade,\
    SystemLog

######################################################
@app.route('/basic/<submenu>',methods=['GET','POST'])
def basic(submenu):
    print("* " + submenu)
    if submenu == 'networksetting':
        form = LANConfiguration()
        if form.validate_on_submit():
            flash("success network settings")
            print("ip_address = {}".format(form.ip_address.data))
            return redirect(url_for('siem'))
        return render_template('lanconfiguration.html',form=form)
    elif submenu == 'administration':
        form = SystemInformation()
        if form.validate_on_submit():
            flash("success sys administration settings")
            return redirect(url_for('siem'))
        return render_template('systeminformation.html',form=form)

@app.route('/algo/<submenu>',methods=['GET','POST'])
def algo(submenu):
    if submenu == 'jamming':
        form = Jamming()
        if form.validate_on_submit():
            flash("success jamming settings")
            return redirect(url_for('siem'))
        return render_template('jamming.html',form=form)
    elif submenu == 'wlanattack':
        form = WLANAttack()
        if form.validate_on_submit():
            flash("success WLAN ATtack settings")
            return redirect(url_for('siem'))
        return render_template('wlanattack.html',form=form)
    elif submenu == 'bruteforcelogin':
        form = BruteForceLogin()
        if form.validate_on_submit():
            flash("success Brute Force Login settings")
            return redirect(url_for('siem'))
        return render_template('bruteforcelogin.html',form=form)
    elif submenu == 'radiuslogin':
        form = RadiusLogin()
        if form.validate_on_submit():
            flash("success Radius Login settings")
            return redirect(url_for('siem'))
        return render_template('radiuslogin.html',form=form)

@app.route('/services/<submenu>',methods=['GET','POST'])
def services(submenu):
    if submenu == 'cli':
        form = ServicesCli()

        if request.method == 'GET':
            form.clish_mode.default = 1
            form.ssh_mode.default = 2
            form.ssh_port.default = 8888
            form.process()

        if form.validate_on_submit(): 
            print("SSH PORT = " + form.ssh_port.data)
            return redirect(url_for('siem'))    
        return render_template('servicescli.html',form=form)
    elif submenu == 'dhcp':
        form = ServicesDhcp()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('servicesdhcp.html',form=form)
    elif submenu == 'webserver':
        form = ServicesWebServer()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('serviceswebserver.html',form=form)
    elif submenu == 'snmp':
        form = ServicesSnmp()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('servicessnmp.html',form=form)

@app.route('/system/<submenu>',methods=['GET','POST'])
def system(submenu):
    if submenu == 'devicemaintenance':
        form = SystemDeviceMaintenance()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('systemdevicemaintenance.html',form=form)
    elif submenu == 'systemlog':
        form = SystemLog()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('systemlog.html',form=form)

@app.route('/status/<submenu>',methods=['GET','POST'])
def status(submenu):
    if submenu == 'systemstatus':
        form = SystemStatus()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('systemstatus.html',form=form)
    elif submenu == 'systemstatistics':
        form = SystemStatistics()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('systemstatistics.html',form=form)
    elif submenu == 'graylogstatus':
        form = GraylogStatus()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('graylogstatus.html',form=form)
    elif submenu == 'alertsmonitor':
        form = AlertsMonitor()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('alertsmonitor.html',form=form)

@app.route('/superuser/<submenu>',methods=['GET','POST'])
def superuser(submenu):
    if submenu == 'componentupgrade':
        form = ComponentUpgrade()
        if form.validate_on_submit():
            return redirect(url_for('siem'))
        return render_template('componentupgrade.html',form=form)
######################################################

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/siem')
@login_required
def siem():
    return render_template('siem.html' if current_user.username == 'admin' else 'siemuser.html')

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
        next_page = request.args.get('next') 
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('siem')    
        return redirect(next_page)
    return render_template('login.html', title='Log In', form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
