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

@app.route('/games/<int:id>', methods=['GET'])
def find_game_id(id):
    for game in games:
        if game.get('id') == id:
            return jsonify(game)

@app.route('/games/<int:id>',methods=["PUT"])
def game_edit_id(id):
    edited_game = request.get_json()
    for key, game in enumerate(games):
        if game.get('id') == id:
            games[key].update(edited_game)
        return jsonify(games)

@app.route('/games/<int:id>',methods=["DELETE"])
def game_delete_id(id):
    for key, game in enumerate(games):
        if game.get('id') == id:
            del games[key]
    return jsonify(games)

app.run()