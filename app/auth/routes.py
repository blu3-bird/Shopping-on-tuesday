"""
Authentication routes for admin users.

This module defines the routes responsible for handling admin login and logout
functionality. It includes logic for validating credentials, managing user
sessions, redirecting authenticated users, and ensuring secure access through
Flask-Login.

Routes:
    - /login: Display and process the admin login form.
    - /logout: Log out the currently authenticated admin user.
"""

# app/admin/routes.py
from flask import redirect, request, render_template, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.auth.forms import adminForm
from app.constants import ROUTE_ADMIN_DASHBOARD
from app.models import Admin
from app.auth import auth
from app import db

@auth.route('/login', methods=['GET','POST'])
def login():
    """
    Handle admin login functionality.

    Displays the login form (GET) and processes authentication (POST).
    Validates the admin's username and password, logs the user in on success,
    and redirects them to the appropriate dashboard or next requested page.

    If the user is already authenticated, they are redirected to the admin dashboard.

    Returns:
        Response: Rendered login page on GET or failed login.
        Response: Redirect to dashboard or next page on successful login.
    """

    # check if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for(ROUTE_ADMIN_DASHBOARD))
    
    form = adminForm()

    if form.validate_on_submit():

        admin = Admin.query.filter_by(username=form.username.data).first()

        if admin is None or not admin.check_password(form.password.data):
            flash("Invalid Username or Password",'error')
            return redirect(url_for('auth.login'))

        login_user(admin,remember=form.remember_me.data)
        flash(f'Welcome Back {admin.username}!','success')

        next_page = request.args.get('next')

        if next_page:
            return redirect(next_page)
        
        return redirect(url_for(ROUTE_ADMIN_DASHBOARD))
    
    return render_template('auth/login.html', form=form)
    
@auth.route('/logout')
@login_required
def logout():
    """
    Log out the current admin user.

    Logs the user out of the session, flashes a confirmation message,  
    and redirects them back to the main website index page.

    Returns:
        Response: Redirect to the main index page after logout.
    """
    flash('User has been successfully logout!','success')
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/arson',methods=['GET','POST'])
def create_admin():
    """Create new admin account"""

    from app.auth.forms import AdminCreateClass

    form = AdminCreateClass()

    if form.validate_on_submit():

        existing_user = Admin.query.filter_by(
            username = form.username.data
        ).first()

        if existing_user:
            flash('Username Already Taken','Error')
            return render_template('auth/create_admin.html',form=form)
        
        existing_email = Admin.query.filter_by(
            email = form.email.data
        ).first()

        if existing_email:
            flash('Email Address already Registered','error')

            return render_template('auth/create_admin.html',form=form)
        
        new_admin = Admin(username= form.username.data,email=form.email.data)

        new_admin.set_password(form.password.data)

        db.session.add(new_admin)
        db.session.commit()

        flash(f'User Account "{new_admin.username}" Created Successfully','success')

        return redirect(url_for('auth.login'))
    return render_template('auth/create_admin.html',form=form)