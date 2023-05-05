import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.selenium
def test_products_frontend():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:8081")

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
    add_button = add_product_form.find_element(By.TAG_NAME, "button")
    add_button.click()

    next_button = driver.find_element(By.CLASS_NAME, "next-button")
    while True:
        disabled_attr = next_button.get_attribute("disabled")
        if disabled_attr is None or disabled_attr == "disabled":
            break
        next_button.click()
        time.sleep(1)

    new_product_row = product_table.find_element(
        By.XPATH, "//*[@id='app']/div/table/tbody/tr[4]/td[1]")
    assert new_product_row is not None

    del_button = driver.find_element(
        By.XPATH, "//*[@id='app']/div/table/tbody/tr[4]/td[5]/button")
    del_button.click()

    with pytest.raises(Exception):
        product_table.find_element(
            By.XPATH, "//*[@id='app']/div/table/tbody/tr[6]/td[1]")

    driver.quit()
