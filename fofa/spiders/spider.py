# -*- coding: utf-8 -*-
import scrapy
import base64
from fofa.items import FofaItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['fofa.so']

    def start_requests(self):
        rule_url_list = []
        get_cookie=open('cookie.ini','rt')
        cookie = get_cookie.read()
        get_cookie.close()
        cookie_dict = {'_fofapro_ars_session':cookie}
        for line in open('rules.ini','rt'):
            rule = line.replace('\n','')
            base64_rule = base64.b64encode(rule.encode('utf-8')).decode("utf-8")
            rule_url = 'https://fofa.so/result?page=1&qbase64=%s'%(base64_rule)
            rule_url_list.append(rule_url)
        for url in rule_url_list:
            yield scrapy.Request(url=url,cookies=cookie_dict,callback=self.parse)
    def parse(self, response):
        for someone in response.xpath("//*[@id='ajax_content']/div/div[@class='list_mod']"):
            if not 'cloudfaressl' in someone.extract():
                item = FofaItem()
                ip_list = someone.xpath("div[@class='list_mod_c']/div/div[1]/ul/li/a[@target='_blank']/text()").extract()
                item['ip'] = ip_list[0]
                yield item
        next_link = response.xpath("//*[@id='will_page']/a[@class='next_page']/@href").extract()
        if next_link:
            yield scrapy.Request(response.urljoin(next_link[0]),callback=self.parse)
