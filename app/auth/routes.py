#app/admin/routes.py
from flask import redirect, request, render_template, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from app.auth.forms import adminForm
from app.models import Admin
from app.auth import auth


@auth.route('/login', methods=['GET','POST'])
def login():
    """super admin route"""

    # check if user is already logined in
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    
    form = adminForm()

    if form.validate_on_submit():

        admin = Admin.query.filter_by(username=form.username.data).first_or_404()

        if admin is None or not admin.check_password(form.password.data):
            flash("Invalid Username or Password",'error')
            return redirect(url_for('auth.login'))

        login_user(admin,remember=form.remember_me.data)
        flash(f'Welcome Back {admin.username}!','success')

        next_page = request.args.get('next')

        if next_page:
            return redirect(url_for(next_page))
        
        return redirect(url_for('admin.dashboard'))
    return render_template('auth/login.html', form=form)
    
@auth.route('/logout')
@login_required
def logout():
    flash('User has been successfully logout!','success')
    logout_user()
    return redirect(url_for('main.index'))
