from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import csv,time



pages = 6
detail_list = [['Name', 'Brand', 'Price', 'Image Url', 'Product Url']]

driver = webdriver.Firefox()

driver.get('https://www.matchesfashion.com/intl/mens/shop/shoes?page=1')                    #  selecting country and currency
element = driver.find_element_by_xpath('//*[@id="shipping-country"]')                       #
element.click()                                                                             #
time.sleep(1)                                                                               #
select = driver.find_element_by_id('shippingCountry')                                       #
action = ActionChains(driver)                                                               #
action.click(on_element=select)                                                             #
action.perform()                                                                            # populate list
driver.find_element_by_xpath('//*[@id="settings__wrapper"]/div[1]/div/div/span[73]').click()# selecting country
time.sleep(2)                                                                               # wait for auto selection
button = driver.find_element_by_xpath('//*[@id="command"]/button').click()                  # of currency
                                                                                            # saving settings



for page in range(1, pages+1):                                                              # iterate through result pages
    
    driver.get('https://www.matchesfashion.com/intl/mens/shop/shoes?page='+str(page))

    if page == 6:                                                                           # no of results on last page
        results_per_page = 213
    else:
        results_per_page = 240                                                              # results per page

    

    for result in range(1, results_per_page+1):

        try:
            # fetching elements having product detail
            image = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/div/a/img')
            brand = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/a/div[1]')
            name = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/a/div[2]')
            product = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/a')
            price = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/a/div[3]/span')
        except:
            # In case ,register pop-up appears 
            time.sleep(5)
            driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[1]/div/a').click()       # close pop-up
            image = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/div/a/img')
            brand = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/a/div[1]')
            name = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/a/div[2]')
            product = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/a')
            price = driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result)+']/div/a/div[3]/span')
        finally:
            #saving details
            image_url = image.get_attribute('src')
            brand = brand.text
            name = name.text
            product_url= product.get_attribute('href')
            price = price.text
        
            # scroll upcoming results into view , to load images and get image-url 
        if      result % 3 == 0 and result != 240 and result != 213:
            try:
            	# finding element of next row
                element = driver.find_element_by_xpath(
                    '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result+1)+']/div/a/div[3]/span')
            except:
                time.sleep(5)
                driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/a').click()  # In case pop-up , close it
                element = driver.find_element_by_xpath(
                    '/html/body/div[4]/div[4]/div[1]/div[4]/div[9]/ul/li['+str(result+1)+']/div/a/div[3]/span')
            finally:
            	# scrolling to view next row
                driver.execute_script("arguments[0].scrollIntoView();", element)
                time.sleep(1)


        detail_list.append([name, brand, price, image_url, product_url])    # adding product info to list
       
# name of resulting csv file
filename = "Task 1 Results.csv"

# writing to csv file
with open(filename, 'w', newline='') as file:

    csvwriter = csv.writer(file)
    csvwriter.writerows(detail_list)

driver.close()
