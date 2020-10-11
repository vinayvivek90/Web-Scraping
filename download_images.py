from selenium import webdriver
from time import sleep
import pyautogui
import csv
from os import path



filename = 'Task 1 Results.csv'

with open(filename,'r') as file:			#read data from file
	data = csv.reader(file)
	data = list(data)

driver = webdriver.Chrome()
#Window maximization
driver.maximize_window()


for detail in data[1:]:
	filename = detail[3].split('/')[-1]		# getting filename from url
	if path.exists('images/'+filename):
		continue
	else:
		driver.get(detail[3])				# getting image
		sleep(1)
		pyautogui.hotkey('ctrlleft','s')	#saving it
		sleep(1)
		pyautogui.press('enter')
		sleep(1)
		
		print(data.index(detail))

driver.close()