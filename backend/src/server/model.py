from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy() # TODO: MIGRATE AND UPGRADE

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(128), unique=True, nullable=False)
    salt = db.Column(db.String(128), unique=True, nullable=False)
    isAdmin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"
    
class service(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    halalStatus = db.Column(db.String, nullable=False)
    lastContacted = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Service {self.name}>"
    
class ServiceSupplier(db.Model):
    serviceID = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    supplierID = db.Column(db.Integer, db.ForeignKey('supplier.id'), primary_key=True)
    
class Supplier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Supplier {self.name}: {self.status}>"

class statusHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serviceID = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    halalStatus = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    
    def __repr__(self):
        return f"<Status History {self.date}: {self.halalStatus}>"
    
class Contact(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    serviceID = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    type = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Contact {self.type}: {self.value}>"

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serviceID = db.Column(db.Integer, db.ForeignKey('service.id'), primary_key=True)
    street = db.Column(db.String, nullable=False)
    suburb = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Location {self.street}, {self.suburb}, {self.state}>"
