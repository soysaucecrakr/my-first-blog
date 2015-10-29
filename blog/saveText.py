from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://boardgamegeek.com/boardgame/12333/twilight-struggle'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())

gamename = soup.find("meta", {"name":"title"})['content']

numofplayers = soup.find("div", {"id":"results_players_thing_12333"}).text
numofplayers = numofplayers.strip('\t\r\n')

ages = soup.find("div", {"id":"results_minage_thing_12333"}).text
ages = ages.strip('\t\r\n')
ages = ages.strip("and up")
ages = ages.strip('\t\r\n')

playtime = soup.find("div", {"id":"results_playtime_thing_12333"}).text
playtime = playtime.strip('\t\r\n')
genrename = ""


genre = soup.find_all(href=re.compile("boardgamecategory"))[1:]
for href in genre:
	genrename = genrename + href.contents[0] + '\t'

txt = open('parseddata.txt', 'w')

with open('parseddata.txt', 'w'):
	txt.write(gamename + '\t' + numofplayers + '\t' + ages + " and up" + '\t' + 
	playtime + '\t' + genrename + '\t')
