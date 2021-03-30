import re
import csv
import requests

# python .\Cinema_Paradiso.py train
class Config():
    save_path = "cinema_paradis_data.csv"
    domain = "https://www.dy2018.com/"
    head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57"
    }


opt = Config()

def train(**kwargs):
    for k_, v_ in kwargs.items():
        setattr(opt, k_, v_)

    resp = requests.get(opt.domain, verify = False, headers = opt.head)
    resp.encoding = 'gb2312'  # chinese

    obj1 = re.compile(r"2020必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
    obj2 = re.compile(r"<a href='(?P<href>.*?)'", re.S)  
    obj3 = re.compile(r"◎片　　名(?P<name>.*?)<br />◎年　　代(?P<year>.*?)<br />◎产　　地(?P<place>.*?)<br />"
                      r"◎类　　别(?P<category>.*?)<br />◎语　　言(?P<language>.*?)<br />.*?◎豆瓣评分(?P<douban_score>.*?)/10 from(?P<dou_from>.*?)"
                      r"users<br />◎IMDb评分(?P<imbd_score>.*?)/10 from(?P<imbd_from>.*?)users<br />",re.S)

    result1 = obj1.finditer(resp.text)
    child_href_list = []
    for it in result1:
        ul = it.group("ul")

        result2 = obj2.finditer(ul)
        for i in result2:
            child_href = opt.domain + i.group("href").strip("/")
            child_href_list.append(child_href)

    for href in child_href_list:
        child_resp = requests.get(href, verify = False, headers = opt.head)
        child_resp.encoding = "gb2312"
        result3 = obj3.finditer(child_resp.text)
        
        with open(opt.save_path, mode = "a+", encoding = "utf-8", newline='') as f:
            csvwriter = csv.writer(f)
            for t in result3:
                dic = t.groupdict()
                dic['year'] = dic['year'].strip()
                csvwriter.writerow(dic.values())

        child_resp.close()

    f.close()
    resp.close()

if __name__=="__main__":
    import fire
    fire.Fire()