from app import db

class Keeper(db.Model):
    __tablename__ = "keepers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    name_of_hold = db.Column(db.String(64))
    beasts = db.relationship('Beast', backref='keeper')

    def __repr__(self):
        return f"<Keeper: {self.name}: {self.name_of_hold}"

class Beast(db.Model):
    __tablename__ = "beasts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    dob = db.Column(db.DateTime())
    breed = db.Column(db.String(64))
    origin_country = db.Column(db.String(64))
    keeper_id = db.Column(db.Integer, db.ForeignKey('keepers.id'))


class MagicalAbility(db.Model):
    __tablename__ = "magical_abilities"

    id = db.Column(db.Integer, primary_key=True)
    ability = db.Column(db.String(64))
    description = db.Column(db.Text())

class BeastAbility(db.Model):
    __tablename__ = "beast_abilities"

    id = db.Column(db.Integer, primary_key=True)
    beast_id = db.Column(db.Integer, db.ForeignKey('beasts.id'))
    magical_ability_id = db.Column(db.Integer,db.ForeignKey('abilities.id'))