from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time
import pandas as pd

url = "https://urbanoutfitters.com/womens-clothing"

driver = Driver(uc=True)

driver.get(url)
time.sleep(25)

product_list = driver.find_elements(By.CLASS_NAME,"o-pwa-product-tile")
product_name_list = []
price_list = []

for product in product_list:
    product_name_list.append(product.find_element(By.CLASS_NAME,"o-pwa-product-tile__heading").text)
    price_list.append(product.find_element(By.CLASS_NAME,"c-pwa-product-price__current").text)

product_dict = {
    "product name" : product_name_list,
    "price" : price_list
}

df = pd.DataFrame(product_dict)
df.to_csv('product.csv')
print(df['price'][0])

driver.quit()