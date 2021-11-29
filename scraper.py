import requests
from bs4 import BeautifulSoup

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

def link_extra():
  url = "https://extra.globo.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_extra = soup.find('div', class_ = 'top_story m1 sports no_blog').find('a').attrs['href']
  return manchete_extra

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

def link_r7():
  url = "https://www.r7.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_r7 = soup.find('h3', class_ = 'r7-flex-title-h1').find('a').attrs['href']
  return manchete_r7

def link_opovo():
  url = "https://www.opovo.com.br/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_opovo = soup.find('div', class_ = 'materia1').find('a').attrs['href']
  return manchete_opovo

def link_nyt():
  url = "https://www.nytimes.com/"
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_nyt = soup.find('a', class_ = 'css-13shibb').attrs['href']
  return manchete_nyt
