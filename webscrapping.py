import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import csv
chrome_path=r'D:\Xampp\htdocs\Python\webscrapping\chromedriver.exe'
driver=webdriver.Chrome(chrome_path)
kf=[]
kf.append('prop-price')
kf.append('key-bed')
kf.append('key-bath')
kf.append('key-kitchen')
kf.append('key-parking')
kf.append('key-garden')
counter=0
def information(uw):
    a=[]
    a.append(counter)
    a.append(uw)
    #for loc
    loc=driver.find_element_by_class_name("green-text")
    word=loc.text
    na=word.split(',')
    l=len(na)
    a.append(na[l-2])
    #for complete loc
    cl=driver.find_element_by_css_selector("body > div.dark-wrapper > div:nth-child(1) > div.light-wrapper.inner2 > div.row > div.col-sm-9 > div.green-text > h2")
    a.append(cl.text)
    #Size
    sz=[]
    cl=driver.find_element_by_css_selector("body > div.dark-wrapper > div:nth-child(1) > div.light-wrapper.inner2 > div.row > div.col-sm-9 > div.green-text > h2")
    word=cl.text
    na=word.split(' ')
    sz.append(na[0])
    sz.append(na[1])
    sz.append(na[2])
    s = ' '.join(sz) 
    a.append(s)
    #Key feature
    for klm in range(0,6):
        try:
            element=driver.find_element_by_class_name(kf[klm])
            a.append(int(''.join(filter(str.isdigit, element.text))))
        except NoSuchElementException:
            a.append(0)
    #More features
    for mz in range(13,17):
        try:
            element=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[{}]/div[4]/i""".format(mz))
            frr=mz
            print(frr)
            break;
        except NoSuchElementException:
            bw=1
            
    for mf in range(1,9):
        org=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[{}]/div[{}]/i""".format(frr,mf))
        val = org.get_attribute("class")
        if val=='icon-ok':
            a.append(1)
        if val=='icon-cancel-1':
             a.append(0)
    #NearBy 
    for op in range(18,20):
        try:
            element=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[{}]/div[2]/b""".format(op))
            jk=[]  
            for nb in range(1,7):
                ppp=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[{}]/div[{}]""".format(op,nb))
                word=ppp.text
                jk=word.split(':')
                if jk[1]==' Yes':
                    a.append(1)
                else:
                    a.append(0)
            break;
        except NoSuchElementException:
            bw=1
    else:
        for gh in range(1,7):
            a.append('Null')
    #other details
    for iop in range(19,25):
        try:
            element=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[{}]/div[2]/b""".format(iop))
            nnn=iop
            na=[]
            od=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[{}]/div[1]".format(nnn))
            word=od.text
            na=word.split(' ')
            a.append(na[3]) #year of construction #year of construction
             #no of stories
            na=[]
            od=driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[{}]/div[2]".format(nnn))
            word=od.text
            na=word.split(':')
            a.append(na[1]) 
         #for brand new or furnished
            jk=[]        
            for nb in range(3,5):
                ppp=driver.find_element_by_xpath("""/html/body/div[5]/div[1]/div[1]/div[1]/div[1]/div[{}]/div[{}]""".format(nnn,nb))
                word=ppp.text                       
                jk=word.split(':')
                if jk[1]==' Yes':
                    a.append(1)
                else:
                    a.append(0)
        except NoSuchElementException:
            b=1
    else:      
        for ijjj in range(0,4):
            a.append('Null')
    
    with open('MidEvaluation.csv', 'a') as csvFile:
        writer = csv.writer(csvFile, lineterminator='\r' )
        writer.writerow(a)
    
                
    
   
    
for u in range(10,15):
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0,400);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[1]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[1]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1 
        information(u)
    except:
        mj=1
    
    
    
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,600);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[2]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[2]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=1
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,800);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[3]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[3]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=1
        
        
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,1000);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[4]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[4]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=1
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,1200);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[5]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[5]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
        
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,1400);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[6]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[6]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
    
    
        

   
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,1400);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[7]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[7]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,1600);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[8]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[8]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,2300);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[9]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[9]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,2500);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[10]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[10]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,2700);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[11]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[11]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
  
     
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,3000);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[12]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[12]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,3200);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[13]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[13]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2
  
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,3300);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[14]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[14]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        informationu
    except:
        mj=2
    
    driver.get("https://www.homespakistan.com/?p={}&page=oldsearch&rentOrBuy=Buy&property_cityId=23&property_propertySubtypeId=2&orderType2=1&record_per_page=15&isImage=0&installments=0&property_sub=Please%20Enter%20Area&fresh=AnyTime".format(u))
    driver.execute_script("window.scrollTo(0,3600);")
    time.sleep(2)
    prc=driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[15]/div/div[1]/div[2]/div/h3""")
    try:
        jkpo=int(''.join(filter(str.isdigit, prc.text)))
        driver.find_element_by_xpath("""//*[@id="Featured_agent"]/div[15]/div/div[1]/div[3]/div/div[2]/div""").click()
        counter=counter+1    
        information(u)
    except:
        mj=2

        
    
    
  
