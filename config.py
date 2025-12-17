import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-in-production'

        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance' , 'arson.db')

        SQLALCHEMY_TRACK_MODIFICATION = False

        UPLOAD_FOLDER = os.path.join(basedir,'app','static','uploads')

        MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5mb

        ALLOWED_EXTENSIONS = {
        'png','jpg','jpeg','gif', 'webp'
        }

class DevelopmentConfig(Config):
            DEBUG = True

class ProductionConfig(Config):
            DEBUG = False


config ={
    'development': DevelopmentConfig,
    'production' : ProductionConfig,
    'default': DevelopmentConfig
}


INSTAGRAM_URL = "https://instagram.com/blu3_bird_"
