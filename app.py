import requests
import beautifulsoup4
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
	token = "2134084726:AAEIypTzacglN21GzeTNy1qn3onQzShIt30"
	dados = request.json()
	mensagem = {"chat_id": dados["message"]["chat"]["id"], "text": "oiiiiiiiiiii!"}
	endpoint = "sendMessage"
	url = f"https://api.telegram.org/bot{token}/{endpoint}"
	requests.post(url, data = mensagem)
	return "ok"
	
