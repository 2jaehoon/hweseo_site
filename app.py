from flask import Flask, render_template
import json

app = Flask(__name__)

def load_goods():
	try:
		with open("goods.json", "r", encoding="utf-8") as f:
			return json.load(f)
	except:
		return []

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/goods")
def goods():
	items = load_goods()
	return render_template("goods.html", goods=items)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)
