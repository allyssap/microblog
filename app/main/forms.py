from flask import request
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, SelectField, PasswordFi, FileField
from wtforms.validators import ValidationError, DataRequired, Length, Regexp, EqualTo
from flask_babel import _, lazy_gettext as _l
from app.models import User

class SecurityForm(FlaskForm):
    question = SelectField('Question', choices=[("What is your mother's maiden name?", "What is your mother's maiden name?"),
                ("What was your first pet's name?", "What was your first pet's name?"),
                ("What was your high schools mascot?", "What was your high schools mascot?"),
                ("What city did your parents meet in?", "What city did your parents meet in?")])
    answer = TextAreaField(_l('Answer'), validators=[DataRequired()], render_kw={"rows": 1, "cols": 32})
    submit = SubmitField(_l('Submit'))

class EditPost(FlaskForm):
    edit = TextAreaField(_l('Edit'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

class DeleteAccount(FlaskForm):
    password = PasswordField(_l('Current Password'), validators=[DataRequired()])
    submit = SubmitField('Delete')
    back = SubmitField('Nevermind')

class UploadPic(FlaskForm):
    image = FileField('Image', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Upload'

class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))

class ChangePass(FlaskForm):
    current_password = PasswordField(_l('Current Password'), validators=[DataRequired()])
    new_password = PasswordField(_l('New Password'), validators=[DataRequired(),
             Regexp(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'), EqualTo('confirm_password',
             message='Passwords must match')])
    confirm_password = PasswordField(_l('Confirm Password'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    product = TextAreaField(_l('Product'), validators=[DataRequired()], render_kw={"rows": 1, "cols": 32})
    company = TextAreaField(_l('Company'), validators=[DataRequired()], render_kw={"rows": 1, "cols": 32})
    category = SelectField('Category', choices=[('Electronics', 'Electronics'), ('Furniture', 'Furniture'),
                ('Books', 'Books'), ('Clothes','Clothes'), ('Makeup','Makeup'),
                ('Toys','Toys'), ('Games','Games'), ('Tools', 'Tools'), ('Other', 'Other')])
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'meta' not in kwargs:
            kwargs['meta'] = {'csrf': False}
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))
