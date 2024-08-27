from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/dashboard')
def dashboard():
    # Logic for displaying the dashboard based on the user's role
    return render_template('dashboard/applicant_dashboard.html')  # Update based on user role
