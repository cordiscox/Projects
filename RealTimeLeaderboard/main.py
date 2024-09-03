# main.py

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from models import Game, Ranking
from sqlalchemy import asc

main = Blueprint('main', __name__)

@main.route('/')
def index():
    games = Game.query.all()
    all_games = {game.id: game for game in games}
    game_ids = [game.id for game in games[:4]]
    rankings_by_game = {}

    for game_id in game_ids:

        game = Game.query.get(game_id)
        
        # Obtener los primeros 10 rankings de cada juego
        top_rankings = Ranking.query.filter(Ranking.id_game == game_id)\
                                    .order_by(Ranking.score.desc())\
                                    .limit(10).all()
        rankings_by_game[game.title] = top_rankings

        # Obtener el ranking más alto del usuario logueado para este juego
        #highest_ranking = Ranking.query.filter(Ranking.id_game == game_id, Ranking.user_id == logged_in_user_id)\
        #                                .order_by(Ranking.score.desc()).first()
        #user_highest_rankings.append(highest_ranking)

    return render_template('index.html', all_games=all_games, rankings=rankings_by_game) 


#, user_highest_rankings=user_highest_rankings)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/submit_score', methods=['GET', 'POST'])
def submit_score():
    games = Game.query.all()  # Supongamos que tienes un modelo Game
    if request.method == 'POST':
        game_id = request.form.get('game')
        score = int(request.form.get('score'))
        # Aquí puedes manejar el guardado del puntaje
    return render_template('submit_score.html', games=games)