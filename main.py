#API - um lugar para disponibilizar reursos e/ou funcionalidades
#1 - Objetivo - criar uma api que disponibiliza a consulta, criação, edição de jogos
#2 - URL base - Local para qual estará fazendo as requisições - localhost
#3 - Endpoints -
# localhost/games(GET)
# localhost/games/id(GET)
# localhost/games/id(PUT)
# localhost/games/id(DELETE)

#4- Qual recurso

from flask import Flask, jsonify, request
from bd import games

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
@app.route('/games', methods=['GET'])
def get_games():
    return (jsonify(message='Games List', data=games)
    )

@app.route('/games', methods=['POST'])
def insert_game():
    game = request.json
    games.append(game)
    return (jsonify(message='game cadastred sucefully', Game=games)
    )

def delete_game():
    game = request.json
    games.remove()

app.run()