#Importing the important libraries in the scrapy
# scrapy.http is imported for requesting the data from the html page 

#---------------------------------------------------------------------------------------------------------------------------------------------------#

from typing import Iterable
import scrapy
from scrapy.http import Request

# this class is by default created  while generating the scrapy spider 
#name :- Name of the scrapy spider 
# allowed_domains :- name of the domains which we are allowing to the spider

#-----------------------------------------------------------------------------------------------------------------------------------------------------#



class BillsSpider(scrapy.Spider):
    name = "bills"
    allowed_domains = ["ndlegis.gov"]
    start_urls = ["https://ndlegis.gov"]


#------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    
    # Function Start_Requests is used to get the all the elements and webpage data from the provided url.


    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Host": "www.ndlegis.gov",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }



    def start_requests(self):
        
        urls = [f'https://www.ndlegis.gov/assembly/68-2023/bill-index.html']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse,headers=self.headers)


#------------------------------------------------------------------------------------------------------------------------------------------------------#
    
            # Below function is the main functions for extracting the data 

            # We have used the cards in which we are assigning the total no. of the bills that are provided on the webpage.

            # We have taken various empty list which are going to be used in the code to store the text values from the webpage 

            # We have find out the xpath of the elements where our data is stored this data is extract from the various attributes and stored in the list.

            # We have used the multiple if else conditions and various suedo condition for gathering the data from the webpage.
    
    def parse(self, response):
        cards = response.xpath("//div[@class='col bill']")
        print(len(cards))
        bill_status1=[]
      
        jurisdictions=[]
        organization_classification=[]
        bill_details = response.xpath("//h4[@class='bill-name flex']/text()").getall() 
        bill_status = response.xpath("//span[1][@data-toggle='tooltip']/@class").getall()
        # print(bill_status)

        for b in bill_status:
            if b =="passed-bill flex-right hide":
                bill_status1.append('Failed')
            else:
                bill_status1.append('Passed')
            jurisdictions.append('North Dakota')

        for i in bill_details:
            if i.startswith('H'):
                organization_classification.append('Lower')
            else:
                organization_classification.append('Upper')



        
        bill_type1 = response.xpath("//div[@class='card']/ul/li[3]/text()").getall()


        chamber = response.xpath("//div[@class='card']/ul/li[4]/text()").getall()

    
        assembly = response.xpath("//div[@class='card']/ul/li[6]/text()").getall()


        session = response.xpath("//div[@class='card']/ul/li[7]/text()").getall()


        session_date_month = response.xpath("//div[@class='card']/ul/li[5]/text()").getall()



        # for bill_type_abbr in bill_details:
            
        #     if bill_type_abbr in ("HR", "SR"):
        #         bill_type .append("resolution")
        #     if bill_type_abbr in ("HCR", "SCR"):
        #         bill_type.append( "concurrent resolution")
        #     if bill_type_abbr in ("HMR", "SMR"):
        #         bill_type.append("memorial")
        #     else:
        #         bill_type.append( "bill")
        # print(len(bill_type))

#------------------------------------------------------------------------------------------------------------------------------------------------------




        bill_urls = response.xpath("//a[@class='card-link']/@href").getall()
        

        sponsors= response.xpath("//div[@class='sponsors scroll']/p/text()").getall()
        

        bill_description = response.xpath("//p[@class='title scroll']/text()").getall()
        
        

        last_official_action =response.xpath("//div[@class='final-action scroll']/p/text()").getall()
#------------------------------------------------------------------------------------------------------------------------------------------------------#    
# #Since we have to create a dictionary in the below code which will be used further in the dataframe so we have to main tain the length of all list same.So we are checking the length of the list.

        print(len(bill_details))
        print(len(last_official_action))
        print(len(bill_urls))
        print(len(sponsors))
        print(len(bill_description))
        print(len(bill_type1))
        print(len(chamber))
        print(len(assembly))
        print(len(session))
        print(len(bill_status1))
#------------------------------------------------------------------------------------------------------------------------------------------------------#     
# Finally we gather all the details in the list and we are using the above the list to create a dictionary because we have to use this dictionary in the dataframe.




        datadetails =  { "identifier":bill_details,
                         "title":bill_description,
                         "classifications":bill_type1,
                         "session_identifiers":assembly,
                         "juridiction":jurisdictions,
                         "organization_classification":organization_classification,
                         "bill_urls":bill_urls,
                         "sponsors": sponsors,
                         "last_official_action":last_official_action,
                        "chamber":chamber,
                        "session":session,
                        "bill_status":bill_status1,
                        "session_date_month":session_date_month,
                    
        }
#------------------------------------------------------------------------------------------------------------------------------------------------------


# Finally we are using the pandas libraries for creating a dataframe from the datadetails dictionary and we have write this dataframe into the csv.


        import pandas as pd
        df = pd.DataFrame(datadetails)
        df.to_csv(r'D:/north_dakota_bills.csv')




        




