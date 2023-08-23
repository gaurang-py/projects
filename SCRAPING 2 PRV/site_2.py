from selenium import webdriver
from twocaptcha import TwoCaptcha
from csv import reader
import mysql.connector
import pandas as pd

########### FUNCTION TO CONVERT STRING FROM LIST ##############
def listToString(s): 
    str1 = ""  
    for ele in s: 
        str1 += ele
    return str1 

############### LOOPING THROUGH ALL ELEMENTS OF GIVEN INPUTS #################
with open('./inputs.csv','r') as record:
    csv_reader = reader(record)
    for row in csv_reader:
        value = row
        print(listToString(row))

        ##########  MYSQL DATABASE CHANGE CREDS BEFORE USE #################
        cnx = mysql.connector.connect(user='root', password='Patel4717@',host='localhost',database='a')

        ############# MYSQL INSERT QUERYS FOR BOTH OF THE TABLES ##################
        add_data = ("INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
        add_fil_nam = ("insert into file1 values(%s,%s,%s);")
        cursor= cnx.cursor()
        value =" "
        no = row
        ############2captcha.com API KEY################
        api_key = "f73f72c687903f05eaaff89b25e793a0"
        ################## CHROME DRIVER (Use As Per Yours Chrome Version) #############
        driver = webdriver.Chrome("./chromedriver.exe")

        ##### MANDATORY FOR CREATING COOKIES AS THIS SITE IS WELL DESIGNED #####
        driver.get('https://ip**********.gov.in/PublicSearch/PublicationSearch/')
        driver.get("https://ip**********.gov.in/PublicSearch/PublicationSearch/ApplicationStatus")
        driver.find_element_by_id("ApplicationNumber").send_keys(no)

        ########## CAPTCHA IMAGE DOWNLOADER ########
        with open('captcha_new.png', 'wb') as file:
            l = driver.find_element_by_id('Captcha')
            file.write(l.screenshot_as_png)

        ########### SENDING THE DOWNLOADED CAPTCHA TO 2CAPTCHA #########
        solver = TwoCaptcha(api_key)
        try:
            result = solver.normal('./captcha_new.png')
        except Exception as e:
            print('')
        else:
            ####### GETS AND ENTERS THE SOLVED CAPTCHA AND CONTNIUES THE PROCESS #############
            print(result['code'])
            driver.find_element_by_id("CaptchaText").send_keys(result['code'])
            driver.find_element_by_name('submit').click()
            ###### PATHS OF ALL THE DATA THAT NEEEDS TO BE SCRAPED###############
            application_number= driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[2]/td[2]").text
            application_type= driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[3]/td[2]").text
            date_of_filling= driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[4]/td[2]").text
            applicant_name= driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[5]/td[2]").text
            title_of_invention= driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[6]/td[2]").text
            field_of_invention= driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[7]/td[2]").text
            email= driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[8]/td[2]").text
            email_2= driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[9]/td[2]").text
            email_upd = driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[10]/td[2]").text
            application_number_int = driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[11]/td[2]").text
            pct_application_date = driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[12]/td[2]").text
            prio_date = driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[13]/td[2]").text
            req_date = driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[14]/td[2]").text
            publ_date = driver.find_element_by_xpath("//table[@class='table-striped']/tbody/tr[15]/td[2]").text
            ############ ALL DATA THAT NEEDS TO BE SAVED INTO THE TABLE ###########
            data = (int(application_number),str(application_type),str(date_of_filling),str(applicant_name),str(title_of_invention),str(field_of_invention),str(email),str(email_2),str(email_upd),str(application_number_int),str(pct_application_date),str(prio_date),str(req_date),str(publ_date))
            cursor.execute(add_data,data)
            ################### GETTING THE THE FILES UPLODED #############
            driver.find_element_by_name("SubmitAction").click()
            file_name = driver.find_elements_by_xpath("//table[@class='table-striped']/tbody/tr/td[1]")
            file_upload_date = driver.find_elements_by_xpath("//table[@class='table-striped']/tbody/tr/td[1]")
            ################### LOOPING THROUGH ALL THE FILES ####################
            for z in file_name:
                value = str(value) + "," + str(z.text)
            files = (int(application_number),len(file_name),value)
            cursor.execute(add_fil_nam,files)
            cnx.commit()
            ######## STORING DATA INTO CSV FOR EASY ACCESS ##########
            cursor.execute("SELECT * FROM DATA")
            data = cursor.fetchall()
            cursor.execute("SELECT * FROM file1")
            files = cursor.fetchall()
            df_data = pd.DataFrame(data)
            df_file = pd.DataFrame(files)   
            df_data.to_csv("INPAS_SCRAPED.csv")
            df_file.to_csv("INPAS_SCRAPED_files.csv")
            cursor.close()
            cnx.close()
            driver.quit()