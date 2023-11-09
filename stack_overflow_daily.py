import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 600))
display.start()
chrome_options = Options()

#CHANGE THIS LINE     chrome://version/ Profile Path /home/{user}/.config/chromium
print('MAKE SURE TO CHANGE USER DATA LINE')
chrome_options.add_argument("--user-data-dir=/home/pi/.config/chromium")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--disable-setuid-sandbox")
chrome_options.add_argument("--headless")
#You can find this with the command  ->  which chromedriver
dr=webdriver.Chrome(service=ChromeService('/usr/bin/chromedriver'),options=chrome_options)

dr.get('https://stackoverflow.com/')
#Or make a list of stack sites to visit
'''
sites=['https://stackoverflow.com/','https://ai.stackexchange.com/']
for site in sites:
	dr.get(site)
	source=dr.page_source
	#print(source.index('First Last'),' index of First Last')
	#Add sleep to ensure loading of page
	time.sleep(15)
'''
#for testing to find your name in source
#source=dr.page_source
#print(source.index('First Last'),' index of First Last')

#testing to check if on ask question page
#out=dr.find_elements(by=By.XPATH,value='//a[@href="/questions/ask"]')
#print(out,1)
#out=dr.find_elements(by=By.XPATH,value='//a[text()="\n        Ask Question\n    "]')
#print(out,2)

time.sleep(15)
dr.close()
display.stop()
