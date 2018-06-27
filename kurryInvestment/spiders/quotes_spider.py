import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
            'http://www.narakkalkuries.com/intimation.html#i'
    ]

    def parse(self, response):
        count=0  
        for check in response.xpath('//table[@class="MsoTableGrid"]'):
            print("The value of counter is",count)
            print("The value of check is",check)
            item = dict()
#            item['noOfChitty'] =[''.join(cell.xpath('./a/text()|./text()').extract()).strip() for cell in check.xpath('//table[@class="MsoTableGrid"]/tr/td[1]')]
#            item['noOfChitty'] =''.join(check.xpath('//table[@class="MsoTableGrid"]/tr/td[1]//text()').extract()).strip()
#            item['monthInfo]' = check.xpath('//table[@class="MsoTableGrid"]/tr/td[2]//text()').extract(),
#            item['chittyNo'] =check.xpath('//table[@class="MsoTableGrid"]/tr/td[3]//text()').extract(),
#            item['regNo'] =check.xpath('//table[@class="MsoTableGrid"]/tr/td[4]//text()').extract(),
            item['sala'] = check.xpath('//table[@class="MsoTableGrid"]/tr/td[5]//text()').re(r'[0-9,-]+')
# 	     item['inst']=check.xpath('//table[@class="MsoTableGrid"]/tr/td[6]//text()').extract(),	
#            item['chittyStatus']=check.xpath('//table[@class="MsoTableGrid"]/tr/td[7]//text()').extract(),
#            item['chittyAmount']=check.xpath('//table[@class="MsoTableGrid"]/tr/td[8]//text()').extract()	
            yield item
            count+=1;
