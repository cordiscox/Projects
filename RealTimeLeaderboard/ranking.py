# main.py

from flask import Blueprint, render_template, request

from models import Game, Ranking
from sqlalchemy import asc

ranking = Blueprint('ranking', __name__)


@ranking.route('/')
def index():
    games = Game.query.all()
    game_ids = [game.id for game in games[:4]]
    rankings_by_game = {}

    for game_id in game_ids:

        game = Game.query.get(game_id)
        
        # Obtener los primeros 10 rankings de cada juego
        top_rankings = Ranking.query.filter(Ranking.id_game == game_id)\
                                    .order_by(Ranking.score.desc())\
                                    .limit(10).all()
        rankings_by_game[game.title] = top_rankings

    return render_template('ranking.html', rankings=rankings_by_game) 