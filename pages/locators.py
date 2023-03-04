from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a > span')
    FILTER_BY_TYPE = (By.ID, 'typesSelector')
    FILTER_BY_DOG = (By.ID, 'pv_id_2_0')


class ProfilePageLocators:
    LOGO_BTN = (By.CLASS_NAME, 'p-menubar-start')
    ADD_PET_BTN = (By.CSS_SELECTOR, '#app > main > div > div > div.p-dataview-header > div > div:nth-child(1) > button')
    ADD_PET_NAME = (By.ID, 'name')
    ADD_PET_AGE = (By.CSS_SELECTOR, '#age > input')
    CHOOSE_PET_TYPE = (By.CSS_SELECTOR, '#typeSelector')
    CHOOSE_PET_TYPE_DOG = (By.XPATH, '//*[@aria-label="dog"]')
    CHOOSE_PET_GENDER = (By.CSS_SELECTOR, '#genderSelector')
    CHOOSE_PET_GENDER_MALE = (By.XPATH, '//*[@aria-label="Male"]')
    SUBMIT_ADD_PET_BTN = (By.XPATH, '//*[@id="app"]/main/div/div/form/div/div[2]/div[3]/button[1]')
