from flask import Flask
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from config import BaseConfig
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_folder="./static/dist", template_folder="./static")

app.config.from_object(BaseConfig)
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
bcrypt = Bcrypt(app)
