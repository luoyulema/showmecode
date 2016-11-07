import Scrapy


class Qiushibaike(scrapy.spiders.Spiders):
    """docstring for Qiushibaike"""
    name = 'qiushibaike'
    allowed_domains = ['qiushibaike.com']
    start_urls = [
        "http://www.qiushibaike.com/8hr/page/"
    ]
