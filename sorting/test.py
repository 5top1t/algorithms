from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get('https://www.random.org/integer-sets/?sets=10&num=1000&min=1&max=1000&commas=on&order=random&format=html&rnd=new')

elem = browser.find_elements_by_css_selector('li')  # Find the search box
print(elems)

browser.quit()