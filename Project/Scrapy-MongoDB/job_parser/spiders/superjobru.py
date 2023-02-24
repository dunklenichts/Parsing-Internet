import scrapy
from scrapy.http import HtmlResponse
from job_parser.items import JobParserItem

class SuperjobruSpider(scrapy.Spider):
    name = 'superjobru'
    allowed_domains = ['superjob.ru']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f'https://www.superjob.ru/vakansii/{kwargs.get("search")}.html?geo%5Bt%5D%5B0%5D=4']

    def parse(self, response: HtmlResponse):
        links = response.xpath("//span[@class='_26gg2 _3oXMw _2LaRg hbKbL rIDaO oDIMq _33qju _1ZV-S']/a")
        for link in links:
            yield response.follow(link, callback=self.parse_job)

    def parse_job(self, response:HtmlResponse):
        company_name = response.xpath("//div[@class='_1bobf _346ix waa66 _13McR']/a/div/span/text()").getall()
        company_name = str(company_name[0])

        name = response.xpath("//h1/text()").getall()
        name = str(name[0])

        salary = response.xpath("//div[@class='_1bobf _26gg2 dcwto _1mkh0 hbKbL _8RHLv _2G-tF _7_bhQ']/span/span/text()").getall()
        sub_salary = ''
        for elem in salary:
            sub_salary += elem
        salary = sub_salary

        photo = response.xpath("//div[@class='_1bobf _346ix _13McR']/a/img/@src").getall()
        photo = 'http:' + photo[0]
        photo = photo.split()
        photo = str(photo[0])

        url = response.url

        yield JobParserItem(name=name, company_name=company_name, salary=salary, photo=photo, url=url)