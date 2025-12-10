import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from  .pages.basket_page import BasketPage
import time




@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):

    page = ProductPage(browser, link)
    page.open()


    page.add_to_cart_from_product_page()

    price_in_item_page = page.get_item_price()
    book_name = page.get_item_name()
    page.check_message_about_item_add_to_cart(book_name)
    page.check_price_in_cart(price_in_item_page)



@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):

    page = ProductPage(browser, link)
    page.open()

    page.add_to_cart_from_product_page()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_from_product_page()
    page.should_disappeared_success_message()



@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_be_message_about_empty_cart()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty()
    basket_page.should_be_message_about_empty_cart()