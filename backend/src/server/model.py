from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry
from sqlalchemy.orm import relationship
db = SQLAlchemy() 

class Broadcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    message = db.Column(db.String, nullable=False)
    startDate = db.Column(db.Date, nullable=False)
    startTime = db.Column(db.Time, nullable=False)
    endDate = db.Column(db.Date, nullable=False)
    endTime = db.Column(db.Time, nullable=False)
    isImportant = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return f"<Broadcast {self.title}>"
    
class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    salt = db.Column(db.String, unique=True, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"
    
class FoodService(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    lastContacted = db.Column(db.Date, nullable=True)
    notes = db.Column(db.String, nullable=True)

    type = db.Column(db.Integer, db.ForeignKey('service_type.id'), nullable=False)
    halalStatus = db.Column(db.Integer, db.ForeignKey('halal_status.id'), nullable=False)

    locations = relationship('Location', backref='food_service', cascade='all, delete')
    contact = relationship('Contact', backref='food_service', cascade='all, delete')
    statusHistory = relationship('StatusHistory', backref='food_service', cascade='all, delete')

    serviceSupplier = relationship('ServiceSupplier', backref='food_service', cascade='all, delete')
    foodServiceTagJunction = relationship('FoodServiceTagJunction', backref='food_service', cascade='all, delete')

    def __repr__(self):
        return f"<Food Service {self.name}>"

class ServiceType(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"<Food Service Type {self.name}>"
    
class FoodServiceTagJunction(db.Model): 
    serviceID = db.Column(db.Integer, db.ForeignKey('food_service.id'), primary_key=True)
    tagID = db.Column(db.Integer, db.ForeignKey('service_tag.id'), primary_key=True)

class ServiceTag(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    foodServiceTagJunction = relationship('FoodServiceTagJunction', backref='service_tag', cascade='all, delete')
    
    def __repr__(self):
        return f"<Food Service Tag {self.name}>"
    
class HalalStatus(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"<Halal Status {self.name}>"
    
class ServiceSupplier(db.Model):
    serviceID = db.Column(db.Integer, db.ForeignKey('food_service.id'), primary_key=True)
    supplierID = db.Column(db.Integer, db.ForeignKey('supplier.id'), primary_key=True)
    
class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    notes = db.Column(db.String, nullable=True)

    supplier = relationship('ServiceSupplier', backref='supplier', cascade='all, delete')

    def __repr__(self):
        return f"<Supplier {self.name}>"

class StatusHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serviceID = db.Column(db.Integer, db.ForeignKey('food_service.id'), nullable=False)
    halalStatus = db.Column(db.Integer, db.ForeignKey('halal_status.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return f"<Status History {self.date}: {self.halalStatus.name}>"
    
class Contact(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    serviceID = db.Column(db.Integer, db.ForeignKey('food_service.id'), nullable=False)
    type = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Contact {self.type}: {self.value}>"

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serviceID = db.Column(db.Integer, db.ForeignKey('food_service.id'), nullable=False)
    street = db.Column(db.String, nullable=False)
    postCode = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    geom = db.Column(Geometry(geometry_type='POINT', srid=4326), nullable=True)

    def __repr__(self):
        return f"<Location {self.street}, {self.postCode}, {self.city}, {self.state}>"
