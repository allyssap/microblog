from flask import render_template, current_app
from flask_babel import _
from app.email import send_email
import math, random


# def generate_otp(user):
#     # Declare a digits variable
#     # which stores all digits
#     digits = "0123456789"
#     otp = ""
#     # length of password can be changed
#     # by changing value in range
#     for i in range(4):
#         otp += digits[math.floor(random.random() * 10)]
#     user.otp = otp
#     return otp

def send_otp_email(user):
    # ## generate_otp(user)
    # user.otp = "1234"
    otp = '1234'
    send_email(_('[Microblog] Your one time passcode'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/otp.txt',
                                         user=user, otp=otp, link ='auth/verificationlink.html'),
               html_body=render_template('email/otp.html',
                                         user=user, otp=otp))
    return otp

def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(_('[Microblog] Reset Your Password'),
               sender=current_app.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',
                                         user=user, token=token),
               html_body=render_template('email/reset_password.html',
                                         user=user, token=token))
