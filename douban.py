import requests
import re
import csv

class Config(object):
    url = "https://movie.douban.com/top250"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57"
    }
    data_start = 0     #  it has to be multiple of 20
    data_end   = 250
    is_down    = False
    save_path  = "douban_top250_data.csv"
    save_path1 = "douban_top250_data_1.csv"  # if is_down = True, then save_path = save_path1

opt = Config()

# python .\douban.py train 
def train(**kwargs):
    for k_, v_ in kwargs.items():
        setattr(opt, k_, v_)

    url = opt.url
    head = opt.head

    for page_start in range(opt.data_start, opt.data_end, 20):

        param = {
            "start": page_start,
            "filter": "",
        }
        resp = requests.get(url, headers = head, params = param, verify = False)
        page_content = resp.text

        # Regular coding rule               
        obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                        r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)'
                        r'</span>.*?<span>(?P<number>.*?)人评价</span>', re.S)
        
        result = obj.finditer(page_content)
        
        # save data
        if opt.is_down:
            path = opt.save_path1
        else:
            path = opt.save_path

        with open(path, mode = "a+", encoding = "utf-8", newline='') as f:
            csvwriter = csv.writer(f)
            for it in result:
                #print(it.group("name"))
                dic = it.groupdict()
                dic['year'] = dic['year'].strip()
                csvwriter.writerow(dic.values())

    f.close()
    resp.close()

if __name__ == '__main__':
    import fire
    fire.Fire()

