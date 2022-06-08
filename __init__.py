from gartner import WebScraperGartner 
from techmeme import WebScraperTechMeme 

URL1 = "https://www.gartner.com/en/conferences/calendar"
URL2 = "https://www.techmeme.com/events"

data1 = WebScraperGartner(URL1).start()
data2 = WebScraperTechMeme(URL2).start()

print(data1)
print("-----------------------------------------------------")
print(data2)