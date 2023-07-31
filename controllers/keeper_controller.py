from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models import Keeper, Beast, MagicalAilment, Treatment
from app import db

keepers_blueprint = Blueprint("keepers", __name__)

@keepers_blueprint.route("/keepers")
def keepers():
    keepers = Keeper.query.all()
    return render_template("keepers/index.jinja", keeper=keepers)

@keepers_blueprint.route("/keepers/<id>")
def show_keepers(id):
    keeper = Keeper.query.get(id)
    beasts = Beast.query.all()
    return render_template("keepers/show.jinja", keeper=keeper, beasts=beasts)

@keepers_blueprint.route("/keepers/<id>/add_beast", methods=['POST'])
def add_beast_to_keeper():
    beast_id = request.form("beast_id")
    new_beast = Beast(beast_id = beast_id)
    db.session.add(new_beast)
    db.session.commit
    return redirect("keeper/<id>")