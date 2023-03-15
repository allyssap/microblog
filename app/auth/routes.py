from flask import render_template, redirect, url_for, flash, request, session
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from flask_babel import _
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, \
    ResetPasswordRequestForm, ResetPasswordForm, QuestionSecurityCheck, AccountSecurityCheck
from app.models import User
from app.auth.email import send_password_reset_email

@bp.route('/get_user', methods=['GET', 'POST'])
def get_user():
    form = AccountSecurityCheck()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            flash(_('Invalid username or password'))
            return redirect(url_for('auth.login'))
        elif user.sec_question == 'NULL' or user.sec_answer == 'NULL':
            flash(_('This account does not have its security question set.'))
            return redirect(url_for('auth.login'))
        else:
            session['username'] = form.username.data
            return redirect(url_for('auth.answer_sec'))
    return render_template('auth/get_user.html', title=_('Username'), form=form)

@bp.route('/answer_sec', methods=['GET', 'POST'])
def answer_sec():
    user_name = session.get('username')
    if user_name is None:
        return redirect(url_for('auth.login'))
    else:
        user = User.query.filter_by(username=user_name).first()
        form = QuestionSecurityCheck()
        form.question.data = user.sec_question
        if form.validate_on_submit():
            if form.answer.data == user.sec_answer:
                login_user(user)
                return redirect(url_for('main.login'))
            else:
                flash(_('Invalid answer'))
                return redirect(url_for('auth.login'))
    return render_template('auth/answer_sec.html', title=_('Security Question'), form=form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('auth/login.html', title=_('Sign In'), form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Congratulations, you are now a registered user!'))
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title=_('Register'),
                           form=form)


@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(
            _('Check your email for the instructions to reset your password'))
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html',
                           title=_('Reset Password'), form=form)


@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_('Your password has been reset.'))
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)
