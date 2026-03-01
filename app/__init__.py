#app/__init__.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from config import config
import os

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app(config_name='default'):

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config["INSTAGRAM_URL"] = "https://instagram.com/blu3_bird_"

   
    instance_path = os.path.join(app.root_path, '..', 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)

    
    upload_path = app.config.get('UPLOAD_FOLDER')
    if upload_path and not os.path.exists(upload_path):
        os.makedirs(upload_path)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page'

    @login_manager.user_loader
    def load_user(user_id):
        """To get Admin object"""
        from app.models import Admin
        return Admin.query.get(int(user_id))

    
    from app.main import main
    from app.auth import auth
    from app.admin import admin

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(admin, url_prefix='/admin')
    app.register_blueprint(auth, url_prefix='/auth')

    
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/500.html"), 500
    
    
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/400.html'), 404

    
    return app