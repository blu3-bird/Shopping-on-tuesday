import os
from dotenv import load_dotenv

load_dotenv()



basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

        SECRET_KEY = os.environ.get('SECRET_KEY')

        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance' , 'arson.db')

        SQLALCHEMY_TRACK_MODIFICATIONS = False

        UPLOAD_FOLDER = os.path.join(basedir,'app','static','uploads')

        MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5mb

        ALLOWED_EXTENSIONS = {
        'png','jpg','jpeg','gif', 'webp'
        }

class DevelopmentConfig(Config):
            DEBUG = True

            if not Config.SECRET_KEY:
                    import warnings
                    warnings.warn(
                            "SECRET_KEY not set! Using insecure development key. "
                            "DO NOT use this in production!"
                    )
                    SECRET_KEY = 'dev-only-insecure-key-never-use-in-production'

class ProductionConfig(Config):
            DEBUG = False

            if not Config.SECRET_KEY:
                    raise ValueError(
                           " \n\n"
                        "========================================\n"
                        "ERROR: SECRET_KEY is not set!\n"
                        "..."
                    )


config ={
    'development': DevelopmentConfig,
    'production' : ProductionConfig,
    'default': DevelopmentConfig
}


INSTAGRAM_URL = "https://instagram.com/blu3_bird_"
