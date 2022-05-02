from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()

    
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    nick = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False )
    email = db.Column(db.String(250), nullable=False, unique=True)
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "nick": self.nick,
            "password": self.password,
            "email": self.email
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favourite_user = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('Users')
    favourite_char = db.Column(db.Integer, db.ForeignKey('characters.id'))
    character = db.relationship('Characters')
    favourite_planets = db.Column(db.Integer, db.ForeignKey('planets.id'))
    planets = db.relationship('Planets')
    favourite_vehicles = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    vehicles = db.relationship('Vehicles')

    def serialize(self):
        return {
            "id": self.id,
            "favorite_user": self.favourite_user,
            "favorite_char": self.favourite_char,
            "favorite_planets": self.favourite_planets,
            "favorite_vehicles": self.favourite_vehicles
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    height= db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "height": self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(250))
    diameter = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250))
    gravity = db.Column(db.String(250))
    population = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    surface_water = db.Column(db.String(250))
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water
        }


class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250))
    description = db.Column(db.String(250))
    starship_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.String(250))
    length = db.Column(db.String(250))
    crew = db.Column(db.String(250))
    passengers = db.Column(db.String(250))
    max_atmosphering_speed = db.Column(db.String(250))
    hyperdrive_rating = db.Column(db.String(250))
    MGLT = db.Column(db.String(250))
    cargo_capacity = db.Column(db.String(250))
    consumables = db.Column(db.String(250))
    pilots = db.Column(db.String(250))
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "starship_class": self.starship_class,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "passengers": self.passengers,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "pilots": self.pilots
        }