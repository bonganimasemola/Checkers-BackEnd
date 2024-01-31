from flask import Flask, jsonify,request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, user, game
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

CORS(app)

db.init_app(app)

migrate = Migrate(app, db)

CORS(app)

original_board = [
    [" ", "W", " ", "W", " ", "W", " ", "W"],
    ["W", " ", "W", " ", "W", " ", "W", " "],
    [" ", "W", " ", "W", " ", "W", " ", "W"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["B", " ", "B", " ", "B", " ", "B", " "],
    [" ", "B", " ", "B", " ", "B", " ", "B"],
    ["B", " ", "B", " ", "B", " ", "B", " "]
]

@app.route("/user", methods = [ 'POST' ])
def create_user():
    data=request.get_json()
    username=data[ 'username']
    password=data[password]
    
    user=user.query.filter_by(username=username).first()
    
    if user:
        return jsonify({'error': True,'message': 'Cant create user user exists'}), 400
    
    json_board =json.dumps (original_board)
    game=Game(board=json_board)
    db.session.add(game) 
    db.session.commit()
    new_user = User(username=username, password=password, game_id=game.id)
    db. session.add(new_user) 
    db.session.commit()
    return jsonify({'id': new_user.id, 'game': game.id})

@app.route("/board/<int:id>", methods = ["GET" ])
def get_board(id):
    user=user.query.filter_by(id=id).first()
    game=json.loads(user.game.board)
    print (game)
    return "jsonify(user)"



if __name__ == '__main__':
    app.run(port=5555, debug=True)
