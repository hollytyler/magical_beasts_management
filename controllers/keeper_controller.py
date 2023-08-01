from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models import Keeper, Beast
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

@keepers_blueprint.route("/keepers/<id>/add", methods=['POST'])
def add(id):
    beast_id = request.form("beasts")
    Beast.query.get(id) # get the beast by id
    beast = Beast(keeper_id=beast_id)
    # set its keeper_id to id
    db.session.commit(beast) # commit
    return redirect('/keepers/<id>')