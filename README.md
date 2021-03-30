# Crawler
Mainly crawling data


There are some example of crawler.
* douban: movie top250
* cinema paradise: a must-watch movie in 2020
## Environment

* re
* requests
* csv

## Usage
**1. douban.py**  
The crawling data variables are as follows:
movie "name","year","score","number".
```
python douban.py train --save_path="douban_top250_data.csv"
```
ps: 程序主要练习了多个数据在一个页面可以获取，以及翻页。  

**2. Cinema_Paradise.py**  
The crawling data variables are as follows:
movie "name","year","place","category","language","douban_score","dou_form","imbd_score","imbd_from".
```
python Cinema_Paradise.py train
```
ps: 程序主要练习了数据需要通过点进子链接爬取,例如淘宝商品信息
## Reference
[https://www.bilibili.com/video/BV1i54y1h75W]
  