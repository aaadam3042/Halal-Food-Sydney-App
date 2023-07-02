from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
    
class Charity(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    logoURL = db.Column(db.String, nullable=False)
    storefrontURL = db.Column(db.String, nullable=True)
    adminFees = db.Column(db.Boolean, nullable=True)
    distribution = db.Column(db.Boolean, nullable=True)

    def __repr__(self):
        return f"<Charity {self.name}>"
    
class Contact(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    charityID = db.Column(db.Integer, db.ForeignKey('charity.id'), nullable = False)
    type = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Contact {self.type}: {self.value}>"
    
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Category {self.name}>"

class CharityCategory(db.Model):
    charityID = db.Column(db.Integer, db.ForeignKey('charity.id'), primary_key=True)
    categoryID = db.Column(db.Integer, db.ForeignKey('category.id'), primary_key=True)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    charityID = db.Column(db.Integer, db.ForeignKey('charity.id'), primary_key=True)
    street = db.Column(db.String, nullable=False)
    suburb = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
