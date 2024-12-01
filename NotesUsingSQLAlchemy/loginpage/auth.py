from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully !', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.notes'))

            else:
                flash('Wrong Password')
        else:
            flash('User Doesnt Exsists')
    return render_template('login.html', boolean=True)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        cpassword = request.form.get('cpassword')

        if len(email) < 4:
            flash('Email must be greater than 4 charcters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 2 charcters.', category='error')
        elif password != cpassword:
            flash('Password must match', category='error')
        elif len(cpassword) <7:
            flash('Password name must be greater than 7 charcters.', category='error')
        else:
            new_user = User(email=email, password=generate_password_hash(password), first_name=username, )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Accout Created !', category='success')
            return redirect(url_for('auth.login'))
    return render_template('signup.html')