import subprocess
from app import app,redis_store
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
import myscriptutils as scriptutils

######################################################
@app.route('/basic/<submenu>',methods=['GET','POST'])
def basic(submenu):
    print("* " + submenu)
    if submenu == 'networksetting':
        form = LANConfiguration()
        ip_mode = scriptutils.get_ip_mode()
        ip_addr = scriptutils.get_ipaddr()
        subnet_mask = scriptutils.get_subnet_mask()
        default_gwaddr = scriptutils.get_defaultgwaddr()
        dnsservers = scriptutils.get_dnsservers()

        if request.method == 'GET':
	    form.ip_mode.default = 1 if ip_mode == 'static' else 2 
	    form.ip_address.default = ip_addr
            form.subnet_mask.default = subnet_mask
            form.default_gateway_address.default = default_gwaddr
            form.primary_dns_ip_address.default = dnsservers[0]
            form.secondary_dns_ip_address.default = dnsservers[1] if len(dnsservers)==2 else ''
	    form.process()

        if form.validate_on_submit():
            flash("success network settings")
            print("ip_address = {}".format(form.ip_address.data))

            ip_mode = form.ip_mode.data
            if ip_mode == '1':
                print("setting for static networking")
                ipaddr = form.ip_address.data
                subnet = form.subnet_mask.data
                gw = form.default_gateway_address.data
                dns1 = form.primary_dns_ip_address.data
                dns2 = form.secondary_dns_ip_address.data
		scriptutils.do_staticnetworking(ipaddr,subnet,gw,dns1,dns2)

            return redirect(url_for('siem'))
        return render_template('lanconfiguration.html',form=form)
    elif submenu == 'administration':
        form = SystemInformation()

        if request.method == 'GET':
            form.system_contact.default = redis_store.get('agent:syscontact')
            form.system_location.default = redis_store.get('agent:syslocation')
            form.ro_commstring.default = redis_store.get('agent:rocommunity')
            form.process()

        if form.validate_on_submit():
            flash("success sys administration settings")
            prev_sc = form.system_contact.default = redis_store.get('ugent:syscontact')
            prev_sl = form.system_location.default = redis_store.get('agent:syslocation')
            prev_ro = form.ro_commstring.default = redis_store.get('agent:rocommunity')
            if prev_sc != form.system_contact.data:
                redis_store.set('agent:syscontact',form.system_contact.data)
                redis_store.publish('agent','agent:syscontact')
            if prev_sl != form.system_location.data:
                redis_store.set('agent:syslocation',form.system_location.data)
                redis_store.publish('agent','agent:syslocation')
            if prev_ro != form.ro_commstring.data:
                redis_store.set('agent:rocommunity',form.ro_commstring.data)
                redis_store.publish('agent','agent:rocommunity')
            return redirect(url_for('siem'))
        return render_template('systeminformation.html',form=form)

@app.route('/algo/<submenu>',methods=['GET','POST'])
def algo(submenu):
    if submenu == 'jamming':
        form = Jamming()
        if request.method == 'GET':
            form.timeout.default = redis_store.get('algo:JammingEventTimeout')
            form.process()
        if form.validate_on_submit():
            flash("success jamming settings")
            previous = redis_store.get('algo:JammingEventTimeout')
            if previous != form.timeout.data:
                redis_store.set('algo:JammingEventTimeout',form.timeout.data)
                redis_store.publish('algo','algo:JammingEventTimeout')
            return redirect(url_for('siem'))
        return render_template('jamming.html',form=form)
    elif submenu == 'wlanattack':
        form = WLANAttack()
        if request.method == 'GET':
            form.timeout.default = redis_store.get('algo:WlanAttackEventTimeout')
            form.process()
        if form.validate_on_submit():
            previous = redis_store.get('algo:WlanAttackEventTimeout')
            if previous != form.timeout.data:
                redis_store.set('algo:WlanAttackEventTimeout',form.timeout.data)
                redis_store.publish('algo','algo:WlanAttackEventTimeout')
            flash("success WLAN ATtack settings")
            return redirect(url_for('siem'))
        return render_template('wlanattack.html',form=form)
    elif submenu == 'bruteforcelogin':
        form = BruteForceLogin()
        if request.method == 'GET':
            form.timeout.default = redis_store.get('algo:BruteForceLoginEventTimeout')
            form.duration.default = redis_store.get('algo:BruteForceLoginWindow')
            form.count.default = redis_store.get('algo:BruteForceLoginThd')
            form.process()
        if form.validate_on_submit():
            previous_to = redis_store.get('algo:BruteForceLoginEventTimeout')
            previous_win = redis_store.get('algo:BruteForceLoginWindow')
            previous_thd = redis_store.get('algo:BruteForceLoginThd')
            if previous_to != form.timeout.data:
                redis_store.set('algo:BruteForceLoginEventTimeout',form.timeout.data)
                redis_store.publish('algo','algo:BruteForceLoginEventTimeout')
            if previous_win != form.duration.data:
                redis_store.set('algo:BruteForceLoginWindow',form.duration.data)
                redis_store.publish('algo','algo:BruteForceLoginWindow')
            if previous_thd != form.count.data:
                redis_store.set('algo:BruteForceLoginThd',form.count.data)
                redis_store.publish('algo','algo:BruteForceLoginThd')
            #form.process()
            flash("success Brute Force Login settings")
            return redirect(url_for('siem'))
        return render_template('bruteforcelogin.html',form=form)
    elif submenu == 'radiuslogin':
        form = RadiusLogin()
        if request.method == 'GET':
            form.timeout.default = redis_store.get('algo:RadiusLoginEventTimeout')
            form.duration.default = redis_store.get('algo:RadiusLoginWindow')
            form.count.default = redis_store.get('algo:RadiusLoginThd')
            form.process()
        if form.validate_on_submit():
            previous_to = redis_store.get('algo:RadiusLoginEventTimeout')
            previous_win = redis_store.get('algo:RadiusLoginWindow')
            previous_thd = redis_store.get('algo:RadiusLoginThd')

            if previous_to != form.timeout.data:
                redis_store.set('algo:RadiusLoginEventTimeout',form.timeout.data)
                redis_store.publish('algo','algo:RadiusLoginEventTimeout')
            if previous_win != form.duration.data:
                redis_store.set('algo:RadiusLoginWindow',form.duration.data)
                redis_store.publish('algo','algo:RadiusLoginWindow')
            if previous_thd != form.count.data:
                redis_store.set('algo:RadiusLoginThd',form.count.data)
                redis_store.publish('algo','algo:RadiusLoginThd')
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
            print("clish_mode = " + form.clish_mode.data)
            print("ssh_mode = " + form.ssh_mode.data)
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
