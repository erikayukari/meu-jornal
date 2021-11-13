import requests
from flask import Flask
from bs4 import BeautifulSoup

def pega_link():
  url = "https://www.globo.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  link_globo = soup.find('a', class_ = 'post__link').attrs['href']
  return link_globo

app = Flask(__name__)

@app.route("/")
def hello_world():
	arquivo = open("templates/home.html")
	return arquivo.read()

@app.route("/sobre")
def sobre():
	return f"""
	<h1>Sobre</h1>
	<a href="/">Home</a>
	<a href="/sobre">Sobre</a>
	<p>Este link foi coletado: </br> {link_globo}</p>
	<p>Este site foi criado por gabriela.</p>
	<p>teste</p>
	"""
