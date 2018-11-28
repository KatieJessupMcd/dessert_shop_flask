from flask import Flask, render_template, jsonify, request
from desserts import dessert_list

app = Flask(__name__)


@app.route("/")
def home():
    """Return home page with basic info"""

    return render_template("index.html")

@app.route("/desserts")
def show_desserts():

   return jsonify(dessert_list.serialize())

@app.route("/desserts", methods = ["POST"])
def post_desserts():
    user_data = request.json
    dessert_list.add(user_data['name'], user_data['description'], user_data['calories'])

    return  jsonify(dessert_list.desserts[-1].serialize())
