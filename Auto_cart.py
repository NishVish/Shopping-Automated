import pandas as pd
url = "https://www.mysmartprice.com/mobile/pricelist/latest-mobile-phones.html"
url_data = pd.read_html(url)
data = url_data[0]
phone = list(data['Mobile Phones'])

# chrome_options = Options()
# chrome_options.add_argument("C:\Program Files\Google\Chrome\Application\chrome.exe")  # Replace with the actual path
# driver = webdriver.Chrome(options=chrome_options)
# wait = WebDriverWait(driver, 10)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import webbrowser
from tkinter import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


def seach_this():
    seach_q = search_entry.get()
    pin_adress = your_pin.get()

    chrome_options = Options()
    chrome_options.add_argument("C:\Program Files\Google\Chrome\Application\chrome.exe")  # Replace with the actual path
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    if (pin_adress):
        stri = seach_q.replace(' ', "+"); 
        driver.get("https://www.amazon.in/s?k="+stri)
        time.sleep(2)

        #entering location 
        setting_pin = driver.find_element(By.XPATH, "//a[@id='nav-global-location-popover-link']")
        setting_pin.click()

        #writing the pin
        time.sleep(2)
        writing_pin = driver.find_element(By.XPATH, "//input[@class='GLUX_Full_Width a-declarative']")
        writing_pin.click()
        writing_pin.send_keys(int(pin_adress))
        writing_pin.send_keys(Keys.RETURN)
        
        time.sleep(5)
        # Click on the first search result
        first_result = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
        first_result.click()
    
        #Wait for the product page to load
        time.sleep(2)
        
        driver.switch_to.window(driver.window_handles[2])
    
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='add-to-cart-button']")))
        add_to_cart_button.click()
        add_to_cart_button.click()
        add_to_cart_button.click()

        time.sleep(2)
    else :

        string = seach_q.replace(' ', "+"); 
        driver.get("https://www.amazon.in/s?k="+ string)
        

        time.sleep(5)
        first_result = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
        first_result.click()
        

        time.sleep(2)
        
        driver.switch_to.window(driver.window_handles[2])

    
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='add-to-cart-button']")))
        add_to_cart_button.click()
        add_to_cart_button.click()
        add_to_cart_button.click()
        time.sleep(2)

            
def add_this_iteem():
    selected_phone = phone_var.get()
    selected_variant = variant_var.get()
    pin_adress = your_pin.get()

    chrome_options = Options()
    chrome_options.add_argument("C:\Program Files\Google\Chrome\Application\chrome.exe")  # Replace with the actual path
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    if(pin_adress):

        selected_p = selected_phone.replace(' ', "+")
        driver.get("https://www.amazon.in/s?k="+selected_p+" "+selected_variant)
    
        
        setting_pin = driver.find_element(By.XPATH, "//a[@id='nav-global-location-popover-link']")
        setting_pin.click()
    
        time.sleep(3)
        #writing the pin
        writing_pin = driver.find_element(By.XPATH, "//input[@class='GLUX_Full_Width a-declarative']")
        writing_pin.click()
        writing_pin.send_keys(pin_adress)
        writing_pin.send_keys(Keys.RETURN)

        time.sleep(5)

        first_result = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
        first_result.click()
    
        time.sleep(2)
        
        driver.switch_to.window(driver.window_handles[2])

        # driver.get("https://instagram.com")
        add_to_cart_button = driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']")
        add_to_cart_button.click()
        add_to_cart_button.click()
        add_to_cart_button.click()
        time.sleep(10)

        driver.quit()

    else:
        selected_p = selected_phone.replace(' ', "+")
        driver.get("https://www.amazon.in/s?k="+selected_p+" "+selected_variant)
    
        time.sleep(5)
        first_result = driver.find_element(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
        first_result.click()
    
        time.sleep(2)
        
        # Get the window handles of all tabs
        driver.switch_to.window(driver.window_handles[2])
  
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='add-to-cart-button']")))
        add_to_cart_button.click()
        add_to_cart_button.click()
        add_to_cart_button.click()

    #

# Create UI using tkinter
import tkinter as tk
root = Tk()
root.title("Amazon Cart Automation")

# Set the default size of the UI (width x height)
default_width = 350
default_height = 190
root.geometry(f"{default_width}x{default_height}")

search_label = Label(root, text="Enter Your Pincode")
search_label.pack()

your_pin_var = StringVar()
your_pin = Entry(root, textvariable=your_pin_var)
your_pin.pack()


phones = phone
phone_var = StringVar()
phone_var.set(phones[0])
phone_dropdown = OptionMenu(root, phone_var, *phones)
phone_dropdown.pack()

variants = ["64GB","128GB", "256GB"]
variant_var = StringVar()
variant_var.set(variants[0])
variant_dropdown = OptionMenu(root, variant_var, *variants)
variant_dropdown.pack()

add_this_item = Button(root, text="Add this Item", command=add_this_iteem)
add_this_item.pack()

search_label = Label(root, text="Or Direct Search on Amazon:")
search_label.pack()

search_var = StringVar()
search_entry = Entry(root, textvariable=search_var)
search_entry.pack()

add_to_cart_button = Button(root, text="Search and Add to Cart", command=seach_this)
add_to_cart_button.pack()

root.mainloop()
