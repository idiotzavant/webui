from flask_wtf import FlaskForm
from wtforms import \
    StringField,\
    PasswordField,\
    BooleanField,\
    SubmitField,\
    SelectField
from wtforms.validators import DataRequired,IPAddress,Length

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
