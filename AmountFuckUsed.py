import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

artist_nameO = input("Enter Artist Name:")
artist_name = artist_nameO.replace(" ","")
artist_name = artist_name.lower()
song_nameO = input("Enter Song Name:")
song_name = song_nameO.replace(" ","")
song_name = song_name.lower()

my_url = "https://www.azlyrics.com/lyrics/"+ artist_name +"/" + song_name + ".html"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

box = page_soup.find("div", {"class" : "col-xs-12 col-lg-8 text-center"})
containers = box.findAll("div")
lyrics = containers[6].text.split();

fuckUsed = 0

for x in lyrics:
    if "fuck" in x.lower():
        fuckUsed += 1

print("In the song " + song_nameO + ", By " + artist_nameO + ", FUCK is used " + str(fuckUsed) + " times...")
