# Crawler
Mainly crawling data


There are some example of crawler.
* douban: [movie top250](https://movie.douban.com/top250)
* cinema paradise: [a must-watch movie in 2020](https://www.dy2018.com/index.html)
* vegetable price : [beijing xinfadi ](http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml)
## Environment


* requests
* re
* bs4
* csv

## Usage
**1. douban.py**  
The crawling data variables are as follows:
movie: "name","year","score","number".
```
python douban.py train --save_path="douban_top250_data.csv"
```
ps: 程序主要练习了多个数据在一个页面可以获取，以及翻页。  

**2. Cinema_Paradise.py**  
The crawling data variables are as follows:
movie: "name","year","place","category","language","douban_score","dou_form","imbd_score","imbd_from".
```
python Cinema_Paradise.py train
```
ps: 程序主要练习了数据需要通过点进子链接爬取,例如淘宝商品信息

**3. BeautifulSoup_VegetablePrice.py**  
The crawling data variables are as follows:
movie "name","low","avg","high","size","unit","date".
```
python BeautifulSoup_VegetablePrice.py train --max_page=4
```
ps: 程序主要联系了利用bs4解析网络，爬取数据。
## Reference
[https://www.bilibili.com/video/BV1i54y1h75W]
  