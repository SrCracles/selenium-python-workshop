from behave import given, when, then
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By

@given('the user is loged in the page')
def step_user_loged(context):
    context.driver = webdriver.Chrome()  # o webdriver.Firefox()
    context.driver.get("https://www.saucedemo.com/v1/index.html")
    context.login_page = LoginPage(context.driver)
    context.inventory_page = InventoryPage(context.driver)
    context.login_page.login("standard_user", "secret_sauce")

@when('the user add two products to the cart, go to the cart, and then quit one')
def step_user_add_two_and_quit_one(context):
    context.inventory_page.add_two_products()
    context.inventory_page.go_to_cart()
    context.inventory_page.remove_one()


@then('the cart should have just one product')
def step_the_cart_should_have_one_product(context):
    quantity = context.inventory_page.quantity_buttons_in_cart()
    assert quantity == 1

def after_scenario(context, scenario):
    context.driver.quit()