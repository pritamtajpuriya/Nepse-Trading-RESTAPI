from time import sleep
from urllib import request
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
from urllib.error import URLError, HTTPError
from .models import Company, Trade

import re

#Convert String To float 

def convertInFloat(value):
    if value!='':
        return float(value)
    else:
 
        return 0.0

#Create company

def create_company(symbol,trade_obj):
    print("fetch company data ..")
    try:
         # Request URL
        reqURL= Request('https://merolagani.com/CompanyDetail.aspx?symbol='+symbol,headers={'User-Agent': 'Mozilla/5.0'})
        # Using urllip to read url
        html=urlopen(reqURL).read()

        #Beautiful Soup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files.
        bs= BeautifulSoup(html,'html.parser')

        # filter using id of tag
        companyData=bs.find(id="accordion").find_all("tbody")

        name=bs.find(id="ctl00_ContentPlaceHolder1_CompanyDetail1_companyName").text
        print(name)
        data=[]
        for cdata in companyData:
            var = cdata.find("td")
            dd=''
            try:
                # Remove none required escape sequence
                d=re.sub("[ , % \n \r]","",var.text )
                if d!="1." and d!='2.' :
                    data.append(d)
                
                
                
                # print(dd)
                # print(re.sub("[ ,]","",var.text ))
                
            except:
                print('error')
            
            

        sector=data[0]
        # print(data[1])
        print(data)
        shares_outstanding=convertInFloat(data[1])

        market_price=convertInFloat(data[2])

        change=convertInFloat(data[3])

        last_trade_on=data[4]

        week_52_high_low=data[5]
        high,low=week_52_high_low.split('-',1)
        week_52_high=high
        week_52_low=low
        day_180_average=convertInFloat(data[6])
        day_120_average=convertInFloat(data[7])

        year_1_yield=convertInFloat(data[8])
        eps=data[9]

        pe_ratio=convertInFloat(data[10])
        book_value=convertInFloat(data[11])
        pbv=convertInFloat(data[12])
        dividend=data[13]
        bonus=data[14]
        right_share=data[15]
        day_30_avg_volume=convertInFloat(data[16])


        market_capitalization=convertInFloat(data[17])



        dicData={'trade':trade_obj,'name':name,'sector':sector,'shares_outstanding':shares_outstanding,'market_price':market_price,'change':change,'last_trade_on':last_trade_on,'weeks_52_high':week_52_high,'weeks_52_low':week_52_low,'day_120_average':day_120_average,'year_1_yeild':year_1_yield,
        'eps':eps,'pe_ratio':pe_ratio,'book_value':book_value,'pbv':pbv,'dividend':dividend,'bonus':bonus,'right_share':right_share,'day_30_avg_volume':day_30_avg_volume,'market_capitalization':market_capitalization}

        Company.objects.create(**dicData)

    except HTTPError as e:
        print('error',e.code)
        create_company(symbol=symbol,trade_obj=trade_obj)
    else:
        print('everyting is fine')
    




