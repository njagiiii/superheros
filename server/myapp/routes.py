from flask import jsonify, request,render_template
from myapp import app, db,hero_bp,power_bp,heropower_bp
from sqlalchemy.orm.exc import NoResultFound
from myapp.models import Hero, Power, HeroPower
from flask_restful import Resource, Api,abort



api = Api(app)

class HomeResource(Resource):
    def home(id=0):
        return render_template("index.html")
        # return{"message":"Hello World!"}
    
class Heros(Resource):
    def get(self):
        heros = Hero.query.all()
        hero_list = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heros]
        return jsonify(heros=hero_list)


class HeroIdResource(Resource):
    def get(self, id):
        hero = Hero.query.get(id)
        if hero is None:
            abort(404, error='Hero not found')

        hero_data = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [{'id': power.id, 'name': power.name, 'description': power.description} for power in hero.powers]
        }
        return jsonify(hero_data)

class Powers(Resource):
    def get(self):
        powers = Power.query.all()
        power_list = [{'id': power.id, 'name': power.name, 'description': power.description} for power in powers]
        return jsonify(powers=power_list)
    

class PowerIdResource(Resource):
    def get(self, id):
        power = Power.query.get(id)
        if power is None:
            abort(404, error='Power not found')

        power_data = {'id': power.id, 'name': power.name, 'description': power.description}
        return jsonify(power_data)

class PowerPatch(Resource):
    def patch(self, id):
        power = Power.query.get(id)

        if power is None:
            return {"message": "Power not found"}, 404

        data = request.get_json()

        if 'name' in data:
            power.name = data['name']

        if 'description' in data:
            power.description = data['description']

        db.session.commit()

        return {"message": "Power updated successfully", "power": power}

class HeroPowers(Resource):
    def post(self):
        data = request.get_json()

        hero_id = data['hero_id']
        power_id = data['power_id']
        strength = data['strength']

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if hero_id is None or power_id is None or strength is None:
            return jsonify({'error': 'Hero or power not found'}), 404

        new_heropower = HeroPower(hero=hero, power=power, strength=strength)
        db.session.add(new_heropower)
        db.session.commit()

        return {"message": "HeroPower created successfully"}
    

# register blueprints
app.register_blueprint(hero_bp, url_prefix ='/api/heroes')
app.register_blueprint(power_bp, url_prefix ='/api/powers')
app.register_blueprint(heropower_bp, url_prefix ='/api/hero_powers')

# Add resources
# api.add_resource(HomeResource, '/')
api.add_resource(HomeResource, '/<int:id>')
api.add_resource(Heros, '/heroes')
api.add_resource(HeroIdResource, '/heroes/<int:id>')
api.add_resource(Powers, '/powers')
api.add_resource(PowerIdResource, '/powers/<int:id>')
api.add_resource(PowerPatch, '/powers/<int:id>')
api.add_resource(HeroPowers, '/hero_powers')


