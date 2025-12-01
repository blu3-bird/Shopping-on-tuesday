#app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config
import os

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app(config_name = 'default'):

    app = Flask(__name__)

    app.config.from_object(config[config_name])

    instance_path = os.path.join(app.root_path,'..','instance')

    if not os.path.exists(instance_path):
        os.makedirs(instance_path)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page'

    @login_manager.user_loader
    def load_user(user_id):
        """to get Admin object"""
        from app.models import Admin
        return Admin.query.get(int(user_id))

    from app.main.routes import main
    from app.auth.routes import auth
    from app.admin.routes import admin

    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')

    # Custom error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        """Custom 404 error page"""
        from flask import render_template
        return render_template('error/404.html'), 404

    with app.app_context():
        db.create_all()

        return app