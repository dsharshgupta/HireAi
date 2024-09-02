from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from ..models import User
from .. import db
from app import login_manager
from flask_login import login_user,logout_user
bp = Blueprint('auth', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful!')
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Check your email and/or password.')
    return render_template('login.html')
@bp.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')

@bp.route('/register', methods=['POST','GET'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    role = request.form['role']
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()
    flash('Registration successful! You can now log in.')
    return redirect(url_for('auth.login'))
