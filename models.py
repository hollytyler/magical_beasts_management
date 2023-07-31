from app import db

class Keeper(db.Model):
    __tablename__ = "keepers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    name_of_hold = db.Column(db.String(64))
    beasts = db.relationship('Beast', backref='keeper')

    def __repr__(self):
        return f"Keeper {self.id}: {self.name}"

class Beast(db.Model):
    __tablename__ = "beasts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    dob = db.Column(db.String(64))
    species = db.Column(db.String(64))
    native_to = db.Column(db.String(64))
    keeper_id = db.Column(db.Integer, db.ForeignKey('keepers.id'))
    treatments = db.relationship('Treatment', backref='beast')

    def __repr__(self):
        return f"Beast {self.id}: {self.name}"


class MagicalAilment(db.Model):
    __tablename__ = "magical_ailments"

    id = db.Column(db.Integer, primary_key=True)
    treatment_type= db.Column(db.String(64))
    treatments = db.relationship('Treatment', backref='magical_ailments')

class Treatment(db.Model):
    __tablename__ = "treatments"

    id = db.Column(db.Integer, primary_key=True)
    beast_id = db.Column(db.Integer, db.ForeignKey('beasts.id'))
    magical_ailment_id = db.Column(db.Integer,db.ForeignKey('magical_ailments.id'))