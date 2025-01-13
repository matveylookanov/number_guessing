from flask import Blueprint, jsonify, request
from app.models import Game
from app import db

api_bp = Blueprint("api", __name__)

@api_bp.route("/game", methods=["GET"])
def get_game():
    game = Game.query.first()
    if game:
        return jsonify(game.to_dict())
    return jsonify({"error": "No game found"}), 404

@api_bp.route("/game/<int:id>", methods=["GET"])
def get_game_by_id(id):
    game = Game.query.get(id)
    if game:
        return jsonify(game.to_dict())
    return jsonify({"error": "Game not found"}), 404
