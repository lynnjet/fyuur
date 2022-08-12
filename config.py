import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# using environment variables to hide importnant details of the url.

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_SERVER = os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}/{DB_NAME}"
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/fyyur_app'
SQLALCHEMY_TRACK_MODIFICATIONS = False




# class Config:
   
#     SQLALCHEMY_DATABASE_URI = 'postgresql://martin023:0000@localhost/fyyur_app'
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
#     SECRET_KEY = 'my_key'
#     UPLOADED_PHOTOS_DEST='app/static/photos'
    
    

# class ProdConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql://martin023:0000@localhost/fyyur_app'
#     if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
#         SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)



# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin023:0000@localhost/fyyur_app'


  

# class DevConfig(Config):
#     DEBUG = True


    

# config_options = {
#     'development': DevConfig,
#     'production': ProdConfig,
#     'test':TestConfig
    
# }