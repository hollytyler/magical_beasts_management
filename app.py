from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://holly@localhost:5432/magical_beasts"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.beast_controller import beasts_blueprint
from controllers.keeper_controller import keepers_blueprint
from models import Keeper, Beast

app.register_blueprint(beasts_blueprint)
app.register_blueprint(keepers_blueprint)

@app.route("/")
def home():
    return render_template("index.jinja", title="Magical Beasts and Where We Mend Them")

if __name__ == '__main__':
    app.run(debug=True)