import os
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__,static_url_path='', static_folder='../client/dist', template_folder='../client/dist')

# create blueprints
hero_bp = Blueprint('heros', __name__)
power_bp = Blueprint('powers', __name__)
heropower_bp = Blueprint('hero_power', __name__)

app.config['SQLALCHEMY_DATABASE_URI']= os.environ.get('DATABASE_URI')
db=SQLAlchemy(app)
migrate = Migrate(app, db)


