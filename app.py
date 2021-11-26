import requests
from bs4 import BeautifulSoup
from flask import Flask

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
	link_globo = pega_link()
	return f"""
	<h1>Sobre</h1>
	<a href="/">Home</a>
	<a href="/sobre">Sobre</a>
	<p>Este link foi coletado: </br> {link_globo}</p>
	<p>Este site foi criado por gabriela.</p>
	<p>teste</p>
	"""
from flask import request
import requests

@app.route("/telegram", methods = ["POST"])
def telegram():
	link_globo = pega_link()
	# processa mensagem
	update = request.json
	chat_id = update["message"]["chat"]["id"]
	text = update["message"]["text"].lower()
	if text in ["oi", "ola", "olar", "olá"]:
		answer = "Oi! Como vai?"
	elif text in ["bom dia", "boa tarde", "boa noite"]:
		answer = text
	elif "globo.com" in text:
		answer = f"segue o link: {link_globo}"
	else:
		answer = "Nao entendi"
	
	# responde
	token = "2134084726:AAEIypTzacglN21GzeTNy1qn3onQzShIt30"
	mensagem = {"chat_id": update["message"]["chat"]["id"], "text": answer}
	endpoint = "sendMessage"
	url = f"https://api.telegram.org/bot{token}/{endpoint}"
	requests.post(url, data = mensagem)
	return "ok"
