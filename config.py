class Config(object):
    DEBUG = True
    SECRET_HERE = 'JoAN_ROUTing!@$%)*&*&^%#'
    PWD_HASH_SALT = b'Actio_COURSEWOrk!'
    PWD_HASH_ITERATIONS = 77777
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False  # Выключаем ASCII чтобы получать норм. символы через jsonify
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}  # Выключаем ASCII чтобы получать норм. символы через API