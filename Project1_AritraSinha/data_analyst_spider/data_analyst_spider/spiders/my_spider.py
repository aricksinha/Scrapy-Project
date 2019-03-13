import scrapy
class MySpider(scrapy.Spider):
	name="my_spider"
	
	def start_requests(self):
		urls = [
		'https://www.naukri.com/data-analyst-jobs-in-delhi-ncr'
		]
	
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
		
	def parse(self, response):
		from datetime import datetime, timedelta
		import datetime
		jobs=[]
		for x in range(0,65):
			y=x+3

			title=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/a/ul/li/text()'%(y)).extract()
			exp=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/a/span[@class="exp"]/text()'%(y)).extract()
			loc=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/a/span[@class="loc"]/span/text()'%(y)).extract()
			link=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/a[@class="content"]/@href'%(y)).extract()
			company_name=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/a/span[@class="orgRating"]/span[@class="org"]/text()'%(y)).extract()
			skills=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/a/div[@class="more"]/div[1]/span[@class="skill"]/text()'%(y)).extract()
			description=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/a/div[@class="more"]/span[@class="desc"]/text()'%(y)).extract()
			salary=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/div[@class="other_details"]/span[@class="salary  "]/text()'%(y)).extract()
			posted_by=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/div[@class="other_details"]/div[@class="rec_details"]/a[@class="rec_name"]/text()'%(y)).extract()
			posted_by_active=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/div[@class="other_details"]/div[@class="rec_details"]/a[@class="rec_name active"]/text()'%(y)).extract()
			post_date=response.xpath('/html/body/div[5]/div[1]/div[2]/div[1]/div[%d]/div[@class="other_details"]/div[@class="rec_details"]/span[@class="date"]/text()'%(y)).extract()
			   
			if title!=[]:
				sample=[]
				sample.append(title[0])
				sample.append(exp[0])
				sample.append(loc[0])
				sample.append(company_name[0])
				sample.append(link[0])
				sample.append(skills[0])
				if description!=[]:
					sample.append(description[0])
				else:
					sample.append("")
				sample.append(salary[0])
				if posted_by!=[]:
					sample.append(posted_by[0])
				else:
					if posted_by_active!=[]:
						sample.append(posted_by_active[0])	
					else:
						sample.append('')
				if post_date!=[]:
					check=post_date[0][0]
					if check=='T'or check=='J' or check=='F':
						dated = datetime.datetime.now().strftime ("%Y-%m-%d")
					else:
						check=int(check)
						date_time=datetime.datetime.now() - timedelta(days=check)
						dated=date_time.strftime ("%Y-%m-%d")
					sample.append(dated)
				else:
					sample.append('')
				jobs.append(sample)
			
		for x in jobs:
			writer = open('naukri_dataanalytics.csv','a+')
			writer.write('"%s",%s,"%s","%s",%s,"%s","%s","%s",%s,%s\n'%(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]))