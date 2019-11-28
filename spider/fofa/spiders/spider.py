# -*- coding: utf-8 -*-
import scrapy
import base64
from fofa.items import FofaItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['fofa.so']

    def start_requests(self):
        get_ini=open('fofa.ini','rt')
        data = get_ini.read()
        get_ini.close()
        ini_list = eval(data)
        #cookies
        cookie = ini_list['cookie']
        cookie_dict = {'_fofapro_ars_session':cookie}
        #rules
        rule = ini_list['rules']
        base64_rule = base64.b64encode(rule.encode('utf-8')).decode("utf-8")
        rule_url = 'https://fofa.so/result?page=1&qbase64=%s'%(base64_rule)
        yield scrapy.Request(url=rule_url,cookies=cookie_dict,callback=self.parse)

    def parse(self, response):
        get_ini=open('fofa.ini','rt')
        data = get_ini.read()
        get_ini.close()
        ini_list = eval(data)
        try:
            page = response.meta['page']
        except:
            page = ini_list['page']
            pass
        for someone in response.xpath("//*[@id='ajax_content']/div/div[@class='list_mod']"):
            item = FofaItem()
            domain = someone.xpath("div[@class='list_mod_t']/a/text()").extract()
            ip = someone.xpath("div[@class='list_mod_c']/div/div[1]/ul/li/a[@target='_blank']/text()").extract()
            title = someone.xpath("div[@class='list_mod_c']/div/div[1]/ul/li[1]/text()").extract()
            item['domain'] = domain[0]
            item['ip'] = ip[0]
            item['title'] = title[1].replace('\n','').replace('  ','')
            yield item

        next_link = response.xpath("//*[@id='will_page']/a[@class='next_page']/@href").extract()
        if next_link:
            if not 'page=%s'%(page+1) in next_link[0]:
                request = scrapy.Request(response.urljoin(next_link[0]),callback=self.parse)
                request.meta['page'] = page
                yield request
