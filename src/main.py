"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Favorites, Vehicles, Planets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/People', methods=['GET'])
def get_all_characters():
    characters = People.query.all()
    characters_serialize = list(map(lambda x: x.serialize(),characters))
    return jsonify({"response":characters_serialize}),200

@app.route('/People/<int:people_id>', methods=['GET'])
def get_one_character(people_id):
    character = People.query.get(people_id)
    return jsonify({"response":character.serialize()}),200

@app.route('/Planets', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    planets_serialize = list(map(lambda x: x.serialize(),planets))
    return jsonify({"response":planets_serialize}),200

@app.route('/Planets/<int:planet_id>', methods=['GET'])
def get_one_planet(planet_id):
    planet = Planets.query.get(planet_id)
    return jsonify({"response":planet.serialize()}),200

@app.route('/Vehicles', methods=['GET'])
def get_all_vehicles():
    vehicles = Vehicles.query.all()
    vehicles_serialize = list(map(lambda x: x.serialize(),vehicles))
    return jsonify({"response":vehicles_serialize}),200

@app.route('/Vehicles/<int:vehicle_id>', methods=['GET'])
def get_one_vehicle(vehicle_id):
    vehicle = Vehicles.query.get(vehicle_id)
    return jsonify({"response":vehicle.serialize()}),200

@app.route('/Users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_serialize = list(map(lambda x: x.serialize(),users))
    return jsonify({"response":users_serialize}),200

@app.route('/User/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user = User.query.get(user_id)
    return jsonify({"response":user.serialize()}),200

@app.route('/Users', methods=['POST'])
def create_user():
    body_name=request.json.get("name")
    body_nick=request.json.get("nick")
    body_email=request.json.get("email")
    body_password=request.json.get("password")
    user=User(name=body_name, nick=body_nick, email=body_email, password=body_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"name":user.name, "nick":user.nick, "email":user.email, "password":user.password, "msg":"Usuario creado"}),200

@app.route('/Users/favorites', methods=['GET'])
def get_user_favorites():
    favorites = Favorites.query.all()
    favorites_serialize = list(map(lambda x: x.serialize(),favorites))
    return jsonify({"response":favorites_serialize}),200

@app.route('/favorites/<int:user_id>/planet/<int:planet_id>', methods=['POST'])
def add_planet_favorite(user_id,planet_id):
    fav_planet= Favorites(user_id= user_id ,planets_id= planet_id)
    db.session.add(fav_planet)
    db.session.commit()
    return jsonify({"favourite_planet":fav_planet.serialize(), "msg":"Planeta favorito agregado"}),200

@app.route('/favorites/<int:user_id>/people/<int:people_id>', methods=['POST'])
def add_people_favorite(user_id,people_id):
    fav_people= Favorites(user_id= user_id, char_id= people_id)
    db.session.add(fav_people)
    db.session.commit()
    return jsonify({"favourite_char":fav_people.serialize(), "msg":"Personaje favorito agregado"}),200

@app.route('/favorites/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet_favorite(planet_id):
    del_fav_planet= Favorites.query.filter_by(planets_id = planet_id).first()
    db.session.delete(del_fav_planet)
    db.session.commit()
    return jsonify({"deleted":True}),200

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def del_people_fav(people_id):
    del_fav_people= Favorites.query.filter_by(char_id=people_id).first()
    db.session.delete(del_fav_people)
    db.session.commit()
    return jsonify({"deleted":True}),200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
