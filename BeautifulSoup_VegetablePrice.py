import requests
from bs4 import BeautifulSoup
import csv

class Config(object):
    max_page = 3
    save_path  = "vegtable_price.csv"

opt = Config()
f = open("vegtable_price.csv", mode = "a+", encoding = "utf-8", newline='')
csvwriter = csv.writer(f)

def train(**kwargs):
    for k_, v_ in kwargs.items():
        setattr(opt, k_, v_)

    for page in range(1, opt.max_page):
        url="http://www.xinfadi.com.cn/marketanalysis/0/list/{}&page.shtml".format(page)
        resp = requests.get(url)
        page = BeautifulSoup(resp.text, "html.parser")
        #page.find("table", class_= "hq_table")
        table = page.find("table", attrs = {"class": "hq_table"} )
        trs   = table.find_all("tr")[1:]  #Find all rows = "tr"，and column = "td"
        for tr in trs:
            tds  = tr.find_all("td")  # get all of row's data
            name = tds[0].text   
            low  = tds[1].text
            avg  = tds[2].text
            high = tds[3].text
            size = tds[4].text
            unit = tds[5].text
            date = tds[6].text
            csvwriter.writerow([name, low, avg, high, unit, size, date]) 

    f.close()
    resp.close()

if __name__ == '__main__':
    import fire
    fire.Fire()