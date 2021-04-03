import requests
import csv
from lxml import etree

class Config(object):
    kw = "python"
    save_path  = "zhubajie.csv"
    url = "https://www.zbj.com/search/f/?type=new&kw=" + kw

opt = Config()
f = open(opt.save_path, mode = "a+", encoding = "utf-8", newline='')
csvwriter = csv.writer(f)

def train(**kwargs):
    for k_, v_ in kwargs.items():
        setattr(opt, k_, v_)
    
    url = opt.url
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div")  # get every data    
    for div in divs:
        name     = div.xpath("./div/div[1]/div[2]/section[1]/h4[1]/a/text()")[0]
        #location = div.xpath("./div/div[1]/div[2]/section[1]/div[1]/span/text()")#
        price    = div.xpath("./div/div[2]/div[2]/i/text()")[0].strip("¥")
        turnover = div.xpath("./div/div[2]/div[2]/div/span[1]/text()")[0].strip("笔")
        advert   = opt.kw.join(div.xpath("./div/div[2]/div[3]/a/text()"))
        csvwriter.writerow([name, price, turnover, advert])

    f.close()
    resp.close()

if __name__ == '__main__':
    import fire
    fire.Fire()


