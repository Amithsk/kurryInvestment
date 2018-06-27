import scrapy


#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#            'http://www.narakkalkuries.com/intimation.html#i'
#    ]
#
#    def parse(self, response):
#        count=0  
#        for check in response.xpath('//table[@class="MsoTableGrid"]'):
#            print("The value of counter is",count)
#            print("The value of check is",check)
#            yield {
#                  'noOfChitty':check.xpath('//table[@class="MsoTableGrid"]/tr/td[1]//text()').extract(),
#                  'monthInfo':check.xpath('//table[@class="MsoTableGrid"]/tr/td[2]//text()').extract(),
#                  'chittyNo':check.xpath('//table[@class="MsoTableGrid"]/tr/td[3]//text()').extract(),
#                  'regNo':check.xpath('//table[@class="MsoTableGrid"]/tr/td[4]//text()').extract(),
#                  'sala':check.xpath('//table[@class="MsoTableGrid"]/tr/td[5]//text()').extract(), 
# 	          'inst':check.xpath('//table[@class="MsoTableGrid"]/tr/td[6]//text()').extract(),	
# 		  'chittyStatus':check.xpath('//table[@class="MsoTableGrid"]/tr/td[7]//text()').extract(),
#                  'chittyAmount':check.xpath('//table[@class="MsoTableGrid"]/tr/td[8]//text()').extract()	
#            }
#            count+=1;
