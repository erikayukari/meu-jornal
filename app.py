from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "<p>Oi!</p>"

@app.route("/sobre")
def sobre():
	return "<h1>Sobre</h1><p>Este site foi criado por gabriela.</p>"
