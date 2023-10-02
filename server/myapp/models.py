from myapp import db
from datetime import datetime
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heros'

    serialize_rules = ('-powers.heropowers', '-heropowers.power')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name =db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)

    powers = db.relationship('Power', secondary='hero_power', back_populates='heroes')
    heropowers = db.relationship('HeroPower', back_populates='hero')

    
class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    serialize_rules = ('-heroes.powers', '-heropowers.hero')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)

    heroes = db.relationship('Hero', secondary='hero_power', back_populates='powers')
    heropowers = db.relationship('HeroPower', back_populates='power')

    @validates('description')
    def validate_description(self, key,description):
        if len(description) < 20:
            raise ValueError('description must be 20 characters long')
        else:
            return description


class HeroPower(db.Model, SerializerMixin):
      __tablename__ = 'hero_power'

      serialize_rules = ('-hero.powers', '-power.heroes')

      id = db.Column(db.Integer, primary_key=True)
      hero_id = db.Column(db.Integer, db.ForeignKey('heros.id'))
      power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
      strength= db.Column(db.String)
      created_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
      updated_at = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)

      hero = db.relationship('Hero', back_populates = 'heropowers')
      power = db.relationship('Power', back_populates = 'heropowers')

      @validates('strength')
      def validate_strength(self,key,strength):
          allowed_strengths = ['Strong', 'Weak','Average']
          if strength not in allowed_strengths:
              raise ValueError(f"strength must be one of {','.join(allowed_strengths)}")
          return strength
              
