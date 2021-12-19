import datetime
import os
from flask import Flask, request
from scraper import *

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
	manchete_extra = link_extra()
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
	<p>{manchete_extra}</p>
	</br>
	<p>Este site foi criado por Gabriela Caesar.</p>
	"""

# robo do telegram
@app.route("/telegram", methods = ["POST"])
def telegram():
	# processa mensagem
	update = request.json
	chat_id = update["message"]["chat"]["id"]
	text = update["message"]["text"].lower()
	
	if text in ["/start"]:
		answer = """
		Oi! Eu sou o robô da Gabriela e mostro as manchetes dos principais sites de notícias. 
		Sempre que voce quiser saber uma manchete, você pode escrever aqui e eu te envio o link.
		
		ATENÇÃO: Digite "Todos" para receber todos os links. Ou digite apenas um nome do veículo por vez. 
		
		Opções da imprensa do Brasil: globo.com, g1, Valor, UOL, Folha, Estadão, O Globo e Metrópoles.
		"""
	elif text in ["todos", "todo", "tudo", "todos os links", "todas as manchetes"]:
		# chama funcoes do scraper
		manchete_globo_com = link_globo_com()
		manchete_g1 = link_g1()
		manchete_valor = link_valor()
		manchete_uol = link_uol()
		manchete_folha = link_folha()
		manchete_estadao = link_estadao()
		manchete_oglobo = link_oglobo()
		manchete_metropoles = link_metropoles()
		manchete_extra = link_extra()
		# printa mensagem com link
		answer = f"""
		segue o link da globo.com: {manchete_globo_com}
		segue o link do g1: {manchete_g1}
		segue o link do Valor: {manchete_valor}
		segue o link do UOL: {manchete_uol}
		segue o link da Folha: {manchete_folha}
		segue o link do Estadão: {manchete_estadao}
		segue o link d'O Globo: {manchete_oglobo}
		segue o link do Metrópoles: {manchete_metropoles}
		<p>{manchete_extra}</p>
		"""
	elif text in ["globo.com", "globo"]:
		manchete_globo_com = link_globo_com()
		manchete_extra = link_extra()
		answer = f"segue o link da globo.com: {manchete_globo_com} {manchete_extra}"
	elif text in ["g1", "g um"]:
		manchete_g1 = link_g1()
		answer = f"segue o link do g1: {manchete_g1}"
	elif text in ["valor", "valor economico", "valor ecomomico"]:
		manchete_valor = link_valor()
		answer = f"segue o link do Valor: {manchete_valor}"
	elif text in ["uol", "uo", "uoll"]: 
		manchete_uol = link_uol()
		answer = f"segue o link do UOL: {manchete_uol}"
	elif text in ["folha", "folha de spaulo", "folha de s.paulo", "fsp"]:
		manchete_folha = link_folha()
		answer = f"segue o link da Folha: {manchete_folha}"
	elif text in ["estadao", "estadão"]:
		manchete_estadao = link_estadao()
		answer = f"segue o link do Estadão: {manchete_estadao}"
	elif text in ["o globo", "oglobo"]: 
		manchete_oglobo = link_oglobo()
		answer = f"segue o link d'O Globo: {manchete_oglobo}"
	elif text in ["metropoles", "metropolis"]:
		manchete_metropoles = link_metropoles()
		answer = f"segue o link do Metrópoles: {manchete_metropoles}"
	else:
		answer = """Por favor, escreva "todos" se desejar receber todos os links. Ou escreva apenas o nome do veículo que te interessa:
		
		Opções da imprensa do Brasil: globo.com, g1, Valor, UOL, Folha, Estadão, O Globo e Metrópoles.
		"""
	
	# responde
	token = os.environ["TELEGRAM_TOKEN"]
	message = {"chat_id": chat_id, "text": answer}
	endpoint = "sendMessage"
	url = f"https://api.telegram.org/bot{token}/{endpoint}"
	requests.post(url, data = message)
	# finaliza
	return "ok"
    	
