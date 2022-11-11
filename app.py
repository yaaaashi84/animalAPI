from flask import Flask
from flask import render_template
from flask import request
import requests
import json

app = Flask(__name__)


@app.route("/")
def choiced_animal():
    return render_template("index.html")


@app.route("/post", methods=["POST"])
def partner_animal():
    choice = request.form["animal"]
    if choice == "猫":
        partner = requests.get("https://api.thecatapi.com/v1/images/search")
        fig = json.loads(partner.text)[0]["url"]
    elif choice == "犬":
        partner = requests.get("https://dog.ceo/api/breeds/image/random")
        fig = json.loads(partner.text)["message"]
    else:
        partner = requests.get("https://randomfox.ca/floof/")
        fig = json.loads(partner.text)["image"]
    return render_template("display.html", fig=fig)


if __name__ == "__main__":
    app.run(debug=True)
