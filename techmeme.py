# Module
from bs4 import BeautifulSoup
import time, requests, urllib, validators, sys

# TechMeme class
class WebScraperTechMeme:
    # constructor
    def __init__(self, url):
        self.url = url
        self.dataInfo = []

    # check if the url is valid
    def check_valid_url(self):
        if not validators.url(self.url) and self.url != "":
            print("[-] Invalid URL")
            sys.exit(1) 

    # get data from the url
    def get_data(self): 
        print("[+] Getting data...")
        headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        page = requests.get(self.url, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        metaData = soup.findAll('div', {"class" : "rhov"})
        for x in metaData:
            nameInfo = x.a.select_one(":nth-child(2)").text
            locationInfo = x.a.select_one(":nth-child(3)").text
            dateInfo = x.a.div.text
            self.dataInfo.append({"name" : nameInfo, "location" : locationInfo, "date" : dateInfo})
        soup.decompose()

    # returning the data
    def print_data(self):
        print("[+] Printing data...")
        return self.dataInfo

    # main function
    def start(self):
        self.check_valid_url()
        self.get_data()
        data = self.print_data()
        return data
    
    # end of class
    def __del__(self):
        pass


URL = "https://www.techmeme.com/events"

def fid():
    print("okay")

if __name__=="__main__":
    # Start the program
    startTime = time.time()
    # call the class
    start = WebScraperTechMeme(URL)
    start.start()
    endTime = time.time()
    print("[+] Program run time: " + str(endTime - startTime))
