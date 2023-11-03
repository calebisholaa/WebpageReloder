import pyautogui
import time
from selenium import webdriver
from time import sleep
import schedule
import time

link ="https://www.etsu.edu/gradschool/" 

def RefreshWebPage(url =link, NumOfTimeToRefresh=4, RefreshRateInSeconds=7200):
    print("Refreshing.....")
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()

    for i in range(NumOfTimeToRefresh):   #number of times you want to refresh
        time.sleep(RefreshRateInSeconds)  #refresh rate in seconds 
        pyautogui.hotkey('f5')

    driver.quit()



schedule.every().day.at("08:00").do(RefreshWebPage)    #refresh 4 times days after 2hrs(7200 seconds)
        


while True:
    schedule.run_pending()
    time.sleep(1)
#RefreshWebPage(url, 4, 7200)   #refresh 4 times days after 7hrs(7200 seconds)





'''
while True:
now = datetime.now()
if now.hour==9 and now.minute==30:
print(“Its time to run the code”)
# Call your CODE() function here
break

https://pypi.org/project/schedule/
'''