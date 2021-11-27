import requests
import datetime
import os
from bs4 import BeautifulSoup
from flask import Flask, request

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

def link_valor():
  url = "https://valor.globo.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_valor = soup.find('div', class_ = 'theme-title-element').find('a').attrs['href']
  return manchete_valor

def link_uol():
  url = "https://www.uol.com.br/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_uol = soup.find('article', class_ = 'headlineMain section__grid__main__highlight__item').find('a').attrs['href']
  return manchete_uol

def link_folha():
  url = "https://www.folha.uol.com.br/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  #print(soup)
  manchete_folha = soup.find('a', class_ = 'c-main-headline__url').attrs['href']
  return manchete_folha

def link_estadao():
  url = "https://www.estadao.com.br/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_estadao = soup.find('div', class_ = 'intro').find('a').attrs['href']
  return manchete_estadao

def link_oglobo():
  url = "https://oglobo.globo.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_oglobo = soup.find('h1', class_ = 'headline__title').find('a').attrs['href']
  return manchete_oglobo

def link_odia():
  url = "https://odia.ig.com.br/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_odia = soup.find('article', class_ = 'teaser manchetao').find('a').attrs['href']
  return manchete_odia

def link_zerohora():
  url = "https://gauchazh.clicrbs.com.br/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  permalink_zerohora = soup.find('div', class_ = 'featured-card__summary l-col-sm-16').find('a').attrs['href']
  manchete_zerohora = "https://gauchazh.clicrbs.com.br" + permalink_zerohora
  return manchete_zerohora

def link_correio():
  url = "https://www.correiobraziliense.com.br/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_correio = soup.find('div', class_ = 'manch-01').find('article').find('a').attrs['href']
  return manchete_correio

def link_jc():
  url = "https://jc.ne10.uol.com.br/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_jc = soup.find('a', class_ = 'content').attrs['href']
  return manchete_jc

def link_metropoles():
  url = "https://www.metropoles.com/"
  page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.27 Safari/537.36"})
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_metropoles = soup.find('h2', class_ = 'm-title').find('a').attrs['href']
  return manchete_metropoles

def link_nyt():
  url = "https://www.nytimes.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_nyt = soup.find('a', class_ = 'css-13shibb').attrs['href']
  return manchete_nyt

# coisas do site
app = Flask(__name__)

@app.route("/")
def hello_world():
	arquivo = open("templates/home.html")
	return arquivo.read()

@app.route("/manchetes")
def manchetes():
	manchete_globo_com = link_globo_com()
	manchete_g1 = link_g1()
	manchete_valor = link_valor()
	manchete_uol = link_uol()
	manchete_folha = link_folha()
	manchete_estadao = link_estadao()
	manchete_oglobo = link_oglobo()
	manchete_metropoles = link_metropoles()
	manchete_odia = link_odia()
	manchete_zerohora = link_zerohora()
	manchete_correio = link_correio()
	manchete_jc = link_jc()
	manchete_nyt = link_nyt()
	return f"""
	<h1>Manchetes</h1>
	<a href="/">Home</a>
	<a href="/manchetes">Manchetes</a>
	<h2>Imprensa - Brasil</h2>
	<p>Manchete da Globo.com: </br> {manchete_globo_com}</p>
	<p>Manchete do g1: </br> {manchete_g1}</p>
	<p>Manchete do Valor: </br> {manchete_valor}</p>
	<p>Manchete do UOL: </br> {manchete_uol}</p>
	<p>Manchete da Folha: </br> {manchete_folha}</p>
	<p>Manchete do Estadão: </br> {manchete_estadao}</p>
	<p>Manchete d'O Globo: </br> {manchete_oglobo}</p>
	<p>Manchete do Metrópoles: </br> {manchete_metropoles}</p>
	<p>Manchete d'O Dia: </br> {manchete_odia}</p>
	<p>Manchete do Zero Hora: </br> {manchete_zerohora}</p>
	<p>Manchete do Correio Braziliense: </br> {manchete_correio}</p>
	<p>Manchete do Jornal do Commercio: </br> {manchete_jc}</p>
	</br>
	<h2>Imprensa - EUA</h2>
	<p>Manchete do New York Times: </br> {manchete_nyt}</p>
	<p>Este site foi criado por Gabriela Caesar.</p>
	"""

# robo do telegram
@app.route("/telegram", methods = ["POST"])
def telegram():
	# chama funcoes do scraper
	manchete_globo_com = link_globo_com()
	manchete_g1 = link_g1()
	manchete_valor = link_valor()
	manchete_uol = link_uol()
	manchete_folha = link_folha()
	manchete_estadao = link_estadao()
	manchete_oglobo = link_oglobo()
	manchete_metropoles = link_metropoles()
	manchete_odia = link_odia()
	manchete_zerohora = link_zerohora()
	manchete_correio = link_correio()
	manchete_jc = link_jc()
	manchete_nyt = link_nyt()
	# processa mensagem
	update = request.json
	chat_id = update["message"]["chat"]["id"]
	text = update["message"]["text"].lower()
	if text in ["/start"]:
		answer = """
		Oi! Eu sou o robô da Gabriela e mostro as manchetes dos principais sites de notícias. 
		Sempre que voce quiser saber uma manchete, você pode escrever aqui e eu te envio o link.
		
		ATENÇÃO: Digite um nome do veículo por vez. 
		Opções da imprensa do Brasil: globo.com, g1, Valor, UOL, Folha, Estadão, O Globo, Metrópoles, O Dia, Zero Hora e Correio Braziliense.
		Opções da imprensa dos EUA: NYT.
		"""
	elif "globo.com" in text:
		answer = f"segue o link da globo.com: {manchete_globo_com}"
	elif "g1" in text:
		answer = f"segue o link do g1: {manchete_g1}"
	elif "valor" in text:
		answer = f"segue o link do Valor: {manchete_valor}"
	elif "uol" in text: 
		answer = f"segue o link do UOL: {manchete_uol}"
	elif "folha" in text:
		answer = f"segue o link da Folha: {manchete_folha}"
	elif text in ["estadao", "estadão"]:
		answer = f"segue o link do Estadão: {manchete_estadao}"
	elif "o globo" in text: 
		answer = f"segue o link d'O Globo: {manchete_oglobo}"
	elif "metropoles" in text:
		answer = f"segue o link do Metrópoles: {manchete_metropoles}"
	elif "o dia" in text: 
		answer = f"segue o link d'O Dia: {manchete_odia}"
	elif "zero hora" in text: 
		answer = f"segue o link do UOL: {manchete_zerohora}"
	elif "correio braziliense" in text:
		answer = f"segue o link do UOL: {manchete_correio}"
	elif "jornal do commercio" in text:
		answer = f"segue o link do Jornal do Commercio: {manchete_jc}"
	elif "nyt" in text:
		answer = f"segue o link do NYT: {manchete_nyt}"
	else:
		answer = """
		Por favor, digite um veículo **que aparece na lista**.
		Opções da imprensa do Brasil: globo.com, g1, Valor, UOL, Folha, Estadão, O Globo, Metrópoles, O Dia, Zero Hora e Correio Braziliense.
		Opções da imprensa dos EUA: NYT.
		"""
	
	# responde
	token = os.environ["TELEGRAM_TOKEN"]
	mensagem = {"chat_id": update["message"]["chat"]["id"], "text": answer}
	endpoint = "sendMessage"
	url = f"https://api.telegram.org/bot{token}/{endpoint}"
	requests.post(url, data = mensagem)
	return "ok"
