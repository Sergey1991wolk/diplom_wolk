from selenium.webdriver.common.by import By

user_name_field = (By.ID, 'user_login')
user_password_field = (By.ID, 'user_pass')

wrong_login_message = (By.ID, 'login_error')

remember_me = (By.ID, 'rememberme')
login_button = (By.ID, 'wp-submit')

#rem_me_check = (By.XPATH, '//div[@id="block_top_menu"]/ul/li[2]/a')
#lang_combobox = (By.CLASS_NAME, 'shopping_cart')
#lang_change_button = (By.CSS_SELECTOR, 'select[id="selectProductSort"]')
