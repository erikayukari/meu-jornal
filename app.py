import datetime
import os
from flask import Flask, request
from scraper import link_globo_com, link_g1, link_valor, link_uol, link_folha, link_estadao, link_oglobo, link_extra, link_odia, link_zerohora, link_correio, link_jc, link_metropoles, link_r7, link_opovo, link_nyt

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
	manchete_odia = link_odia()
	manchete_zerohora = link_zerohora()
	manchete_correio = link_correio()
	manchete_jc = link_jc()
	manchete_r7 = link_r7()
	manchete_opovo = link_opovo()
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
	<p>Manchete do Extra: </br> {manchete_extra}</p>
	<p>Manchete d'O Dia: </br> {manchete_odia}</p>
	<p>Manchete do Zero Hora: </br> {manchete_zerohora}</p>
	<p>Manchete do Correio Braziliense: </br> {manchete_correio}</p>
	<p>Manchete do Jornal do Commercio: </br> {manchete_jc}</p>
	<p>Manchete d'O Povo: </br> {manchete_opovo}</p>
	<p>Manchete do R7: </br> {manchete_r7}</p>
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
	manchete_extra = link_extra()
	manchete_odia = link_odia()
	manchete_zerohora = link_zerohora()
	manchete_correio = link_correio()
	manchete_jc = link_jc()
	manchete_r7 = link_r7()
	manchete_opovo = link_opovo()
	manchete_nyt = link_nyt()
	# processa mensagem
	update = request.json
	chat_id = update["message"]["chat"]["id"]
	text = update["message"]["text"].lower()
	
	if text in ["/start"]:
		answer = """
		Oi! Eu sou o robô da Gabriela e mostro as manchetes dos principais sites de notícias. 
		Sempre que voce quiser saber uma manchete, você pode escrever aqui e eu te envio o link.
		
		ATENÇÃO: Digite "Todos" para receber todos os links. Ou digite apenas um nome do veículo por vez. 
		
		Opções da imprensa do Brasil: globo.com, g1, Valor, UOL, Folha, Estadão, O Globo, Metrópoles, Extra, O Dia, Zero Hora, Correio Braziliense, R7 e O Povo. Opções da imprensa dos EUA: NYT.
		"""
	elif text in ["todos", "todo", "tudo", "todos os links", "todas as manchetes"]:
		answer = f"""
		segue o link da globo.com: {manchete_globo_com}
		segue o link do g1: {manchete_g1}
		segue o link do Valor: {manchete_valor}
		segue o link do UOL: {manchete_uol}
		segue o link da Folha: {manchete_folha}
		segue o link do Estadão: {manchete_estadao}
		segue o link d'O Globo: {manchete_oglobo}
		segue o link do Metrópoles: {manchete_metropoles}
		segue o link do Extra: {manchete_extra}
		segue o link d'O Dia: {manchete_odia}
		segue o link do Zero Hora: {manchete_zerohora}
		segue o link do Correio Braziliense: {manchete_correio}
		segue o link do Jornal do Commercio: {manchete_jc}
		segue o link do R7: {manchete_r7}
		segue o link d'O Povo: {manchete_opovo}
		segue o link do NYT: {manchete_nyt}
		"""
	elif text in ["globo.com", "globo"]:
		answer = f"segue o link da globo.com: {manchete_globo_com}"
	elif text in ["g1", "g um"]:
		answer = f"segue o link do g1: {manchete_g1}"
	elif text in ["valor", "valor economico", "valor ecomomico"]:
		answer = f"segue o link do Valor: {manchete_valor}"
	elif text in ["uol", "uo", "uoll"]: 
		answer = f"segue o link do UOL: {manchete_uol}"
	elif text in ["folha", "folha de spaulo", "folha de s.paulo", "fsp"]:
		answer = f"segue o link da Folha: {manchete_folha}"
	elif text in ["estadao", "estadão"]:
		answer = f"segue o link do Estadão: {manchete_estadao}"
	elif text in ["o globo", "oglobo"]: 
		answer = f"segue o link d'O Globo: {manchete_oglobo}"
	elif text in ["metropoles", "metropolis"]:
		answer = f"segue o link do Metrópoles: {manchete_metropoles}"
	elif text in ["extra", "jornal extra", "o extra"]: 
		answer = f"segue o link do Extra: {manchete_extra}"
	elif text in ["o dia", "odia"]: 
		answer = f"segue o link d'O Dia: {manchete_odia}"
	elif text in ["zero hora", "zerohora", "0 hora"]: 
		answer = f"segue o link do Zero Hora: {manchete_zerohora}"
	elif text in ["correio braziliense", "correio brasiliense"]:
		answer = f"segue o link do Correio Braziliense: {manchete_correio}"
	elif text in ["jornal do commercio", "jornal do commércio", "jc", "jornal do comercio", "jornal do comércio"]:
		answer = f"segue o link do Jornal do Commercio: {manchete_jc}"
	elif text in ["r7", "r77", "r sete"]: 
		answer = f"segue o link do R7: {manchete_r7}"
	elif text in ["o povo", "opovo", "povo"]:
		answer = f"segue o link d'O Povo: {manchete_opovo}"
	elif text in ["nyt", "the new york times", "new york times"]:
		answer = f"segue o link do NYT: {manchete_nyt}"
	else:
		answer = """Por favor, escreva "todos" se desejar receber todos os links. Ou escreva apenas o nome do veículo que te interessa:
		
		Opções da imprensa do Brasil: globo.com, g1, Valor, UOL, Folha, Estadão, O Globo, Metrópoles, Extra, O Dia, Zero Hora, Correio Braziliense, R7 e O Povo. Opções da imprensa dos EUA: NYT.
		"""
	
	# responde
	token = os.environ["TELEGRAM_TOKEN"]
	mensagem = {"chat_id": update["message"]["chat"]["id"], "text": answer}
	endpoint = "sendMessage"
	url = f"https://api.telegram.org/bot{token}/{endpoint}"
	requests.post(url, data = mensagem)
	return "ok"