@shared_task       
def update_company(symbol,trade_obj):
    print("Update Company data")
    # Request URL
    reqURL= Request('https://merolagani.com/CompanyDetail.aspx?symbol='+symbol,headers={'User-Agent': 'Mozilla/5.0'})
    # Using urllip to read url
    html=urlopen(reqURL).read()

    #Beautiful Soup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files.
    bs= BeautifulSoup(html,'html.parser')

    # filter using id of tag
    companyData=bs.find(id="accordion").find_all("tbody")

    name=bs.find(id="ctl00_ContentPlaceHolder1_CompanyDetail1_companyName").text
    print(name)
    data=[]
    for cdata in companyData:
        var = cdata.find("td")
        dd=''
        try:
            # Remove none required style tags
            d=re.sub("[ , % \n \r]","",var.text )
            if d!="1." and d!='2.' :
                data.append(d)
          
            
            
            # print(dd)
            # print(re.sub("[ ,]","",var.text ))
            
        except:
           print('error')
        
       
    
    sector=data[0]
    print(data[1])
    print(data)
    shares_outstanding=convertInFloat(data[1])
   
    market_price=convertInFloat(data[2])
   
    change=convertInFloat(data[3])
    
    last_trade_on=data[4]
   
    week_52_high_low=data[5]
    high,low=week_52_high_low.split('-',1)
    week_52_high=high
    week_52_low=low
    day_180_average=convertInFloat(data[6])
    day_120_average=convertInFloat(data[7])
   
    year_1_yield=convertInFloat(data[8])
    eps=data[9]
   
    pe_ratio=convertInFloat(data[10])
    book_value=convertInFloat(data[11])
    pbv=convertInFloat(data[12])
    dividend=data[13]
    bonus=data[14]
    right_share=data[15]
    day_30_avg_volume=convertInFloat(data[16])
   
  
    market_capitalization=convertInFloat(data[17])
    
    

    dicData={'trade':trade_obj,'name':name,'sector':sector,'shares_outstanding':shares_outstanding,'market_price':market_price,'change':change,'last_trade_on':last_trade_on,'weeks_52_high':week_52_high,'weeks_52_low':week_52_low,'day_120_average':day_120_average,'year_1_yeild':year_1_yield,
    'eps':eps,'pe_ratio':pe_ratio,'book_value':book_value,'pbv':pbv,'dividend':dividend,'bonus':bonus,'right_share':right_share,'day_30_avg_volume':day_30_avg_volume,'market_capitalization':market_capitalization}
    
    Company.objects.filter(name=name).update(**dicData)

@shared_task
def create_trade():
    
    reqURL= Request('https://merolagani.com/LatestMarket.aspx', headers={'User-Agent': 'Mozilla/5.0'})
    html= urlopen(reqURL).read()
    bs= BeautifulSoup(html,"html.parser")

    # trades=bs.find("tbody").find_all("tr")[0:5]  Limited table row
    trades=bs.find("tbody").find_all("tr")

    for singleCompanyTrade in trades:

        companyTradesDatas= singleCompanyTrade.find_all("td")

        companyData=[]
        for data in companyTradesDatas:

            textdata= data.get_text()
            companyData.append(textdata)

        symbol=companyData[0]
        ltp=convertInFloat(companyData[1].replace(',',''))
        change=convertInFloat(companyData[2].replace(',',''))
        high=convertInFloat(companyData[3].replace(',',''))
        low=convertInFloat(companyData[4].replace(',',''))
        open=convertInFloat(companyData[5].replace(',',''))
        qty=convertInFloat(companyData[6].replace(',',''))
      
        if not Trade.objects.filter(symbol=symbol).exists():
            

            trade_obj =Trade.objects.create(
                symbol=symbol,
                ltp=ltp,
                change=change,
                high=high,
                low=low,
                open=open,
                qty=qty
            )
            print('Creating nepse trade data ..')

            create_company(symbol=symbol,trade_obj=trade_obj)



         # sleep few seconds to avoid database block
        

def update_trade():
    print('Updating  nepse trade data ..')
    reqURL= Request('https://merolagani.com/LatestMarket.aspx', headers={'User-Agent': 'Mozilla/5.0'})
    html= urlopen(reqURL).read()
    bs= BeautifulSoup(html,"html.parser")

    trades=bs.find("tbody").find_all("tr")
    

    for singleCompanyTrade in trades:

        companyTradesDatas= singleCompanyTrade.find_all("td")

        companyData=[]
        for data in companyTradesDatas:

            textdata= data.get_text()
            companyData.append(textdata)

        symbol=companyData[0]
        ltp=convertInFloat(companyData[1].replace(',',''))
        change=convertInFloat(companyData[2].replace(',',''))
        high=convertInFloat(companyData[3].replace(',',''))
        low=convertInFloat(companyData[4].replace(',',''))
        open=convertInFloat(companyData[5].replace(',',''))
        qty=convertInFloat(companyData[6].replace(',',''))
        
        data={"symbol":symbol,"ltp":ltp,"change":change,"high":high,"low":low,"open":open,"qty":qty}
        
        trade_obj=Trade.objects.filter(symbol=symbol).update(**data)
        # update_company(symbol=symbol,trade_obj=trade_obj)
        


create_trade()
while True:
    sleep(30)
    update_trade()





