from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def main_page():
	return("<img src='http://flask.pocoo.org/docs/1.0/_static/flask.png' />")

@app.route("/enter", methods=["GET"])
def var_page():
	return str(request.args.get("cheese")) + ", " + str(request.args.get("onions"))

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
