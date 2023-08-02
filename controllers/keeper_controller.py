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
    beast_id = request.form["beast"]
    beast = Beast.query.get(beast_id)
    beast.keeper_id = id
    db.session.commit() 
    return redirect(f'/keepers/{id}')



@keepers_blueprint.route("/keepers/<keeper_id>/beasts/<beast_id>/delete", methods=['POST'])
def delete_beast_from_keeper(keeper_id, beast_id):
    Beast.query.filter_by(id=beast_id).delete()
    db.session.commit()
    return redirect(f"/keepers/{keeper_id}")