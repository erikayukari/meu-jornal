import requests
from bs4 import BeautifulSoup
from flask import Flask

# scrapers
def link_globo_com():
  url = "https://www.globo.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_globo_com = soup.find('a', class_ = 'post__link').attrs['href']
  return manchete_globo_com

def link_g1():
  url = "https://g1.globo.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  #print(soup)
  manchete_g1 = soup.find('a', class_ = 'feed-post-link gui-color-primary gui-color-hover').attrs['href']
  return manchete_g1

app = Flask(__name__)

@app.route("/")
def hello_world():
	arquivo = open("templates/home.html")
	return arquivo.read()

@app.route("/sobre")
def sobre():
	link_globo_com = link_globo_com()
	link_g1 = link_g1()
	return f"""
	<h1>Sobre</h1>
	<a href="/">Home</a>
	<a href="/sobre">Sobre</a>
	<p>Manchete da Globo.com: </br> {link_globo_com}</p>
	<p>Manchete do g1: </br> {link_g1}</p>
	<p>Este site foi criado por gabriela.</p>
	<p>teste</p>
	"""
from flask import request
import requests

@app.route("/telegram", methods = ["POST"])
def telegram():
	# chama funcoes do scraper
	link_globo_com = link_globo_com()
	link_g1 = link_g1()
	# processa mensagem
	update = request.json
	chat_id = update["message"]["chat"]["id"]
	text = update["message"]["text"].lower()
	if text in ["oi", "ola", "olar", "olá"]:
		answer = "Oi! Como vai?"
	elif text in ["bom dia", "boa tarde", "boa noite"]:
		answer = text
	elif "globo.com" in text:
		answer = f"segue o link da globo.com: {link_globo_com}"
	elif "g1" in text:
		answer = f"segue o link do g1: {link_g1}"
	else:
		answer = "Nao entendi"
	
	# responde
	token = "2134084726:AAEIypTzacglN21GzeTNy1qn3onQzShIt30"
	mensagem = {"chat_id": update["message"]["chat"]["id"], "text": answer}
	endpoint = "sendMessage"
	url = f"https://api.telegram.org/bot{token}/{endpoint}"
	requests.post(url, data = mensagem)
	return "ok"
