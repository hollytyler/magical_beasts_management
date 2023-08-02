from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models import Keeper, Beast
from app import db

beasts_blueprint = Blueprint("beasts", __name__)


@beasts_blueprint.route("/beasts")
def beasts():
    beasts = Beast.query.all()
    return render_template("beasts/index.jinja", beasts=beasts)

@beasts_blueprint.route("/beasts/<id>")
def show_beast(id):
    beast = Beast.query.get(id)
    return render_template("beasts/show.jinja", beast=beast)

@beasts_blueprint.route("/beasts/new")
def add_beasts():
    keepers = Keeper.query.all()
    return render_template("beasts/new.jinja", keepers=keepers)

@beasts_blueprint.route("/beasts/new", methods=["POST"])
def create_beast():
    name = request.form['name']
    dob = request.form['dob']
    species = request.form['species']
    ailment = request.form['ailment']
    keeper_id = request.form['keeper']
    beast = Beast(name=name, dob=dob, species=species, ailment=ailment, keeper_id=keeper_id)
    db.session.add(beast)
    db.session.commit()
    return redirect("/beasts")

@beasts_blueprint.route("/beasts/<id>/delete", methods=['POST'])
def delete_beast(id):
    Beast.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect("/beasts")

@beasts_blueprint.route("/beasts/<id>/edit")
def edit_beast(id):
    keepers = Keeper.query.all()
    beast = Beast.query.get(id)
    return render_template("beasts/edit.jinja", keeper=keepers, beast=beast)

@beasts_blueprint.route('/beasts/<id>', methods=['POST'])
def update_beast(id):
    ailment = request.form['ailment']
    treatment = request.form['treatment']
    keeper_id = request.form['keeper_id']
    beast = Beast.query.get(id)
    beast.ailment = ailment
    beast.keeper_id = keeper_id
    beast.treatment = treatment
    db.session.commit()
    return redirect(f"/beasts/{id}")
