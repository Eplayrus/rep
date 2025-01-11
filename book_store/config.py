class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///book_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': 'DevelopmentConfig',
}
