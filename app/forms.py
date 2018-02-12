from flask_wtf import FlaskForm
from wtforms import \
    StringField,\
    PasswordField,\
    BooleanField,\
    SubmitField,\
    SelectField
from wtforms.validators import DataRequired,IPAddress,Length,NumberRange

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class LANConfiguration(FlaskForm):
    my_choices = [('1', 'Static IP'), ('2', 'Dynamic IP (DHCP)')]
    ip_mode = SelectField('IP Mode',choices = my_choices)
    ip_address  = StringField(u'IP Address', validators=[DataRequired(),IPAddress()])
    subnet_mask  = StringField(u'Subnet Mask', validators=[DataRequired(),IPAddress()])
    default_gateway_address  = StringField(u'Default Gateway Address', validators=[DataRequired(),IPAddress()])
    primary_dns_ip_address  = StringField(u'Primary DNS IP Address', validators=[DataRequired(),IPAddress()])
    secondary_dns_ip_address  = StringField(u'Secondary DNS IP Address', validators=[DataRequired(),IPAddress()])
    submit = SubmitField('Update')

class SystemInformation(FlaskForm):
    system_contact  = StringField('System Contact', validators=[])
    system_location  = StringField('System Location', validators=[])
    system_name  = StringField('System Name', validators=[])
    serial_number  = StringField('Serial Number', validators=[])
    submit = SubmitField('Update')

class Jamming(FlaskForm):
    timeout  = StringField('Timeout', validators=[NumberRange()])
    submit = SubmitField('Update')

class WLANAttack(FlaskForm):
    timeout  = StringField('Timeout', validators=[NumberRange()])
    submit = SubmitField('Update')

class BruteForceLogin(FlaskForm):
    timeout  = StringField('Timeout', validators=[NumberRange()])
    duration  = StringField('Duration', validators=[NumberRange()])
    count  = StringField('Count', validators=[NumberRange()])
    submit = SubmitField('Update')

class RadiusLogin(FlaskForm):
    timeout  = StringField('Timeout', validators=[NumberRange()])
    duration  = StringField('Duration', validators=[NumberRange()])
    count  = StringField('Count', validators=[NumberRange()])
    submit = SubmitField('Update')

def getdefault():
    return 2222

class ServicesCli(FlaskForm):
    mode_options = [('1', 'Enable'), ('2', 'Disable')]
    clish_mode = SelectField('Mode',choices = mode_options)
    ssh_mode = SelectField('Mode',choices = mode_options)
    ssh_port = StringField('Port',validators=[DataRequired(),NumberRange()])
    submit = SubmitField('Update')

class ServicesDhcp(FlaskForm):
    mode_options = [('1', 'Enable'), ('2', 'Disable')]
    mode = SelectField('Mode',choices = mode_options)
    subnet_mask  = StringField(u'Subnet Mask', validators=[DataRequired(),IPAddress()])
    gateway_ip  = StringField(u'Gateway IP', validators=[DataRequired(),IPAddress()])
    primary_dns_ip  = StringField(u'Primary DNS IP', validators=[DataRequired(),IPAddress()])
    secondary_dns_ip  = StringField(u'Secondary DNS IP', validators=[DataRequired(),IPAddress()])
    submit = SubmitField('Update')

class ServicesWebServer(FlaskForm):
    submit = SubmitField('Update')

class ServicesSnmp(FlaskForm):
    submit = SubmitField('Update')

class SystemDeviceMaintenance(FlaskForm):
    submit = SubmitField('Update')

class SystemLog(FlaskForm):
    submit = SubmitField('Update')

class SystemStatus(FlaskForm):
    submit = SubmitField('Update')

class SystemStatistics(FlaskForm):
    submit = SubmitField('Update')

class GraylogStatus(FlaskForm):
    submit = SubmitField('Update')

class AlertsMonitor(FlaskForm):
    submit = SubmitField('Update')

class ComponentUpgrade(FlaskForm):
    submit = SubmitField('Update')
