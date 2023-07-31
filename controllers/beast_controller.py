from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models import Keeper, Beast, MagicalAilment, Treatment
from app import db

beasts_blueprint = Blueprint("beasts", __name__)


@beasts_blueprint.route("/beasts")
def beasts():
    beasts = Beast.query.all()
    return render_template("beasts/index.jinja", beasts=beasts)