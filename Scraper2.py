from selenium import webdriver
import csv

driver = webdriver.Firefox()

pages = 35
detail_list= [['Name','Brand','Price','Image Url','Product Url']]

for page in range(1,pages+1):	# iterate through result pages
	driver.get('https://www.blue-tomato.com/de-AT/products/categories/Snowboard+Shop-00000000/?page='+str(page))
	if page == 35 :				#
		results= 26				# result count on last page
	else:						#
		results=96				# result count per page

	for result in range(results):
		element 	= driver.find_element_by_xpath('//*[@id="p'+str(result)+'"]/span[1]/img')		#
		image_url 	= element.get_attribute('src')													#
		element 	= driver.find_element_by_xpath('//*[@id="p'+str(result)+'"]/span[2]/a')			# getting result details
		name 		= element.get_attribute('data-productname')										#
		brand 		= element.get_attribute('data-brand')											#
		product_url = element.get_attribute('href')													#
		element 	= driver.find_element_by_xpath('//*[@id="p'+str(result)+'"]/span[2]/span[1]')	#
		price 		= element.text
		if 'statt' in price:
			price 	= 	price[:price.find('s')]						# removing old price

		detail_list.append([name,brand,price,image_url,product_url])# saving details in a list
		
# name of resulting csv file  
filename = "Task 2 Results.csv"
    
# writing to csv file  
with open(filename, 'w', newline='') as file:  
      
    csvwriter = csv.writer(file)  
    csvwriter.writerows(detail_list) 		

driver.close()