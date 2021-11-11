from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
	return """
	<h1>Home</g1>
	<a href="/">Home</a>
	<a href="/sobre">Sobre</a>
	"""

@app.route("/sobre")
def sobre():
	return """
	<h1>Sobre</h1>
	<a href="/">Home</a>
	<a href="/sobre">Sobre</a>
	<p>Este site foi criado por gabriela.</p>
	"""
