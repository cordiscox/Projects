# create_tables.py
from app import create_app, db
from models import User, Ranking, Game  # Asegúrate de que el modelo esté importado
import requests
import random
from faker import Faker

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Tables created.")

fake = Faker()
url = f"https://www.mmobomb.com/api1/games?platform=pc&sort-by=relevance"

try:
    response = requests.get(url, verify=True)
    all_games = response.json()
    
    count = 0
    with app.app_context():
        for game in all_games:
            if count < 10:
                new_game = Game(title = game["title"], img = game["thumbnail"])
                db.session.add(new_game)
                db.session.commit()
                count += 1
            else:
                break

        ranking_data = {
            'user_name': [fake.name() for _ in range(200)],
            'id_game': [fake.random_digit() for _ in range(200)],
            'score': [fake.random_number(digits=5) for _ in range(200)]
        }


        for user_name, id_game, score in zip(ranking_data['user_name'], ranking_data['id_game'], ranking_data['score']):
            ranking_entry = Ranking(user_name=user_name, id_game=id_game, score=score)
            db.session.add(ranking_entry)
            db.session.commit()
         
    print("Games and Ranking created.")

except requests.exceptions.RequestException as e:
    print(e)   








