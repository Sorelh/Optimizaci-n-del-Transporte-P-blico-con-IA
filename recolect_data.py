from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from analyze_data import analyze_data
from propose_optimizations import propose_optimizations

def setup_selenium():
    options = Options()
    options.headless = True
    service = Service('C:\\Actividad-8\\chromedriver-win32\\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def collect_data(driver, url):
    driver.get(url)
    time.sleep(20) # Espera a que la página cargue completamente
    tweets = driver.find_elements(By.CSS_SELECTOR, 'article')
    data = [tweet.text for tweet in tweets]
    print(f"collect_data: {data}")
    return data

if __name__ == "__main__":
    driver = setup_selenium()
    data = collect_data(driver, 'https://twitter.com/search?q=transporte%20publico%20Bogota&src=typed_query')
    driver.quit()
    issues = analyze_data(data)
    propose_optimizations(issues=issues)