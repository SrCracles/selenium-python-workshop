from selenium.webdriver.common.by import By
from .base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, 'inventory_list')
    ADD_BUTTON1 = (By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[3]/button')
    ADD_BUTTON2 = (By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[3]/button')
    CART_BUTTON = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    REMOVE_BUTTON = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[2]/div[2]/button')

    def is_inventory_page_displayed(self):
        return self.find_element(self.TITLE).is_displayed()
    
    def add_two_products(self):
        self.click(self.ADD_BUTTON1)
        self.click(self.ADD_BUTTON2)

    def go_to_cart(self):
        self.click(self.CART_BUTTON)


    def remove_one(self):
        self.click(self.REMOVE_BUTTON)

    def quantity_buttons_in_cart(self):
        buttons = self.driver.find_elements(By.XPATH, "//button[text()='REMOVE']")
        return len(buttons)
        
