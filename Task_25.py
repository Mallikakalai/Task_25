from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_path = r"D:\Python_HW\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the IMDB search page
driver.get("https://www.imdb.com/search/name/")
driver.maximize_window()

##Expand the section##
expand = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,"button[data-testid='adv-search-expand-all']")))
actions = ActionChains(driver)
actions.click(expand)
actions.perform()

##Input for Name##
driver.implicitly_wait(20)
name_input=driver.find_element(By.CSS_SELECTOR,"input[name='name-text-input']")
name_input.send_keys("Audrey")

#Input for Birthdate##
driver.implicitly_wait(20)
birth_date_start_input=driver.find_element(By.CSS_SELECTOR,"input[name='birth-date-start-input']")
birth_date_start_input.send_keys("14071990")
birth_date_end_input=driver.find_element(By.CSS_SELECTOR,"input[name='birth-date-end-input']")
birth_date_end_input.send_keys("14072000")

#Input for Birthday##
driver.implicitly_wait(20)
birthday_input=driver.find_element(By.CSS_SELECTOR,"input[name='birthday-input']")
actions = ActionChains(driver)
actions.send_keys_to_element(birthday_input,"06-14")
actions.send_keys(Keys.RETURN)
actions.perform()

##Input for Awards##
driver.implicitly_wait(20)
awards_input = driver.find_element(By.CSS_SELECTOR,"button[data-testid='test-chip-id-oscar_best_supporting_actress_winners']")
actions = ActionChains(driver)
actions.click(awards_input)
actions.perform()

##Input for Topics##
driver.implicitly_wait(20)
topic_dropdown = driver.find_element(By.ID,"within-topic-dropdown-id")
actions = ActionChains(driver)
actions.click(topic_dropdown)
actions.perform()
selectoption = Select(topic_dropdown)
selectoption.select_by_value("BIRTH_PLACE")

##Input for topictext##
topic_text_input=driver.find_element(By.CSS_SELECTOR,"input[name='within-topic-input']")
actions = ActionChains(driver)
actions.send_keys_to_element(topic_text_input,"United States")
actions.send_keys(Keys.RETURN)
actions.perform()

##Input for DeathDate##
driver.implicitly_wait(20)
death_date_start_input=driver.find_element(By.CSS_SELECTOR,"input[name='death-date-start-input']")
death_date_start_input.send_keys("23092000")
death_date_end_input=driver.find_element(By.CSS_SELECTOR,"input[name='death-date-end-input']")
death_date_end_input.send_keys("23092005")

##Input for Gender##
driver.implicitly_wait(20)
gender_input = driver.find_element(By.CSS_SELECTOR,"button[data-testid='test-chip-id-FEMALE']")
actions = ActionChains(driver)
actions.click(gender_input)
actions.perform()

##Input for Credit##
driver.implicitly_wait(20)
credit_input=driver.find_element(By.CSS_SELECTOR,"input[data-testid='autosuggest-input-test-id-filmography']")
actions = ActionChains(driver)
actions.click(credit_input)
actions.send_keys_to_element(credit_input,"Holiday")
actions.pause(2)
actions.send_keys(Keys.DOWN)
actions.pause(2)
actions.send_keys(Keys.ENTER)
actions.perform()

##Input for adults##
adultnames_input=driver.find_element(By.CSS_SELECTOR,"input[id='include-adult-names']")
actions = ActionChains(driver)
actions.click(adultnames_input)
actions.perform()


##See Results##
seeresults=driver.find_element(By.CSS_SELECTOR,"button[data-testid='adv-search-get-results']")
seeresults.click()