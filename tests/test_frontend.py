import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_products_frontend():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("https://devops-frontend-staging.azurewebsites.net")

    product_table = driver.find_element(
        By.CLASS_NAME, "product-table-container")
    assert product_table is not None

    add_product_form = driver.find_element(
        By.CLASS_NAME, "add-product-container")
    assert add_product_form is not None

    name_input = add_product_form.find_element(By.ID, "name")
    name_input.send_keys("New Product")
    desc_input = add_product_form.find_element(By.ID, "description")
    desc_input.send_keys("A new product")
    quantity_input = add_product_form.find_element(By.ID, "quantity")
    quantity_input.send_keys("5")
    price_input = add_product_form.find_element(By.ID, "price")
    price_input.send_keys("1.8")
    add_button = add_product_form.find_element(By.ID, "add")
    add_button.submit()

    time.sleep(5)

    product_table = driver.find_element(
        By.CLASS_NAME, "product-table-container")
    new_product_row = product_table.find_element(
        By.XPATH, "/html/body/div/table/tbody/tr[13]")
    assert new_product_row is not None

    driver.quit()
