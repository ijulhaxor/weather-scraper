import requests
import bs4
import os

def clear():
    os.system("clear")
    pass
def cuaca(region):
    url    = f"https://google.com/search?q=weather+in+{region}"
    result = requests.get( url )
    soup   = bs4.BeautifulSoup( result.text, "html.parser" )

    suhu   = soup.find( "div" , class_='BNeawe' ).text
    cuaca  = soup.find( "div" , class_='tAd8D'  ).text
    kota   = soup.find( "div" , class_='kCrYT'  ).text
    kota   = kota.lstrip().split(' /')[0]
    clear()
    print(f"{cuaca}\n\nWilayah : {kota}\nSuhu    : {suhu}")
    pass

clear()
region = input("Wilayah : ").replace(" ", "+")
cuaca(region)
