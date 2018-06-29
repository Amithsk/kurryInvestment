import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://www.narakkalkuries.com/intimation.html#i'
    ]

    def parse(self, response):
        for check in response.xpath('//table[@class="MsoTableGrid"]'):
            item = dict()
            item['noOfChitty'] =check.xpath('//table[@class="MsoTableGrid"]/tr/td[1]//text()').re(r'[0-9,-/]+|[0-9]+')
            item['monthInfo'] = check.xpath('//table[@class="MsoTableGrid"]/tr/td[2]//text()').re(r'[0-9,-/]+|[NKL 0-9]+'),
            item['chittyNo'] =check.xpath('//table[@class="MsoTableGrid"]/tr/td[3]//text()').re(r'[0-9/]+|[NKL 0-9]+'),
            item['regNo'] =check.xpath('//table[@class="MsoTableGrid"]/tr/td[4]//text()').re(r'[0-9,-/]+'),
            item['sala'] = check.xpath('//table[@class="MsoTableGrid"]/tr/td[5]//text()').re(r'[0-9,-/]+'),
 	    item['inst']=check.xpath('//table[@class="MsoTableGrid"]/tr/td[6]//text()').re(r'[0-9/]+|[A-Za-z]+'),	
            item['chittyStatus']=check.xpath('//table[@class="MsoTableGrid"]/tr/td[7]//text()').re(r'[0-9,]+|[A-Za-z]+'),
            item['chittyAmount']=check.xpath('//table[@class="MsoTableGrid"]/tr/td[8]//text()').re(r'[0-9,]+')	
            yield item
