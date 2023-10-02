from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)

# create blueprints
hero_bp = Blueprint('heros', __name__)
power_bp = Blueprint('powers', __name__)
heropower_bp = Blueprint('hero_power', __name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hero.db'
db=SQLAlchemy(app)
migrate = Migrate(app, db)


