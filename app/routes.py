from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Game
from app import db
import random

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    game = Game.query.first()

    if request.method == "POST":
        guess = int(request.form["guess"])
        if guess == game.number:
            game.attempts += 1
            db.session.commit()
            return render_template("win.html", game=game)
        elif guess < game.number:
            message = "Too low!"
        else:
            message = "Too high!"

        game.attempts += 1
        db.session.commit()
        return render_template("index.html", game=game, message=message)

    if not game:
        new_game = Game(number=random.randint(1, 100), attempts=0)
        db.session.add(new_game)
        db.session.commit()
        game = new_game

    return render_template("index.html", game=game)
