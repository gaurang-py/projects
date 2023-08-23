from selenium import webdriver
from twocaptcha import TwoCaptcha
import mysql.connector
from csv import reader
import pandas as pd
####### FUNCTION TO CONVERT STRING FROM LIST ##############
def listToString(s): 
    str1 = ""  
    for ele in s: 
        str1 += ele
    return str1 



############### LOOPING THROUGH ALL ELEMENTS OF GIVEN INPUTS #################
with open('./inputs1.csv','r') as record:
    csv_reader = reader(record)
    for row in csv_reader:
        value = row
        print(listToString(row))

        ############2captcha.com API KEY################
        api_key = ('f73f72c687903f05eaaff89b25e793a0')
        user=row

        ##########  MYSQL DATABASE CHANGE CREDS BEFORE USE #################
        cnx = mysql.connector.connect(user='root', password='Patel4717@',host='localhost',database='a')
        cursor= cnx.cursor()

        ################## CHROME DRIVER (Use As Per Yours Chrome Version) #############
        driver = webdriver.Chrome("./chromedriver.exe")#Chrome Driver
        driver.get("https://ip********.gov.in/eregister/Application_View.aspx")
        driver.find_element_by_id("rdb_0").click()
        driver.find_element_by_id("applNumber").send_keys(user)

        ########## CAPTCHA IMAGE DOWNLOADER #########
        img = driver.find_element_by_id("ImageCaptcha")
        src = img.get_attribute('src')
        with open('captcha.png', 'wb') as file:
            l = driver.find_element_by_id('ImageCaptcha')
            file.write(l.screenshot_as_png)

        ########### SENDING THE DOWNLOADED CAPTCHA TO 2CAPTCHA #########
        solver = TwoCaptcha(api_key)
        try:
            result = solver.normal('./captcha.png')
        except Exception as e:
            print('')
        else:
            ######## GETS AND ENTERS THE SOLVED CAPTCHA AND CONTNIUES THE PROCESS #############
            print(result['code'])
            driver.find_element_by_id("captcha1").send_keys(result['code'])
            driver.find_element_by_id("btnView").click()
            trademarkno = driver.find_element_by_xpath('//table[@id="SearchWMDatagrid"]/tbody/tr[2]/td[1]').text
            clas = driver.find_element_by_xpath('//table[@id="SearchWMDatagrid"]/tbody/tr[2]/td[2]').text
            application_data = driver.find_element_by_xpath('//table[@id="SearchWMDatagrid"]/tbody/tr[2]/td[3]').text
            trademark = driver.find_element_by_xpath('//table[@id="SearchWMDatagrid"]/tbody/tr[2]/td[3]').text
            pro_name = driver.find_element_by_xpath('//table[@id="SearchWMDatagrid"]/tbody/tr[2]/td[5]').text
            data_2= ("str(trademarkno)","str(clas)","str(application_data)","str(trademark)","str(pro_name)")
            driver.find_element_by_id("SearchWMDatagrid_ctl03_lnkbtnappNumber1").click()
            ######### SECOND PAGE ####################
            as_on_date = driver.find_element_by_xpath("//table[2]/tbody/tr[2]/td").text
            status = driver.find_element_by_xpath("//table[2]/tbody/tr[2]/td").text
            office = driver.find_element_by_xpath("//table[3]/tbody/tr[4]/td[2]").text
            state = driver.find_element_by_xpath("//table[3]/tbody/tr[5]/td[2]").text
            country = driver.find_element_by_xpath("//table[3]/tbody/tr[6]/td[2]").text
            filling_mode = driver.find_element_by_xpath("//table[3]/tbody/tr[7]/td[2]").text
            applies_for = driver.find_element_by_xpath("//table[3]/tbody/tr[8]/td[2]").text
            catergory = driver.find_element_by_xpath("//table[3]/tbody/tr[9]/td[2]").text
            type = driver.find_element_by_xpath("//table[3]/tbody/tr[10]/td[2]").text
            user_details = driver.find_element_by_xpath("//table[3]/tbody/tr[11]/td[2]").text
            certificate_details = driver.find_element_by_xpath("//table[3]/tbody/tr[12]/td[2]").text
            valid_upto = driver.find_element_by_xpath("//table[3]/tbody/tr[13]/td[2]").text
            prop_add = driver.find_element_by_xpath("//table[3]/tbody/tr[15]/td[2]").text
            email = driver.find_element_by_xpath("//table[3]/tbody/tr[16]/td[2]").text
            attorny_name = driver.find_element_by_xpath("//table[3]/tbody/tr[17]/td[2]").text
            attorny_add = driver.find_element_by_xpath("//table[3]/tbody/tr[18]/td[2]").text
            good_services_details = driver.find_element_by_xpath("//table[3]/tbody/tr[18]/td[2]").text

            ############################ MYSQL INSERT QUERY #########################################
            add_trademark ="insert into trademark_full values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') "%\
            (int(trademarkno),str(clas),str(application_data),str(trademark),str(pro_name),str(as_on_date),str(status),str(office),str(state),str(country),
                        str(filling_mode),str(applies_for),str(catergory),str(type),str(user_details),str(certificate_details),str(valid_upto),str(prop_add),str(email),str(attorny_name),
                        str(attorny_add),str(good_services_details))
            cursor.execute(add_trademark)
            cursor.execute("SELECT * FROM trademark_full")
            data = cursor.fetchall()
            df_file = pd.DataFrame(data)
            df_file.to_csv("Trade_Marks_Scraped.csv") 
            cnx.commit()
            cursor.close()
            cnx.close()
            driver.quit()