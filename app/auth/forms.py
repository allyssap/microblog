from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Regexp
from flask_babel import _, lazy_gettext as _l
from app.models import User

class AccountSecurityCheck(FlaskForm):
    username = TextAreaField(_l('Enter your username'), validators=[DataRequired()], render_kw={"rows": 1, "cols": 64})
    submit = SubmitField(_l('Submit'))

class QuestionSecurityCheck(FlaskForm):
    question = StringField(_l('Question'), validators=[DataRequired()])
    answer = TextAreaField(_l('Answer'), validators=[DataRequired()], render_kw={"rows": 1, "cols": 32})
    submit = SubmitField(_l('Submit'))

class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    submit = SubmitField(_l('Sign In'))


class OneTimeLinkForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    submit = SubmitField(_l('Confirm & Back to OTP'))


class VerificationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired()])
    submit = SubmitField(_l('Verification & Sign In'))

class OTPForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    OTP = StringField(_l('OTP'), validators=[DataRequired()]) ###EqualTo(otp)
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Log in') )

class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_l('Password'), validators=[DataRequired(), Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different username.'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('Please use a different email address.'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l('Request Password Reset'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(
        _l('Repeat Password'), validators=[DataRequired(),
                                           EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))
