# -*- coding: utf-8 -*-
"""
https://selenium-python.readthedocs.io/waits.html
"""

import os
import sys
import time
from selenium import webdriver
import pandas as pd
from os import listdir
from os.path import isfile, join
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


orig_stdout = sys.stdout
f = open('C:\\Users\\XXXXXXXXXX\\python_learning\\LOG\\AutoLoginWait.log', 'w')
sys.stdout = f

################
def FILENAMELIST():
        data = pd.read_csv("C:/Users/XXXXXXXXXX/python_learning/listname.csv",sep=',')
        data.headername
        count=0
        for opt in data.headername:
                ##try: 
                    AA=len(data.headername)
                    count +=1
                    print("===================== LOGIN",opt,count,"\\",AA,"=============================================")
                    url ="http://google.com:80/n.u15.0/inton/vw/?predefrtId=116664&mame=" + str(opt)
                    print("current url:", url)
                    driver.get(url)
                    time.sleep(5)
                    driver.set_window_size(1080,800)
                    scrname ="C:/Users/XXXXXXXXXX/python_learning/pic/1/" + str(opt) + ".png"
                    #driver.save_screenshot(scrname)
                    print ("Executed Succesfull")
                    screen = driver.get_screenshot_as_png()
                    # Crop it back to the window size (it may be taller)
                    #box = (0, 0, 1366, 728)
                    box = (0, 0, 480, 320)
                    #im = Image.open(StringIO.StringIO(screen))
                    #Image.open('old.jpeg').convert('RGB').save('new.jpeg')
                    im = Image.open(BytesIO(screen)).convert('RGB')
                    region = im.crop(box)
                    region.save(scrname, 'PNG', optimize=True, quality=95)
                    #print("===================== LOGOUT",count,"\\",AA,"=============================================")
        driver.close()
        driver.quit() 


def MaunalloginUser():
  # Open your browser, and point it to the login page
  driver.get("http://google.com:80/n.u15.0/login.jsp")   
  print("current url 1:",driver.current_url)
     # getpass.getpass("press enter") #< THIS IS THE SECOND PART
    #Here is where you put the rest of the code you want to execute
    ###

    # Explicit wait example
  try:
        wait = WebDriverWait(driver, 10)
        print("current url 2:",driver.current_url)
        wait.until(EC.element_to_be_clickable((By.ID, 'nv2')))
        # implicit wait example
        driver.implicitly_wait(10) # seconds
        print("current url 3:",driver.current_url)
        FILENAMELIST()            
  finally:
        print("defined timerange timeout")    
        driver.quit()
        
def filesize():
        mypath ="C:/Users/XXXXXXXXXX/python_learning/pic/1/"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        #print(onlyfiles)
        print("=============output on the basis of size of the image================================")
        for opt in onlyfiles:
            ff =mypath + opt
            #print(ff)
            fsize=os.stat(ff)
            #print(fsize)
            #print('size:' + fsize.st_size.__str__())
            #6091 7085
            if fsize.st_size <= 7085:     
                print(opt.strip('.png'),fsize.st_size,"failed to redirect !",sep=',')
            else:
                print(opt.strip('.png'),fsize.st_size,"working",sep=',')


if __name__ == "__main__":
    
        # get the path of ChromeDriverServer , keep chromedriver and script in same folder.
        dir = os.path.dirname(__file__)
        print(dir)
        dir = "C:\\Users\\XXXXXXXXXX\\python_learning\\chromedriver_win32\\"
        chrome_driver_path = dir + "chromedriver.exe"        
        # create a new Chrome session
        #driver=webdriver.Chrome(executable_path="C:/Users/XXXXXXXXXX/python_learning/chromedriver.exe")
        driver=webdriver.Chrome(chrome_driver_path)
        driver.implicitly_wait(30)
        driver.maximize_window()
        MaunalloginUser()
        filesize()


sys.stdout = orig_stdout
f.close()  
