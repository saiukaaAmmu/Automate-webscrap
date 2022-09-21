#----Ammu K webscraping using Selenium-python--------

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "C:/Users/webdriver/chromedriver.exe" #driver path
driver = webdriver.Chrome(PATH)
driver.get("https://www.amazon.in")
driver.maximize_window()

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("dell laptops")
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.XPATH, "//span[text()='Dell']").click()

Laptops = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')

Laptop_Name = []
Laptop_Price = []
No_reviews = []
Final_List = []

for laptop in Laptops:

    names = laptop.find_elements(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']")
    for name in names:
        Laptop_Name.append(name.text)

    try:
        if len(laptop.find_elements(By.XPATH, ".//span[@class='a-price-whole']")) > 0:
            prices = laptop.find_elements(By.XPATH, ".//span[@class='a-price-whole']")
            for price in prices:
                # print('the lenght is ===>',len(price.text))
                Laptop_Price.append(price.text)
        else:
            Laptop_Price.append("0")
    except:
        pass
    # reviews = laptop.find_elements(By.XPATH,".//span[@class='a-size-base s-underline-text']")

    try:
        if len(laptop.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")) > 0:
            reviews = laptop.find_elements(By.XPATH, ".//span[@class='a-size-base s-underline-text']")
            for review in reviews:
                # print('the length is===>', len(review.text), review.text)
                No_reviews.append(review.text)
        else:
            No_reviews.append("0")
    except:
        pass

print('number of laptops==>', len(Laptop_Name))
print('number of prices==>', len(Laptop_Price))
print('number of reviews==>', len(No_reviews))

#excel creation and storing scraped datas

df = pd.DataFrame(zip(Laptop_Name, Laptop_Price, No_reviews), columns=['Laptop Name', 'Laptop Price', 'No Of reviews'])

df.to_excel("laptops.xlsx", index=False)

driver.quit()
