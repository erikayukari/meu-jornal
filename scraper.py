import requests
from bs4 import BeautifulSoup

def bs_scraper():
  page = requests.get(url)
  soup = BeautifulSoup(page.content, "html.parser")
  return soup

# scrapers
def link_globo_com():
  url = "https://www.globo.com/"
  bs_scraper()
  manchete_globo_com = soup.find('a', class_ = 'post__link').attrs['href']
  return manchete_globo_com

def link_g1():
  url = "https://g1.globo.com/"
  bs_scraper()
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

def link_metropoles():
  url = "https://www.metropoles.com/"
  page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.27 Safari/537.36"})
  soup = BeautifulSoup(page.content, "html.parser")
  manchete_metropoles = soup.find('h2', class_ = 'm-title').find('a').attrs['href']
  return manchete_metropoles
