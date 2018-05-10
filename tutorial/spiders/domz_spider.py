# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 20:57
# @Author  : Mat
# @Email   : mat_wu@163.com
# @File    : domz_spider.py
# @Software: PyCharm
import scrapy
from scrapy import Spider


class DomzSpider(Spider):
    name = 'dmoz'
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, "wb") as f:
            f.write(response.body)
