from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models import Keeper, Beast, MagicalAbility, BeastAbility
from app import db

keepers_blueprint = Blueprint("keepers", __name__)

@keepers_blueprint.route("/keepers")
def keepers():
    keepers = Keeper.query.all()
    return render_template("keepers/index.jinja", keepers=keepers)